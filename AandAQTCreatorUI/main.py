# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtCore import QRect
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QDialog

from src.svg import svgViewer
# Important:
# You need to run the following command to generate the ui_****.py file
#   pyside6-uic ./AandAQTCreatorUI/mainwindow.ui -o ./AandAQTCreatorUI/ui_mainwindow.py
#   pyside6-uic ./AandAQTCreatorUI/changecountry.ui -o ./AandAQTCreatorUI/ui_changeCountry.py
#   pyside6-uic ./AandAQTCreatorUI/seazone.ui -o ./AandAQTCreatorUI/ui_seazone.py
from ui_mainwindow import Ui_MainWindow
from ui_changeCountry import Ui_changeCountry
from ui_seazone import Ui_seazone


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Axis and Allies 1940 2nd Edition Companion")

        # button init
        self.ui.phaseButton.clicked.connect(self.nextPhase_Click)
        self.ui.menuSave.triggered.connect(self)    # TODO: add save functionality
        self.ui.menuLoad.triggered.connect(self)    # TODO: add load functionality

        # Create and add the web browser to the layout
        self.ui.board = QWidget(self.ui.centralwidget)
        self.ui.board.setObjectName("board")
        self.ui.board.setGeometry(QRect(15, 121, 789, 421))
        self.ui.browser = svgViewer(self.ui)
        self.ui.boardLayout = QVBoxLayout(self.ui.board)
        self.ui.boardLayout.addWidget(self.ui.browser)
        self.ui.board.setLayout(self.ui.boardLayout)

    def nextPhase_Click(self):
        print("Next")
        # TODO: change connection
        self.changeCountryWidget = changeCountryWindow()
        self.changeCountryWidget.show()
        self.changeCountryWidget.territory("South Germany")
        # self.seazoneWidget = seazoneWindow()
        # self.seazoneWidget.show()
        # self.seazoneWidget.seazoneNum(125)


class seazoneWindow(QDialog):
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


class changeCountryWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.open = True
        self.country = ""
        self.changeCountryUI = Ui_changeCountry()
        self.changeCountryUI.setupUi(self)

        # buttons
        self.changeCountryUI.okButton.clicked.connect(self.changeCountry_Ok_Click)
        self.changeCountryUI.cancelButton.clicked.connect(self.changeCountry_Cancel_Click)

    def territory(self, territory):
        self.changeCountryUI.territory.setText(territory)
        self.setWindowTitle(territory)

    def changeCountry_Ok_Click(self):
        if self.changeCountryUI.ussr.isChecked():
            self.country = "ussr"
        elif self.changeCountryUI.ukeur.isChecked():
            self.country = "ukeur"
        elif self.changeCountryUI.ukpac.isChecked():
            self.country = "ukpac"
        elif self.changeCountryUI.anzac.isChecked():
            self.country = "anzac"
        elif self.changeCountryUI.usa.isChecked():
            self.country = "usa"
        elif self.changeCountryUI.china.isChecked():
            self.country = "china"
        elif self.changeCountryUI.fra.isChecked():
            self.country = "fra"
        elif self.changeCountryUI.ger.isChecked():
            self.country = "ger"
        elif self.changeCountryUI.jap.isChecked():
            self.country = "jap"
        elif self.changeCountryUI.ita.isChecked():
            self.country = "ita"
        else:
            return
        # TODO: implement changed country
        self.close()

    def changeCountry_Cancel_Click(self):
        print("Cancel")
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
