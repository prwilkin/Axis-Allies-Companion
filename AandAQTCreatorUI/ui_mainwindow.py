# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGraphicsView, QHBoxLayout,
    QLCDNumber, QLabel, QLayout, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 602)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
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
        self.centralwidget.setPalette(palette)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayoutWidget_11 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_11.setObjectName(u"verticalLayoutWidget_11")
        self.verticalLayoutWidget_11.setGeometry(QRect(550, 10, 141, 91))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.verticalLayoutWidget_11)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.RichText)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.turnNum = QLCDNumber(self.verticalLayoutWidget_11)
        self.turnNum.setObjectName(u"turnNum")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.turnNum)


        self.verticalLayout.addLayout(self.formLayout)

        self.phase = QLabel(self.verticalLayoutWidget_11)
        self.phase.setObjectName(u"phase")

        self.verticalLayout.addWidget(self.phase)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 10, 531, 91))
        self.ipc = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.ipc.setObjectName(u"ipc")
        self.ipc.setContentsMargins(0, 0, 0, 0)
        self.gerIPC = QVBoxLayout()
        self.gerIPC.setObjectName(u"gerIPC")
        self.gerTurn = QLabel(self.horizontalLayoutWidget_2)
        self.gerTurn.setObjectName(u"gerTurn")
        self.gerTurn.setAlignment(Qt.AlignCenter)

        self.gerIPC.addWidget(self.gerTurn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gerIPC.addItem(self.verticalSpacer_2)

        self.gerBank = QLabel(self.horizontalLayoutWidget_2)
        self.gerBank.setObjectName(u"gerBank")
        self.gerBank.setAlignment(Qt.AlignCenter)

        self.gerIPC.addWidget(self.gerBank)


        self.ipc.addLayout(self.gerIPC)

        self.ussrIPC = QVBoxLayout()
        self.ussrIPC.setObjectName(u"ussrIPC")
        self.ussrTurn = QLabel(self.horizontalLayoutWidget_2)
        self.ussrTurn.setObjectName(u"ussrTurn")
        self.ussrTurn.setAlignment(Qt.AlignCenter)

        self.ussrIPC.addWidget(self.ussrTurn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.ussrIPC.addItem(self.verticalSpacer)

        self.ussrBank = QLabel(self.horizontalLayoutWidget_2)
        self.ussrBank.setObjectName(u"ussrBank")
        self.ussrBank.setAlignment(Qt.AlignCenter)

        self.ussrIPC.addWidget(self.ussrBank)


        self.ipc.addLayout(self.ussrIPC)

        self.japIPC = QVBoxLayout()
        self.japIPC.setObjectName(u"japIPC")
        self.japTurn = QLabel(self.horizontalLayoutWidget_2)
        self.japTurn.setObjectName(u"japTurn")
        self.japTurn.setAlignment(Qt.AlignCenter)

        self.japIPC.addWidget(self.japTurn)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.japIPC.addItem(self.verticalSpacer_3)

        self.japBank = QLabel(self.horizontalLayoutWidget_2)
        self.japBank.setObjectName(u"japBank")
        self.japBank.setAlignment(Qt.AlignCenter)

        self.japIPC.addWidget(self.japBank)


        self.ipc.addLayout(self.japIPC)

        self.usaIPC = QVBoxLayout()
        self.usaIPC.setObjectName(u"usaIPC")
        self.usaTurn = QLabel(self.horizontalLayoutWidget_2)
        self.usaTurn.setObjectName(u"usaTurn")
        self.usaTurn.setAlignment(Qt.AlignCenter)

        self.usaIPC.addWidget(self.usaTurn)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.usaIPC.addItem(self.verticalSpacer_4)

        self.usaBank = QLabel(self.horizontalLayoutWidget_2)
        self.usaBank.setObjectName(u"usaBank")
        self.usaBank.setAlignment(Qt.AlignCenter)

        self.usaIPC.addWidget(self.usaBank)


        self.ipc.addLayout(self.usaIPC)

        self.chinaIPC = QVBoxLayout()
        self.chinaIPC.setObjectName(u"chinaIPC")
        self.chinaTurn = QLabel(self.horizontalLayoutWidget_2)
        self.chinaTurn.setObjectName(u"chinaTurn")
        self.chinaTurn.setAlignment(Qt.AlignCenter)

        self.chinaIPC.addWidget(self.chinaTurn)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.chinaIPC.addItem(self.verticalSpacer_5)

        self.chinaBank = QLabel(self.horizontalLayoutWidget_2)
        self.chinaBank.setObjectName(u"chinaBank")
        self.chinaBank.setAlignment(Qt.AlignCenter)

        self.chinaIPC.addWidget(self.chinaBank)


        self.ipc.addLayout(self.chinaIPC)

        self.ukeurIPC = QVBoxLayout()
        self.ukeurIPC.setObjectName(u"ukeurIPC")
        self.ukeurTurn = QLabel(self.horizontalLayoutWidget_2)
        self.ukeurTurn.setObjectName(u"ukeurTurn")
        self.ukeurTurn.setAlignment(Qt.AlignCenter)

        self.ukeurIPC.addWidget(self.ukeurTurn)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.ukeurIPC.addItem(self.verticalSpacer_6)

        self.ukeurBank = QLabel(self.horizontalLayoutWidget_2)
        self.ukeurBank.setObjectName(u"ukeurBank")
        self.ukeurBank.setAlignment(Qt.AlignCenter)

        self.ukeurIPC.addWidget(self.ukeurBank)


        self.ipc.addLayout(self.ukeurIPC)

        self.ukpacIPC = QVBoxLayout()
        self.ukpacIPC.setObjectName(u"ukpacIPC")
        self.ukpacTurn = QLabel(self.horizontalLayoutWidget_2)
        self.ukpacTurn.setObjectName(u"ukpacTurn")
        self.ukpacTurn.setAlignment(Qt.AlignCenter)

        self.ukpacIPC.addWidget(self.ukpacTurn)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.ukpacIPC.addItem(self.verticalSpacer_7)

        self.ukpacBank = QLabel(self.horizontalLayoutWidget_2)
        self.ukpacBank.setObjectName(u"ukpacBank")
        self.ukpacBank.setAlignment(Qt.AlignCenter)

        self.ukpacIPC.addWidget(self.ukpacBank)


        self.ipc.addLayout(self.ukpacIPC)

        self.itaIPC = QVBoxLayout()
        self.itaIPC.setObjectName(u"itaIPC")
        self.itaTurn = QLabel(self.horizontalLayoutWidget_2)
        self.itaTurn.setObjectName(u"itaTurn")
        self.itaTurn.setAlignment(Qt.AlignCenter)

        self.itaIPC.addWidget(self.itaTurn)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.itaIPC.addItem(self.verticalSpacer_8)

        self.itaBank = QLabel(self.horizontalLayoutWidget_2)
        self.itaBank.setObjectName(u"itaBank")
        self.itaBank.setAlignment(Qt.AlignCenter)

        self.itaIPC.addWidget(self.itaBank)


        self.ipc.addLayout(self.itaIPC)

        self.anzacIPC = QVBoxLayout()
        self.anzacIPC.setObjectName(u"anzacIPC")
        self.anzacTurn = QLabel(self.horizontalLayoutWidget_2)
        self.anzacTurn.setObjectName(u"anzacTurn")
        self.anzacTurn.setTextFormat(Qt.AutoText)
        self.anzacTurn.setAlignment(Qt.AlignCenter)

        self.anzacIPC.addWidget(self.anzacTurn)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.anzacIPC.addItem(self.verticalSpacer_9)

        self.anzacBank = QLabel(self.horizontalLayoutWidget_2)
        self.anzacBank.setObjectName(u"anzacBank")
        self.anzacBank.setTextFormat(Qt.AutoText)
        self.anzacBank.setAlignment(Qt.AlignCenter)

        self.anzacIPC.addWidget(self.anzacBank)


        self.ipc.addLayout(self.anzacIPC)

        self.fraIPC = QVBoxLayout()
        self.fraIPC.setObjectName(u"fraIPC")
        self.fraTurn = QLabel(self.horizontalLayoutWidget_2)
        self.fraTurn.setObjectName(u"fraTurn")
        self.fraTurn.setAlignment(Qt.AlignCenter)

        self.fraIPC.addWidget(self.fraTurn)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.fraIPC.addItem(self.verticalSpacer_10)

        self.fraBank = QLabel(self.horizontalLayoutWidget_2)
        self.fraBank.setObjectName(u"fraBank")
        self.fraBank.setAlignment(Qt.AlignCenter)

        self.fraIPC.addWidget(self.fraBank)


        self.ipc.addLayout(self.fraIPC)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 30, 531, 45))
        self.countryIcons = QHBoxLayout(self.horizontalLayoutWidget)
        self.countryIcons.setObjectName(u"countryIcons")
        self.countryIcons.setSizeConstraint(QLayout.SetMaximumSize)
        self.countryIcons.setContentsMargins(0, 0, 0, 0)
        self.ger = QLabel(self.horizontalLayoutWidget)
        self.ger.setObjectName(u"ger")
        self.ger.setPixmap(QPixmap(u"../icons/germany.png"))

        self.countryIcons.addWidget(self.ger)

        self.ussr = QLabel(self.horizontalLayoutWidget)
        self.ussr.setObjectName(u"ussr")
        self.ussr.setTextFormat(Qt.RichText)
        self.ussr.setPixmap(QPixmap(u"../icons/ussr.png"))

        self.countryIcons.addWidget(self.ussr)

        self.jap = QLabel(self.horizontalLayoutWidget)
        self.jap.setObjectName(u"jap")
        self.jap.setPixmap(QPixmap(u"../icons/japan.png"))

        self.countryIcons.addWidget(self.jap)

        self.usa = QLabel(self.horizontalLayoutWidget)
        self.usa.setObjectName(u"usa")
        self.usa.setPixmap(QPixmap(u"../icons/usa.png"))

        self.countryIcons.addWidget(self.usa)

        self.china = QLabel(self.horizontalLayoutWidget)
        self.china.setObjectName(u"china")
        self.china.setPixmap(QPixmap(u"../icons/china.png"))

        self.countryIcons.addWidget(self.china)

        self.ukeur = QLabel(self.horizontalLayoutWidget)
        self.ukeur.setObjectName(u"ukeur")
        self.ukeur.setPixmap(QPixmap(u"../icons/ukeur.png"))

        self.countryIcons.addWidget(self.ukeur)

        self.ukpac = QLabel(self.horizontalLayoutWidget)
        self.ukpac.setObjectName(u"ukpac")
        self.ukpac.setPixmap(QPixmap(u"../icons/ukpac.png"))

        self.countryIcons.addWidget(self.ukpac)

        self.ita = QLabel(self.horizontalLayoutWidget)
        self.ita.setObjectName(u"ita")
        self.ita.setPixmap(QPixmap(u"../icons/italy.png"))

        self.countryIcons.addWidget(self.ita)

        self.anzac = QLabel(self.horizontalLayoutWidget)
        self.anzac.setObjectName(u"anzac")
        self.anzac.setPixmap(QPixmap(u"../icons/anzac.png"))

        self.countryIcons.addWidget(self.anzac)

        self.fra = QLabel(self.horizontalLayoutWidget)
        self.fra.setObjectName(u"fra")
        self.fra.setPixmap(QPixmap(u"../icons/france.png"))

        self.countryIcons.addWidget(self.fra)

        self.anzac.raise_()
        self.ita.raise_()
        self.ussr.raise_()
        self.fra.raise_()
        self.ukeur.raise_()
        self.ger.raise_()
        self.china.raise_()
        self.jap.raise_()
        self.usa.raise_()
        self.ukpac.raise_()
        self.board = QGraphicsView(self.centralwidget)
        self.board.setObjectName(u"board")
        self.board.setGeometry(QRect(15, 121, 781, 421))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(700, 10, 95, 96))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.country = QLabel(self.verticalLayoutWidget)
        self.country.setObjectName(u"country")

        self.verticalLayout_2.addWidget(self.country)

        self.phaseButton = QPushButton(self.verticalLayoutWidget)
        self.phaseButton.setObjectName(u"phaseButton")
        self.phaseButton.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.phaseButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        self.menuSave = QMenu(self.menubar)
        self.menuSave.setObjectName(u"menuSave")
        self.menuLoad = QMenu(self.menubar)
        self.menuLoad.setObjectName(u"menuLoad")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSave.menuAction())
        self.menubar.addAction(self.menuLoad.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">Turn:</span></p></body></html>", None))
        self.phase.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Combat Phase</span></p></body></html>", None))
        self.gerTurn.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">###</span></p></body></html>", None))
        self.gerBank.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">###</span></p></body></html>", None))
        self.ussrTurn.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">###</span></p></body></html>", None))
        self.ussrBank.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">###</span></p></body></html>", None))
        self.japTurn.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">###</span></p></body></html>", None))
        self.japBank.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">###</span></p></body></html>", None))
        self.usaTurn.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">###</span></p></body></html>", None))
        self.usaBank.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">###</span></p></body></html>", None))
        self.chinaTurn.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">###</span></p></body></html>", None))
        self.chinaBank.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">###</span></p></body></html>", None))
        self.ukeurTurn.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">###</span></p></body></html>", None))
        self.ukeurBank.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">###</span></p></body></html>", None))
        self.ukpacTurn.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">###</span></p></body></html>", None))
        self.ukpacBank.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">###</span></p></body></html>", None))
        self.itaTurn.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">###</span></p></body></html>", None))
        self.itaBank.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">###</span></p></body></html>", None))
        self.anzacTurn.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">###</span></p></body></html>", None))
        self.anzacBank.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">###</span></p></body></html>", None))
        self.fraTurn.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">###</span></p></body></html>", None))
        self.fraBank.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">###</span></p></body></html>", None))
        self.ger.setText("")
        self.ussr.setText("")
        self.jap.setText("")
        self.usa.setText("")
        self.china.setText("")
        self.ukeur.setText("")
        self.ukpac.setText("")
        self.ita.setText("")
        self.anzac.setText("")
        self.fra.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">Country:</span></p></body></html>", None))
        self.country.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">UK-Pac</span></p></body></html>", None))
        self.phaseButton.setText(QCoreApplication.translate("MainWindow", u"Next Phase", None))
        self.menuSave.setTitle(QCoreApplication.translate("MainWindow", u"Save", None))
        self.menuLoad.setTitle(QCoreApplication.translate("MainWindow", u"Load", None))
    # retranslateUi

