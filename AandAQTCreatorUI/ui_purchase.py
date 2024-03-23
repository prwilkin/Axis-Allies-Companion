# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'purchase.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpinBox, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(201, 150)
        palette = QPalette()
        brush = QBrush(QColor(207, 207, 207, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        Dialog.setPalette(palette)
        self.ipc = QSpinBox(Dialog)
        self.ipc.setObjectName(u"ipc")
        self.ipc.setGeometry(QRect(60, 50, 61, 31))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 161, 31))
        self.horizontalLayoutWidget_13 = QWidget(Dialog)
        self.horizontalLayoutWidget_13.setObjectName(u"horizontalLayoutWidget_13")
        self.horizontalLayoutWidget_13.setGeometry(QRect(10, 110, 181, 33))
        self.horizontalLayout_13 = QHBoxLayout(self.horizontalLayoutWidget_13)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.okButton = QPushButton(self.horizontalLayoutWidget_13)
        self.okButton.setObjectName(u"okButton")
        self.okButton.setFlat(False)

        self.horizontalLayout_13.addWidget(self.okButton)


        self.retranslateUi(Dialog)

        self.okButton.setDefault(True)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Purchase IPC</span></p></body></html>", None))
        self.okButton.setText(QCoreApplication.translate("Dialog", u"Confirm", None))
    # retranslateUi

