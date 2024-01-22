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

        self.page().loadFinished.connect(self.onLoadFinished)

    # Hide scrollbars by injecting CSS
    def onLoadFinished(self):
        css = "body { overflow: hidden; }"
        script = f"var style = document.createElement('style'); style.type = 'text/css'; style.appendChild(document.createTextNode('{css}')); document.head.appendChild(style);"
        self.page().runJavaScript(script)

    # allow zoom with scroll wheel
    def wheelEvent(self, event):
        modifiers = QApplication.keyboardModifiers()
        if modifiers == Qt.ControlModifier:
            zoomInFactor = 1.1
            zoomOutFactor = 1 / zoomInFactor

            # Zoom in or out
            if event.angleDelta().y() > 0:
                self.setZoomFactor(self.zoomFactor() * zoomInFactor)
            else:
                self.setZoomFactor(self.zoomFactor() * zoomOutFactor)
            event.accept()  # Indicate that the event was handled
        else:
            super(svgViewer, self).wheelEvent(event)


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
