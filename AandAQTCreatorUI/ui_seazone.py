# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'seazone.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QPlainTextEdit, QSizePolicy, QWidget)

class Ui_seazone(object):
    def setupUi(self, seazone):
        if not seazone.objectName():
            seazone.setObjectName(u"seazone")
        seazone.resize(320, 176)
        self.buttonBox = QDialogButtonBox(seazone)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 140, 301, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(seazone)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 241, 41))
        self.seazoneNum = QLabel(seazone)
        self.seazoneNum.setObjectName(u"seazoneNum")
        self.seazoneNum.setGeometry(QRect(260, 0, 41, 41))
        self.numInput = QPlainTextEdit(seazone)
        self.numInput.setObjectName(u"numInput")
        self.numInput.setGeometry(QRect(30, 60, 251, 51))

        self.retranslateUi(seazone)
        self.buttonBox.accepted.connect(seazone.accept)
        self.buttonBox.rejected.connect(seazone.reject)

        QMetaObject.connectSlotsByName(seazone)
    # setupUi

    def retranslateUi(self, seazone):
        seazone.setWindowTitle(QCoreApplication.translate("seazone", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("seazone", u"<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">Convoy Losses for Seazone:</span></p></body></html>", None))
        self.seazoneNum.setText(QCoreApplication.translate("seazone", u"<html><head/><body><p><span style=\" font-size:12pt;\">###</span></p></body></html>", None))
    # retranslateUi

