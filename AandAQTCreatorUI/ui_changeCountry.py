# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'changecountry.ui'
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
    QLabel, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_changeCountry(object):
    def setupUi(self, changeCountry):
        if not changeCountry.objectName():
            changeCountry.setObjectName(u"changeCountry")
        changeCountry.resize(320, 409)
        changeCountry.setStyleSheet(u"background: rgb(207, 207, 207)")
        self.buttonBox = QDialogButtonBox(changeCountry)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 370, 301, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(changeCountry)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 301, 31))
        self.verticalLayoutWidget = QWidget(changeCountry)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(70, 40, 160, 332))
        self.buttons = QVBoxLayout(self.verticalLayoutWidget)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setContentsMargins(0, 0, 0, 0)
        self.country = QLabel(self.verticalLayoutWidget)
        self.country.setObjectName(u"country")
        self.country.setAlignment(Qt.AlignCenter)

        self.buttons.addWidget(self.country)

        self.ussr = QRadioButton(self.verticalLayoutWidget)
        self.ussr.setObjectName(u"ussr")

        self.buttons.addWidget(self.ussr)

        self.ukeur = QRadioButton(self.verticalLayoutWidget)
        self.ukeur.setObjectName(u"ukeur")

        self.buttons.addWidget(self.ukeur)

        self.ukpac = QRadioButton(self.verticalLayoutWidget)
        self.ukpac.setObjectName(u"ukpac")

        self.buttons.addWidget(self.ukpac)

        self.anzac = QRadioButton(self.verticalLayoutWidget)
        self.anzac.setObjectName(u"anzac")

        self.buttons.addWidget(self.anzac)

        self.usa = QRadioButton(self.verticalLayoutWidget)
        self.usa.setObjectName(u"usa")

        self.buttons.addWidget(self.usa)

        self.china = QRadioButton(self.verticalLayoutWidget)
        self.china.setObjectName(u"china")

        self.buttons.addWidget(self.china)

        self.fra = QRadioButton(self.verticalLayoutWidget)
        self.fra.setObjectName(u"fra")

        self.buttons.addWidget(self.fra)

        self.ger = QRadioButton(self.verticalLayoutWidget)
        self.ger.setObjectName(u"ger")

        self.buttons.addWidget(self.ger)

        self.jap = QRadioButton(self.verticalLayoutWidget)
        self.jap.setObjectName(u"jap")

        self.buttons.addWidget(self.jap)

        self.ita = QRadioButton(self.verticalLayoutWidget)
        self.ita.setObjectName(u"ita")

        self.buttons.addWidget(self.ita)


        self.retranslateUi(changeCountry)
        self.buttonBox.accepted.connect(changeCountry.accept)
        self.buttonBox.rejected.connect(changeCountry.reject)

        QMetaObject.connectSlotsByName(changeCountry)
    # setupUi

    def retranslateUi(self, changeCountry):
        changeCountry.setWindowTitle(QCoreApplication.translate("changeCountry", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("changeCountry", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">Change Country Ownership</span></p></body></html>", None))
        self.country.setText(QCoreApplication.translate("changeCountry", u"TextLabel", None))
        self.ussr.setText(QCoreApplication.translate("changeCountry", u"USSR", None))
        self.ukeur.setText(QCoreApplication.translate("changeCountry", u"UK-Europe", None))
        self.ukpac.setText(QCoreApplication.translate("changeCountry", u"UK-Pacfic", None))
        self.anzac.setText(QCoreApplication.translate("changeCountry", u"Anzac", None))
        self.usa.setText(QCoreApplication.translate("changeCountry", u"USA", None))
        self.china.setText(QCoreApplication.translate("changeCountry", u"China", None))
        self.fra.setText(QCoreApplication.translate("changeCountry", u"France", None))
        self.ger.setText(QCoreApplication.translate("changeCountry", u"Germany", None))
        self.jap.setText(QCoreApplication.translate("changeCountry", u"Japan", None))
        self.ita.setText(QCoreApplication.translate("changeCountry", u"Italy", None))
    # retranslateUi

