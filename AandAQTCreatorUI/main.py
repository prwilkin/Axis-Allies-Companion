# This Python file uses the following encoding: utf-8
import os
import sys

from PySide6.QtCore import QRect
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QDialog

from src.mainBackend import nextCountry, load, parser
from src.header import turnNum, phase, countryTurn, ipcTable
from src.svg import svgViewer
from ui_bonus import Ui_Bonus
from ui_changeCountry import Ui_changeCountry
# Important:
# You need to run the following command to generate the ui_****.py file
#   pyside6-uic ./AandAQTCreatorUI/mainwindow.ui -o ./AandAQTCreatorUI/ui_mainwindow.py
#   pyside6-uic ./AandAQTCreatorUI/changecountry.ui -o ./AandAQTCreatorUI/ui_changeCountry.py
#   pyside6-uic ./AandAQTCreatorUI/seazone.ui -o ./AandAQTCreatorUI/ui_seazone.py
#   pyside6-uic ./AandAQTCreatorUI/bonus.ui -o ./AandAQTCreatorUI/ui_bonus.py
from ui_mainwindow import Ui_MainWindow
from ui_seazone import Ui_seazone


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Axis and Allies 1940 2nd Edition Companion")

        os.chdir("..")
        parser(os.path.abspath(os.curdir) + "/src/NewGame.txt")

        # button init
        self.ui.phaseButton.clicked.connect(self.nextPhase_Click)
        # self.ui.menuSave.triggered.connect()    # TODO: add save functionality
        self.ui.menuLoad.triggered.connect(load())    # TODO: add load functionality

        # Create and add the web browser to the layout
        self.ui.board = QWidget(self.ui.centralwidget)
        self.ui.board.setObjectName("boards")
        self.ui.board.setGeometry(QRect(15, 121, 789, 421))
        self.ui.browser = svgViewer()
        self.ui.boardLayout = QVBoxLayout(self.ui.board)
        self.ui.boardLayout.addWidget(self.ui.browser)
        self.ui.board.setLayout(self.ui.boardLayout)

        os.chdir("./AandAQTCreatorUI")
        self.displayIPC()
        self.displayItems()

    def nextPhase_Click(self):
        print("Next")
        import src.header as header
        if header.phase == "Purchase":
            # process bonus & add income to bank
            from src.bonusCalculator import bonusIncomeCalculator
            bonusIncomeCalculator()
            header.countryTurn = nextCountry(header.countryTurn)
            header.phase = "Combat"
        elif header.phase == "Combat":
            # TODO: check seazone for convoy
            header.phase = "Income"
        elif header.phase == "Income":
            # show bonus window
            self.bonusWidget = bonusWindow()
            self.bonusWidget.show()
            header.phase = "Purchase"
        self.displayItems()
        # self.changeCountryWidget = changeCountryWindow()
        # self.changeCountryWidget.show()
        # self.changeCountryWidget.territory("South Germany")
        # self.seazoneWidget = seazoneWindow()
        # self.seazoneWidget.show()
        # self.seazoneWidget.seazoneNum(125)

    def displayIPC(self):
        self.ui.gerBank.setText(str(ipcTable["gerBank"]))
        self.ui.gerTurn.setText(str(ipcTable["gerTurn"]))
        self.ui.ussrBank.setText(str(ipcTable["ussrBank"]))
        self.ui.ussrTurn.setText(str(ipcTable["ussrTurn"]))
        self.ui.japBank.setText(str(ipcTable["japBank"]))
        self.ui.japTurn.setText(str(ipcTable["japTurn"]))
        self.ui.usaBank.setText(str(ipcTable["usBank"]))
        self.ui.usaTurn.setText(str(ipcTable["usTurn"]))
        self.ui.chinaBank.setText(str(ipcTable["chinaBank"]))
        self.ui.chinaTurn.setText(str(ipcTable["chinaTurn"]))
        self.ui.ukeurBank.setText(str(ipcTable["ukeurBank"]))
        self.ui.ukeurTurn.setText(str(ipcTable["ukeurTurn"]))
        self.ui.ukpacBank.setText(str(ipcTable["ukpacBank"]))
        self.ui.ukpacTurn.setText(str(ipcTable["ukpacTurn"]))
        self.ui.itaBank.setText(str(ipcTable["itaBank"]))
        self.ui.itaTurn.setText(str(ipcTable["itaTurn"]))
        self.ui.anzacBank.setText(str(ipcTable["anzacBank"]))
        self.ui.anzacTurn.setText(str(ipcTable["anzacTurn"]))
        self.ui.fraBank.setText(str(ipcTable["fraBank"]))
        self.ui.fraTurn.setText(str(ipcTable["fraTurn"]))

    def displayItems(self):
        import src.header as header
        self.ui.turnNum.display(header.turnNum)
        self.ui.phase.setText(str(header.phase))
        self.ui.phase.setStyleSheet("qproperty-alignment:AlignCenter; font-size:12pt; font-weight:700")
        self.ui.country.setText(str(header.countryTurn))
        self.ui.country.setStyleSheet("font-size:11pt; font-weight:700")


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
            self.country = "us"
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


class bonusWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.bonusUI = Ui_Bonus()
        self.bonusUI.setupUi(self)
        self.setWindowTitle("Bonuses")

        # buttons
        self.bonusUI.okButton.clicked.connect(self.bonus_Ok_Clicked)

    def bonus_Ok_Clicked(self):
        import src.header as header
        if self.bonusUI.ussr_ger_war.isChecked() and not header.bonusTable["ussr-ger"]:
            header.bonusTable["ussr-ger"] = True
        if self.bonusUI.ussr_jap.isChecked() and not header.bonusTable["ussr-jap"]:
            header.bonusTable["ussr-jap"] = True
        if self.bonusUI.ussr_ita.isChecked() and not header.bonusTable["ussr-ita"]:
            header.bonusTable["ussr-ita"] = True
        if self.bonusUI.uk_jap.isChecked() and not header.bonusTable["uk/anzac-jap"]:
            header.bonusTable["uk/anzac-jap"] = True
        if self.bonusUI.us_jap.isChecked() and not header.bonusTable["us-jap"]:
            header.bonusTable["us-jap"] = True
        if self.bonusUI.us_ger.isChecked() and not header.bonusTable["us-ger"]:
            header.bonusTable["us-ger"] = True
        if self.bonusUI.egypt.isChecked():
            header.bonusTable["egypt"] = True
        else:
            header.bonusTable["egypt"] = False
        if self.bonusUI.seazone125.isChecked():
            header.bonusTable["seazone125"] = True
        else:
            header.bonusTable["seazone125"] = False
        if self.bonusUI.allyussr.isChecked():
            header.bonusTable["allyussr"] = True
        else:
            header.bonusTable["allyussr"] = False
        if self.bonusUI.mediterranean.isChecked():
            header.bonusTable["mediterranean"] = True
        else:
            header.bonusTable["mediterranean"] = False
        if self.bonusUI.indochina.isChecked() and not header.bonusTable["indochina"]:
            header.bonusTable["indochina"] = True
        if self.bonusUI.unprovoked.isChecked() and not header.bonusTable["unprovoked"]:
            header.bonusTable["unprovoked"] = True
        if self.bonusUI.usfra.isChecked() and not header.bonusTable["usfra"]:
            header.bonusTable["usfra"] = True
        self.close()


def start():
    app = QApplication(sys.argv)
    import src.header as header
    header.mainWin = MainWindow()
    header.mainWin.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    start()
