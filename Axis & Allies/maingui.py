import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class GameUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Set the main window's properties
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Sample Game UI')

        # Turn order and IPC Income labels and placeholders
        self.turn_order_label = QLabel('Turn Order', self)
        self.turn_order_label.move(10, 10)

        self.turn_number_label = QLabel('Turn: ##', self)
        self.turn_number_label.move(100, 10)

        self.ipc_income_label = QLabel('IPC Income:', self)
        self.ipc_income_label.move(200, 10)

        self.ipc_bank_label = QLabel('IPC Bank:', self)
        self.ipc_bank_label.move(300, 10)

        # Grey circles for images
        for i in range(10):
            label = QLabel(self)
            pixmap = QPixmap(10, 10)  # You would replace this with your actual image
            pixmap.fill(Qt.gray)
            label.setPixmap(pixmap)
            label.move(10 + i*15, 50)

        # Phases
        self.phases_label = QLabel('Phases:\nPurchase\nCombat\nNon-combat\nIncome', self)
        self.phases_label.move(10, 100)

        # Green square (SVG Widget Placeholder)
        self.green_square = QWidget(self)
        # self.green_square.setStyleSheet("QWidget { background-color: %s }" % Qt.green.name())
        self.green_square.setGeometry(150, 100, 100, 100)

        # Next Phase button
        self.next_phase_button = QPushButton('Next Phase', self)
        self.next_phase_button.move(10, 250)
        self.next_phase_button.clicked.connect(self.next_phase)

    def next_phase(self):
        # Function to be called when 'Next Phase' is clicked
        print("Next Phase button clicked")

def main():
    app = QApplication(sys.argv)
    ex = GameUI()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
