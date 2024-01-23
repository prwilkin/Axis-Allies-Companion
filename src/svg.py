import sys

from PySide6.QtCore import QObject, Slot, QUrl, Qt
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication


# svg will be loaded in this webEngineView class
class svgViewer(QWebEngineView):
    def __init__(self):
        super(svgViewer, self).__init__()

        # Set up QWebChannel: allows flow between python app and javascript window
        self.channel = QWebChannel()
        self.myObject = MyObject()
        self.channel.registerObject('myObj', self.myObject)
        self.page().setWebChannel(self.channel)

        # load SVG and HTML
        self.load(QUrl.fromLocalFile('C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/board.html'))


# This class is the tool for communicating with python and Javascript
class MyObject(QObject):
    @Slot(str)
    def receiveId(self, element_id):
        print("Clicked on element with ID:", element_id)
        # TODO: Add further processing here


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyObject()
    window.show()
    sys.exit(app.exec())
