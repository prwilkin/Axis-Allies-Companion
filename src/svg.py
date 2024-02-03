from PySide6.QtCore import QObject, Slot, QUrl
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtWebEngineWidgets import QWebEngineView

from src.mainBackend import changeOwner, updateTerritory, colorPicker


# svg will be loaded in this webEngineView class
class svgViewer(QWebEngineView):
    def __init__(self, mainWindowUI):
        super(svgViewer, self).__init__()

        # Set up QWebChannel: allows flow between Py app and JS window
        self.channel = QWebChannel()
        self.myObject = MyObject(mainWindowUI)
        self.channel.registerObject('myObj', self.myObject)
        self.page().setWebChannel(self.channel)

        # load SVG and HTML
        self.load(QUrl.fromLocalFile('C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/board.html'))


# This class is the tool for communicating between Py and JS
class MyObject(QObject):
    def __init__(self, mainWindowUI):
        super().__init__()
        self.mainWindowUI = mainWindowUI
        self.convoy = [1, 6, 10, 19, 20, 26, 35, 36, 37, 39, 41, 42, 43, 44,
                        54, 62, 63, 70, 71, 72, 80, 82, 85, 89, 93, 97, 98,
                        99, 101, 105, 106, 109, 119, 125]

    # JS to Py that handles click events in the svg
    @Slot(str)
    def receiveId(self, element_id):
        print("Clicked on element with ID:", element_id)
        status, territory = self.processId(element_id)
        if status:
            print(territory)
            # open window & get country
            country = changeOwner(territory)
            # update backend record keeping
            updateTerritory(territory, country)
            # get color to give to javascript
            color = colorPicker(country)
            self.sendColorToJavaScript(element_id, color)
        else:
            return None

    # Py to JS function to call with group name and color
    @Slot(str, str)
    def sendColorToJavaScript(self, groupName, color):
        print("Send Js")
        script = f"applyColorToGroup('{groupName}', '{color}');"
        self.mainWindowUI.browser.page().runJavaScript(script)

    # cut id into a group id and filter non-eligible out
    def processId(self, element_id):
        # contains seazone, filter with numbers to check for convoy
        if ("Sea Zone" or "sea zone") in element_id:
            split = element_id.split(" ")
            for number in self.convoy:
                if int(split[len(split) - 1]) == number:
                    return True, "Sea Zone" + split[len(split) - 1]

        # Convoys in: 1, 6, 10, 19, 20, 26, 35, 36, 37, 39, 41, 42, 43, 44
        # 54, 62, 63, 70, 71, 72, 80, 82, 85, 89, 93, 97, 98, 99, 101, 105
        # 106, 109, 119, 125
        # contains '_' ignore as its text element
        elif "_" in element_id:
            return False, None
        # Split at ' 0'
        else:
            territory = element_id.split(" 0")
            return True, territory[0]

    # JS to Py Debug channel for console.log since PyCharm Debugger wont enter java script code
    @Slot(str)
    def receiveLog(self, message):
        print("JS log:", message)
