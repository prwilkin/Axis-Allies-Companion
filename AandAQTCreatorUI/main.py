# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_****.py file
#   pyside6-uic .\AandAQTCreatorUI\mainwindow.ui -o .\AandAQTCreatorUI\ui_mainwindow.py
#   pyside6-uic .\AandAQTCreatorUI\changecountry.ui -o .\AandAQTCreatorUI\ui_changeCountry.py
#   pyside6-uic .\AandAQTCreatorUI\seazone.ui -o .\AandAQTCreatorUI\ui_seazone.py
from ui_mainwindow import Ui_MainWindow
from ui_seazone import Ui_seazone
from ui_changeCountry import Ui_changeCountry


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.seazoneUI = Ui_seazone()
        self.seazoneUI.setupUi(self)

        # button init
        self.ui.phaseButton.clicked.connect(self.nextPhase_Click)

    def nextPhase_Click(self):
        print("Next")

    def changeCountry_Ok_Click(self):
        print("Changed")

    def seazone_Ok_Click(self):
        print("Seazone")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
