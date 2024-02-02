# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bonus.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Bonus(object):
    def setupUi(self, Bonus):
        if not Bonus.objectName():
            Bonus.setObjectName(u"Bonus")
        Bonus.resize(477, 531)
        palette = QPalette()
        brush = QBrush(QColor(207, 207, 207, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        Bonus.setPalette(palette)
        font = QFont()
        font.setPointSize(10)
        Bonus.setFont(font)
        self.label = QLabel(Bonus)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 0, 111, 31))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.label.setFont(font1)
        self.verticalLayoutWidget = QWidget(Bonus)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 30, 453, 450))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.label_2.setFont(font2)

        self.horizontalLayout.addWidget(self.label_2)

        self.ussr_ger_war = QCheckBox(self.verticalLayoutWidget)
        self.ussr_ger_war.setObjectName(u"ussr_ger_war")

        self.horizontalLayout.addWidget(self.ussr_ger_war)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.ussr_jap = QCheckBox(self.verticalLayoutWidget)
        self.ussr_jap.setObjectName(u"ussr_jap")

        self.horizontalLayout_3.addWidget(self.ussr_jap)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.ussr_ita = QCheckBox(self.verticalLayoutWidget)
        self.ussr_ita.setObjectName(u"ussr_ita")

        self.horizontalLayout_2.addWidget(self.ussr_ita)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.uk_jap = QCheckBox(self.verticalLayoutWidget)
        self.uk_jap.setObjectName(u"uk_jap")

        self.horizontalLayout_4.addWidget(self.uk_jap)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.us_jap = QCheckBox(self.verticalLayoutWidget)
        self.us_jap.setObjectName(u"us_jap")

        self.horizontalLayout_5.addWidget(self.us_jap)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.us_ger = QCheckBox(self.verticalLayoutWidget)
        self.us_ger.setObjectName(u"us_ger")

        self.horizontalLayout_6.addWidget(self.us_ger)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.egypt = QCheckBox(self.verticalLayoutWidget)
        self.egypt.setObjectName(u"egypt")

        self.horizontalLayout_7.addWidget(self.egypt)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_14 = QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_14.addWidget(self.label_14)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_7)

        self.checkBox = QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_14.addWidget(self.checkBox)


        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_8.addWidget(self.label_9)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.allyussr = QCheckBox(self.verticalLayoutWidget)
        self.allyussr.setObjectName(u"allyussr")

        self.horizontalLayout_8.addWidget(self.allyussr)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_9.addWidget(self.label_10)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

        self.mediterranean = QCheckBox(self.verticalLayoutWidget)
        self.mediterranean.setObjectName(u"mediterranean")

        self.horizontalLayout_9.addWidget(self.mediterranean)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_10.addWidget(self.label_11)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)

        self.indochina = QCheckBox(self.verticalLayoutWidget)
        self.indochina.setObjectName(u"indochina")

        self.horizontalLayout_10.addWidget(self.indochina)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_12 = QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_11.addWidget(self.label_12)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_5)

        self.unprovoked = QCheckBox(self.verticalLayoutWidget)
        self.unprovoked.setObjectName(u"unprovoked")

        self.horizontalLayout_11.addWidget(self.unprovoked)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_13 = QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_12.addWidget(self.label_13)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_6)

        self.usfra = QCheckBox(self.verticalLayoutWidget)
        self.usfra.setObjectName(u"usfra")

        self.horizontalLayout_12.addWidget(self.usfra)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayoutWidget_13 = QWidget(Bonus)
        self.horizontalLayoutWidget_13.setObjectName(u"horizontalLayoutWidget_13")
        self.horizontalLayoutWidget_13.setGeometry(QRect(270, 490, 195, 33))
        self.horizontalLayout_13 = QHBoxLayout(self.horizontalLayoutWidget_13)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.okButton = QPushButton(self.horizontalLayoutWidget_13)
        self.okButton.setObjectName(u"okButton")
        self.okButton.setFlat(False)

        self.horizontalLayout_13.addWidget(self.okButton)


        self.retranslateUi(Bonus)

        self.okButton.setDefault(True)


        QMetaObject.connectSlotsByName(Bonus)
    # setupUi

    def retranslateUi(self, Bonus):
        Bonus.setWindowTitle(QCoreApplication.translate("Bonus", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Bonus", u"Bonuses", None))
        self.label_2.setText(QCoreApplication.translate("Bonus", u"Soviet Union-Germany:", None))
        self.ussr_ger_war.setText(QCoreApplication.translate("Bonus", u"At War", None))
        self.label_4.setText(QCoreApplication.translate("Bonus", u"Soviet Union-Japan:", None))
        self.ussr_jap.setText(QCoreApplication.translate("Bonus", u"At War", None))
        self.label_3.setText(QCoreApplication.translate("Bonus", u"Soviet Union-Italy:", None))
        self.ussr_ita.setText(QCoreApplication.translate("Bonus", u"At War", None))
        self.label_5.setText(QCoreApplication.translate("Bonus", u"UK/Anzac-Japan:", None))
        self.uk_jap.setText(QCoreApplication.translate("Bonus", u"At War", None))
        self.label_6.setText(QCoreApplication.translate("Bonus", u"US-Japan:", None))
        self.us_jap.setText(QCoreApplication.translate("Bonus", u"At War", None))
        self.label_7.setText(QCoreApplication.translate("Bonus", u"US-Germany:", None))
        self.us_ger.setText(QCoreApplication.translate("Bonus", u"At War", None))
        self.label_8.setText(QCoreApplication.translate("Bonus", u"German land unit(s) in Egypt:", None))
        self.egypt.setText(QCoreApplication.translate("Bonus", u"Yes", None))
        self.label_14.setText(QCoreApplication.translate("Bonus", u"Sea zone 125 has no axis warship:", None))
        self.checkBox.setText(QCoreApplication.translate("Bonus", u"Yes", None))
        self.label_9.setText(QCoreApplication.translate("Bonus", u"Allied unit(s) in original Soviet territories:", None))
        self.allyussr.setText(QCoreApplication.translate("Bonus", u"Yes", None))
        self.label_10.setText(QCoreApplication.translate("Bonus", u"Allied surface warships in the Mediterranean:", None))
        self.mediterranean.setText(QCoreApplication.translate("Bonus", u"Yes", None))
        self.label_11.setText(QCoreApplication.translate("Bonus", u"Japan attack French Indo-China:", None))
        self.indochina.setText(QCoreApplication.translate("Bonus", u"Yes", None))
        self.label_12.setText(QCoreApplication.translate("Bonus", u"Japan unprovoked war against UK/Anzac:", None))
        self.unprovoked.setText(QCoreApplication.translate("Bonus", u"Yes", None))
        self.label_13.setText(QCoreApplication.translate("Bonus", u"US land unit(s) in France:", None))
        self.usfra.setText(QCoreApplication.translate("Bonus", u"Yes", None))
        self.okButton.setText(QCoreApplication.translate("Bonus", u"Confirm", None))
    # retranslateUi

