# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtCore import QRect, QUrl
from PySide6.QtSvgWidgets import QGraphicsSvgItem
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGraphicsScene, QGraphicsView, QVBoxLayout

# Important:
# You need to run the following command to generate the ui_****.py file
#   pyside6-uic ./AandAQTCreatorUI/mainwindow.ui -o ./AandAQTCreatorUI/ui_mainwindow.py
#   pyside6-uic ./AandAQTCreatorUI/changecountry.ui -o ./AandAQTCreatorUI/ui_changeCountry.py
#   pyside6-uic ./AandAQTCreatorUI/seazone.ui -o ./AandAQTCreatorUI/ui_seazone.py
from ui_mainwindow import Ui_MainWindow
from ui_seazone import Ui_seazone
from ui_changeCountry import Ui_changeCountry
from src.svggui import SvgInteractiveViewer
from src.svg import MyObject

widgetOpen = False  # TODO
# Enable remote debugging
sys.argv.append('--remote-debugging-port=12345')

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Axis and Allies 1940 2nd Edition Companion")

        # button init
        self.ui.phaseButton.clicked.connect(self.nextPhase_Click)

        # Create and add the web browser to the layout
        self.ui.board = QWidget(self.ui.centralwidget)
        self.ui.board.setObjectName("board")
        self.ui.board.setGeometry(QRect(15, 121, 789, 421))
        self.ui.browser = QWebEngineView()
        self.ui.boardLayout = QVBoxLayout(self.ui.board)
        self.ui.boardLayout.addWidget(self.ui.browser)
        self.ui.board.setLayout(self.ui.boardLayout)

        self.myObj = MyObject()
        channel = QWebChannel()
        channel.registerObject('myObj', self.myObj)
        self.ui.browser.page().setWebChannel(channel)

        self.ui.browser.load(QUrl.fromLocalFile('C:/Users/patri/Documents/GIT Repos/Axis-Allies-Companion/src/board.html'))

    def nextPhase_Click(self):
        print("Next")
        # change connection TODO
        # self.changeCountryWidget = changeCountryWindow()
        # self.changeCountryWidget.show()
        # self.changeCountryWidget.territory("South Germany")
        self.seazoneWidget = seazoneWindow()
        self.seazoneWidget.show()
        self.seazoneWidget.seazoneNum(125)


class seazoneWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.seazoneUI = Ui_seazone()
        self.seazoneUI.setupUi(self)

        # buttons
        self.seazoneUI.okButton.clicked.connect(self.seazone_Ok_Click)
        self.seazoneUI.cancelButton.clicked.connect(self.seazone_Cancel_Click)

    def seazoneNum(self, num):
        self.seazoneUI.seazoneNum.setText(str(num))
        self.setWindowTitle("Seazone " + str(num))

    def seazone_Ok_Click(self):
        # print("Seazone")
        x = int(self.seazoneUI.numInput.toPlainText())
        print(x)
        # pass input to the convoy loss functions for IPC TODO
        self.close()

    def seazone_Cancel_Click(self):
        # print("Cancel")
        self.close()


class changeCountryWindow(QWidget):
    def __init__(self, parent=None):
        if widgetOpen == True:
            self.close()
            return
        super().__init__(parent)
        self.changeCountryUI = Ui_changeCountry()
        self.changeCountryUI.setupUi(self)

        # buttons
        self.changeCountryUI.okButton.clicked.connect(self.changeCountry_Ok_Click)
        self.changeCountryUI.cancelButton.clicked.connect(self.changeCountry_Cancel_Click)

    def territory(self, territory):
        self.changeCountryUI.territory.setText(territory)
        self.setWindowTitle(territory)

    def changeCountry_Ok_Click(self):
        country = ""
        if self.changeCountryUI.ussr.isChecked():
            country = "ussr"
        elif self.changeCountryUI.ukeur.isChecked():
            country = "ukeur"
        elif self.changeCountryUI.ukpac.isChecked():
            country = "ukpac"
        elif self.changeCountryUI.anzac.isChecked():
            country = "anzac"
        elif self.changeCountryUI.usa.isChecked():
            country = "usa"
        elif self.changeCountryUI.china.isChecked():
            country = "china"
        elif self.changeCountryUI.fra.isChecked():
            country = "fra"
        elif self.changeCountryUI.ger.isChecked():
            country = "ger"
        elif self.changeCountryUI.jap.isChecked():
            country = "jap"
        elif self.changeCountryUI.ita.isChecked():
            country = "ita"
        else:
            return
        print(country)
        # implement changed country TODO
        self.close()

    def changeCountry_Cancel_Click(self):
        # print("Cancel")
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
