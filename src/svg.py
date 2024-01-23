from PySide6.QtCore import QObject, Slot, QUrl
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtWebEngineWidgets import QWebEngineView


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

    # JS to Py that handles click events in the svg
    @Slot(str)
    def receiveId(self, element_id):
        print("Clicked on element with ID:", element_id)
        # TODO: Add further processing here
        color = self.processId(element_id)
        self.sendColorToJavaScript(element_id, color)

    # Py to JS function to call with group name and color
    @Slot(str, str)
    def sendColorToJavaScript(self, groupName, color):
        print("Send Js")
        script = f"applyColorToGroup('{groupName}', '{color}');"
        self.mainWindowUI.browser.page().runJavaScript(script)

    def processId(self, element_id):
        # TODO
        # Logic to determine color based on element_id
        # For example, return a color string like '#FF5733'
        return '#2870BA'
        # US Green #186518
        # France Blue #2870BA
        # Germany Black #626262
        # USSR Red #BB0000
        #

    # JS to Py Debug channel for console.log since PyCharm Debugger wont enter java script code
    @Slot(str)
    def receiveLog(self, message):
        print("JS log:", message)
