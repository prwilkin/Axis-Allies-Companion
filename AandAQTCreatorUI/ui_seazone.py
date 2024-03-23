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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QRadioButton, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_seazone(object):
    def setupUi(self, seazone):
        if not seazone.objectName():
            seazone.setObjectName(u"seazone")
        seazone.resize(320, 320)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(207, 207, 207, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(231, 231, 231, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(103, 103, 103, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(138, 138, 138, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 127))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Active, QPalette.Accent, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Accent, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush8 = QBrush(QColor(103, 103, 103, 127))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.Accent, brush2)
        seazone.setPalette(palette)
        self.label = QLabel(seazone)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 241, 41))
        self.seazoneNum = QLabel(seazone)
        self.seazoneNum.setObjectName(u"seazoneNum")
        self.seazoneNum.setGeometry(QRect(260, 0, 41, 41))
        self.horizontalLayoutWidget = QWidget(seazone)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(120, 270, 195, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.okButton = QPushButton(self.horizontalLayoutWidget)
        self.okButton.setObjectName(u"okButton")
        self.okButton.setFlat(False)

        self.horizontalLayout.addWidget(self.okButton)

        self.cancelButton = QPushButton(self.horizontalLayoutWidget)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)

        self.convoyLoss = QSpinBox(seazone)
        self.convoyLoss.setObjectName(u"convoyLoss")
        self.convoyLoss.setGeometry(QRect(190, 110, 51, 41))
        self.verticalLayoutWidget = QWidget(seazone)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 40, 101, 271))
        self.buttons = QVBoxLayout(self.verticalLayoutWidget)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setContentsMargins(0, 0, 0, 0)
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

        self.nue = QRadioButton(self.verticalLayoutWidget)
        self.nue.setObjectName(u"nue")

        self.buttons.addWidget(self.nue)

        self.label_2 = QLabel(seazone)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(132, 59, 181, 31))

        self.retranslateUi(seazone)

        self.okButton.setDefault(True)


        QMetaObject.connectSlotsByName(seazone)
    # setupUi

    def retranslateUi(self, seazone):
        seazone.setWindowTitle(QCoreApplication.translate("seazone", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("seazone", u"<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">Convoy Losses for Seazone:</span></p></body></html>", None))
        self.seazoneNum.setText(QCoreApplication.translate("seazone", u"<html><head/><body><p><span style=\" font-size:12pt;\">###</span></p></body></html>", None))
        self.okButton.setText(QCoreApplication.translate("seazone", u"Confirm", None))
        self.cancelButton.setText(QCoreApplication.translate("seazone", u"Cancel", None))
        self.ussr.setText(QCoreApplication.translate("seazone", u"USSR", None))
        self.ukeur.setText(QCoreApplication.translate("seazone", u"UK-Europe", None))
        self.ukpac.setText(QCoreApplication.translate("seazone", u"UK-Pacfic", None))
        self.anzac.setText(QCoreApplication.translate("seazone", u"Anzac", None))
        self.usa.setText(QCoreApplication.translate("seazone", u"USA", None))
        self.china.setText(QCoreApplication.translate("seazone", u"China", None))
        self.fra.setText(QCoreApplication.translate("seazone", u"France", None))
        self.ger.setText(QCoreApplication.translate("seazone", u"Germany", None))
        self.jap.setText(QCoreApplication.translate("seazone", u"Japan", None))
        self.ita.setText(QCoreApplication.translate("seazone", u"Italy", None))
        self.nue.setText(QCoreApplication.translate("seazone", u"Neutral", None))
        self.label_2.setText(QCoreApplication.translate("seazone", u"<html><head/><body><p><span style=\" font-style:italic;\">Roll dice for convoy losses</span></p></body></html>", None))
    # retranslateUi

