# This Python file uses the following encoding: utf-8
import os
import sys

from PySide6.QtCore import QRect
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QDialog

from src.mainBackend import convoyCountry, nextCountry, saver, loader, parser
from src.svg import svgViewer
from ui_bonus import Ui_Bonus
from ui_changeCountry import Ui_changeCountry
from ui_purchase import Ui_Dialog
# Important:
# You need to run the following command to generate the ui_****.py file
#   pyside6-uic ./AandAQTCreatorUI/mainwindow.ui -o ./AandAQTCreatorUI/ui_mainwindow.py
#   pyside6-uic ./AandAQTCreatorUI/changecountry.ui -o ./AandAQTCreatorUI/ui_changeCountry.py
#   pyside6-uic ./AandAQTCreatorUI/seazone.ui -o ./AandAQTCreatorUI/ui_seazone.py
#   pyside6-uic ./AandAQTCreatorUI/bonus.ui -o ./AandAQTCreatorUI/ui_bonus.py
#   pyside6-uic ./AandAQTCreatorUI/purchase.ui -o ./AandAQTCreatorUI/ui_purchase.py
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
        #self.ui.menuSave.triggered.connect(saver)    # TODO: add save functionality
        #self.ui.menuLoad.triggered.connect(loader)    # TODO: add load functionality

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
        # print("Next")
        import src.header as header
        if header.phase == "Purchase":
            if header.turnNum != 1:
                # process bonus & add income to bank
                from src.bonusCalculator import bonusIncomeCalculator
                bonusIncomeCalculator()
            self.purUI = purchaseWindow()
            self.purUI.exec()
            self.displayIPC()
            header.phase = "Combat"
        elif header.phase == "Combat":
            convoys = convoyCountry(header.countryConvert[header.countryTurn])
            for convoy in convoys:
                self.seazoneWidget = seazoneWindow()
                convoy = convoy.replace("Sea Zone ", "")
                self.seazoneWidget.seazoneNum(convoy)
                self.seazoneWidget.exec()
            header.phase = "Income"
        elif header.phase == "Income":
            # show bonus window
            self.bonusWidget = bonusWindow()
            self.bonusWidget.exec()
            header.countryTurn = nextCountry(header.countryTurn)
            header.phase = "Purchase"
        self.displayItems()
        # self.changeCountryWidget = changeCountryWindow()
        # self.changeCountryWidget.show()
        # self.changeCountryWidget.territory("South Germany")
        # self.seazoneWidget = seazoneWindow()
        # self.seazoneWidget.show()
        # self.seazoneWidget.seazoneNum(125)

    def displayIPC(self):
        import src.header as header
        self.ui.gerBank.setText(str(header.ipcTable["gerBank"]))
        self.ui.gerTurn.setText(str(header.ipcTable["gerTurn"]))
        self.ui.ussrBank.setText(str(header.ipcTable["ussrBank"]))
        self.ui.ussrTurn.setText(str(header.ipcTable["ussrTurn"]))
        self.ui.japBank.setText(str(header.ipcTable["japBank"]))
        self.ui.japTurn.setText(str(header.ipcTable["japTurn"]))
        self.ui.usaBank.setText(str(header.ipcTable["usBank"]))
        self.ui.usaTurn.setText(str(header.ipcTable["usTurn"]))
        self.ui.chinaBank.setText(str(header.ipcTable["chinaBank"]))
        self.ui.chinaTurn.setText(str(header.ipcTable["chinaTurn"]))
        self.ui.ukeurBank.setText(str(header.ipcTable["ukeurBank"]))
        self.ui.ukeurTurn.setText(str(header.ipcTable["ukeurTurn"]))
        self.ui.ukpacBank.setText(str(header.ipcTable["ukpacBank"]))
        self.ui.ukpacTurn.setText(str(header.ipcTable["ukpacTurn"]))
        self.ui.itaBank.setText(str(header.ipcTable["itaBank"]))
        self.ui.itaTurn.setText(str(header.ipcTable["itaTurn"]))
        self.ui.anzacBank.setText(str(header.ipcTable["anzacBank"]))
        self.ui.anzacTurn.setText(str(header.ipcTable["anzacTurn"]))
        self.ui.fraBank.setText(str(header.ipcTable["fraBank"]))
        self.ui.fraTurn.setText(str(header.ipcTable["fraTurn"]))

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

        self.country = ""

        # buttons
        self.seazoneUI.okButton.clicked.connect(self.seazone_Ok_Click)
        self.seazoneUI.cancelButton.clicked.connect(self.seazone_Cancel_Click)

    def seazoneNum(self, num):
        self.seazoneUI.seazoneNum.setText(str(num))
        self.seazoneUI.seazoneNum.setStyleSheet("font-size:12pt")
        self.setWindowTitle("Seazone " + str(num))

    def seazone_Ok_Click(self):
        # print("Seazone")
        import src.header as header
        if self.seazoneUI.ussr.isChecked():
            self.country = "ussr"
        elif self.seazoneUI.ukeur.isChecked():
            self.country = "ukeur"
        elif self.seazoneUI.ukpac.isChecked():
            self.country = "ukpac"
        elif self.seazoneUI.anzac.isChecked():
            self.country = "anzac"
        elif self.seazoneUI.usa.isChecked():
            self.country = "us"
        elif self.seazoneUI.china.isChecked():
            self.country = "china"
        elif self.seazoneUI.fra.isChecked():
            self.country = "fra"
        elif self.seazoneUI.ger.isChecked():
            self.country = "ger"
        elif self.seazoneUI.jap.isChecked():
            self.country = "jap"
        elif self.seazoneUI.ita.isChecked():
            self.country = "ita"
        elif self.seazoneUI.nue.isChecked():
            self.country = "nue"
        else:
            return
        header.ipcTable[self.country + "Bank"] -= self.seazoneUI.convoyLoss.value()
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
        elif self.changeCountryUI.nue.isChecked():
            self.country = "nue"
        else:
            return
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
        # TODO: if checked stay checked

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


class purchaseWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.purUI = Ui_Dialog()
        self.purUI.setupUi(self)
        self.setWindowTitle("Purchase")

        # buttons
        self.purUI.okButton.clicked.connect(self.purchase_Ok_Click)

    def purchase_Ok_Click(self):
        import src.header as header
        print("Close Pur")
        header.ipcTable[header.countryConvert[header.countryTurn] + "Bank"] -= self.purUI.ipc.value()
        self.close()


def start():
    app = QApplication(sys.argv)
    import src.header as header
    header.mainWin = MainWindow()
    header.mainWin.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    start()
