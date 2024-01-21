import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide6.QtSvgWidgets import QSvgWidget


class svgWidget(QSvgWidget):
    def __init__(self):
        super().__init__("./Board/Board.svg")
        # self.setGeometry(15, 121, 781, 421)
        self.setFixedSize(781, 421)  # Set the fixed size of the widget
