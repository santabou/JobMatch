# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginsignup.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(758, 704)
        Form.setStyleSheet(u"background-color: rgb(184, 246, 255)\n"
"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(Form)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setPixmap(QPixmap(u"logo.png"))

        self.verticalLayout.addWidget(self.title)

        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"border-color: rgb(184, 246, 255);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"font: 700 11pt \"Segoe UI\";")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labellog = QLabel(self.tab)
        self.labellog.setObjectName(u"labellog")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setItalic(False)
        self.labellog.setFont(font1)
        self.labellog.setStyleSheet(u"\n"
"font: 700 20pt \"Segoe UI\";")

        self.verticalLayout_2.addWidget(self.labellog)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setItalic(False)
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"\n"
"font: 700 11pt \"Segoe UI\";")

        self.verticalLayout_2.addWidget(self.label_10)

        self.logusername = QLineEdit(self.tab)
        self.logusername.setObjectName(u"logusername")
        self.logusername.setFont(font2)
        self.logusername.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid grey;\n"
"border-radius: 18px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"background: white;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(48,50,62);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(85, 170, 255);\n"
"background-color: white;\n"
"}")

        self.verticalLayout_2.addWidget(self.logusername)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"\n"
"font: 700 11pt \"Segoe UI\";")

        self.verticalLayout_2.addWidget(self.label_3)

        self.logpassword = QLineEdit(self.tab)
        self.logpassword.setObjectName(u"logpassword")
        self.logpassword.setFont(font2)
        self.logpassword.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid grey;\n"
"border-radius: 18px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"background: white;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(48,50,62);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(85, 170, 255);\n"
"background-color: white;\n"
"}")
        self.logpassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.logpassword)

        self.label_17 = QLabel(self.tab)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_17)

        self.userrad = QRadioButton(self.tab)
        self.buttonGroup = QButtonGroup(Form)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.userrad)
        self.userrad.setObjectName(u"userrad")
        self.userrad.setFont(font2)

        self.verticalLayout_2.addWidget(self.userrad)

        self.comrad = QRadioButton(self.tab)
        self.buttonGroup.addButton(self.comrad)
        self.comrad.setObjectName(u"comrad")
        self.comrad.setFont(font2)

        self.verticalLayout_2.addWidget(self.comrad)

        self.verticalSpacer_3 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.logenter = QPushButton(self.tab)
        self.logenter.setObjectName(u"logenter")
        self.logenter.setFont(font2)
        self.logenter.setStyleSheet(u"background-color: #4E97D1;\n"
"color: rgb(255, 255, 255);\n"
"font: 700 11pt \"Segoe UI\";")

        self.verticalLayout_2.addWidget(self.logenter)

        self.gotosign = QPushButton(self.tab)
        self.gotosign.setObjectName(u"gotosign")
        self.gotosign.setFont(font2)
        self.gotosign.setStyleSheet(u"background-color: #4E97D1;\n"
"color: rgb(255, 255, 255);\n"
"font: 700 11pt \"Segoe UI\";")

        self.verticalLayout_2.addWidget(self.gotosign)

        self.gotosigncom = QPushButton(self.tab)
        self.gotosigncom.setObjectName(u"gotosigncom")
        self.gotosigncom.setFont(font2)
        self.gotosigncom.setStyleSheet(u"background-color: #4E97D1;\n"
"color: rgb(255, 255, 255);\n"
"font: 700 11pt \"Segoe UI\";")

        self.verticalLayout_2.addWidget(self.gotosigncom)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.labelsign = QLabel(self.tab_2)
        self.labelsign.setObjectName(u"labelsign")
        self.labelsign.setFont(font1)
        self.labelsign.setStyleSheet(u"\n"
"font: 700 20pt \"Segoe UI\";")

        self.verticalLayout_3.addWidget(self.labelsign)

        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_11)

        self.signusername = QLineEdit(self.tab_2)
        self.signusername.setObjectName(u"signusername")
        self.signusername.setFont(font2)
        self.signusername.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid grey;\n"
"border-radius: 18px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"background: white;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(48,50,62);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(85, 170, 255);\n"
"background-color: white;\n"
"}")

        self.verticalLayout_3.addWidget(self.signusername)

        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_5)

        self.signpassword = QLineEdit(self.tab_2)
        self.signpassword.setObjectName(u"signpassword")
        self.signpassword.setFont(font2)
        self.signpassword.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid grey;\n"
"border-radius: 18px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"background: white;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(48,50,62);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(85, 170, 255);\n"
"background-color: white;\n"
"}")
        self.signpassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.signpassword)

        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_6)

        self.signemail = QLineEdit(self.tab_2)
        self.signemail.setObjectName(u"signemail")
        self.signemail.setFont(font2)
        self.signemail.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid grey;\n"
"border-radius: 18px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"background: white;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(48,50,62);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(85, 170, 255);\n"
"background-color: white;\n"
"}")

        self.verticalLayout_3.addWidget(self.signemail)

        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_9)

        self.signfirst = QLineEdit(self.tab_2)
        self.signfirst.setObjectName(u"signfirst")
        self.signfirst.setFont(font2)
        self.signfirst.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid grey;\n"
"border-radius: 18px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"background: white;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(48,50,62);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(85, 170, 255);\n"
"background-color: white;\n"
"}")

        self.verticalLayout_3.addWidget(self.signfirst)

        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_7)

        self.signlast = QLineEdit(self.tab_2)
        self.signlast.setObjectName(u"signlast")
        self.signlast.setFont(font2)
        self.signlast.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid grey;\n"
"border-radius: 18px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"background: white;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(48,50,62);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(85, 170, 255);\n"
"background-color: white;\n"
"}")

        self.verticalLayout_3.addWidget(self.signlast)

        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_8)

        self.widget = QWidget(self.tab_2)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.signday = QComboBox(self.widget)
        self.signday.addItem("")
        self.signday.addItem("")
        self.signday.addItem("")
        self.signday.addItem("")
        self.signday.addItem("")
        self.signday.addItem("")
        self.signday.addItem("")
        self.signday.addItem("")
        self.signday.addItem("")
        self.signday.addItem("")
        self.signday.addItem("")
        self.signday.addItem("")
        self.signday.addItem("")
        self.signday.addItem("")
        self.signday.addItem("")
        self.signday.addItem("")
        self.signday.addItem("")
        self.signday.addItem("")
        self.signday.addItem("")
        self.signday.addItem("")
        self.signday.addItem("")
        self.signday.addItem("")
        self.signday.addItem("")
        self.signday.addItem("")
        self.signday.addItem("")
        self.signday.addItem("")
        self.signday.addItem("")
        self.signday.addItem("")
        self.signday.addItem("")
        self.signday.addItem("")
        self.signday.addItem("")
        self.signday.setObjectName(u"signday")
        self.signday.setFont(font2)
        self.signday.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 14px;\n"
"    min-width: 5em;\n"
"	background-color: rgb(231, 231, 231);\n"
"}\n"
"\n"
"QComboBox:on {\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border-bottom-right-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"    background: white;\n"
"    border: 1px solid gray;\n"
"    box-shadow: transparent;\n"
"    padding: 4px 4px 4px 4px\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-color: transparent;\n"
"}")

        self.horizontalLayout.addWidget(self.signday)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.signmonth = QComboBox(self.widget)
        self.signmonth.addItem("")
        self.signmonth.addItem("")
        self.signmonth.addItem("")
        self.signmonth.addItem("")
        self.signmonth.addItem("")
        self.signmonth.addItem("")
        self.signmonth.addItem("")
        self.signmonth.addItem("")
        self.signmonth.addItem("")
        self.signmonth.addItem("")
        self.signmonth.addItem("")
        self.signmonth.addItem("")
        self.signmonth.setObjectName(u"signmonth")
        self.signmonth.setFont(font2)
        self.signmonth.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 14px;\n"
"    min-width: 5em;\n"
"	background-color: rgb(231, 231, 231);\n"
"}\n"
"\n"
"QComboBox:on {\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border-bottom-right-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"    background: white;\n"
"    border: 1px solid gray;\n"
"    box-shadow: transparent;\n"
"    padding: 4px 4px 4px 4px\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-color: transparent;\n"
"}")

        self.horizontalLayout.addWidget(self.signmonth)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.signyear = QLineEdit(self.widget)
        self.signyear.setObjectName(u"signyear")
        self.signyear.setFont(font2)
        self.signyear.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid grey;\n"
"border-radius: 18px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"background: white;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(48,50,62);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(85, 170, 255);\n"
"background-color: white;\n"
"}")

        self.horizontalLayout.addWidget(self.signyear)

        self.horizontalSpacer_2 = QSpacerItem(156, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.widget)

        self.signenter = QPushButton(self.tab_2)
        self.signenter.setObjectName(u"signenter")

        self.verticalLayout_3.addWidget(self.signenter)

        self.gotolog = QPushButton(self.tab_2)
        self.gotolog.setObjectName(u"gotolog")

        self.verticalLayout_3.addWidget(self.gotolog)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_4 = QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.labelcom = QLabel(self.tab_3)
        self.labelcom.setObjectName(u"labelcom")
        self.labelcom.setFont(font1)
        self.labelcom.setStyleSheet(u"\n"
"font: 700 20pt \"Segoe UI\";")

        self.verticalLayout_4.addWidget(self.labelcom)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.label_12 = QLabel(self.tab_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_12)

        self.comusername = QLineEdit(self.tab_3)
        self.comusername.setObjectName(u"comusername")
        self.comusername.setFont(font2)
        self.comusername.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid grey;\n"
"border-radius: 18px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"background: white;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(48,50,62);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(85, 170, 255);\n"
"background-color: white;\n"
"}")

        self.verticalLayout_4.addWidget(self.comusername)

        self.label_13 = QLabel(self.tab_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_13)

        self.compassword = QLineEdit(self.tab_3)
        self.compassword.setObjectName(u"compassword")
        self.compassword.setFont(font2)
        self.compassword.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid grey;\n"
"border-radius: 18px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"background: white;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(48,50,62);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(85, 170, 255);\n"
"background-color: white;\n"
"}")
        self.compassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout_4.addWidget(self.compassword)

        self.label_16 = QLabel(self.tab_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_16)

        self.comemail = QLineEdit(self.tab_3)
        self.comemail.setObjectName(u"comemail")
        self.comemail.setFont(font2)
        self.comemail.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid grey;\n"
"border-radius: 18px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"background: white;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(48,50,62);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(85, 170, 255);\n"
"background-color: white;\n"
"}")

        self.verticalLayout_4.addWidget(self.comemail)

        self.label_14 = QLabel(self.tab_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_14)

        self.comname = QLineEdit(self.tab_3)
        self.comname.setObjectName(u"comname")
        self.comname.setFont(font2)
        self.comname.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid grey;\n"
"border-radius: 18px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"background: white;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(48,50,62);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(85, 170, 255);\n"
"background-color: white;\n"
"}")

        self.verticalLayout_4.addWidget(self.comname)

        self.label_15 = QLabel(self.tab_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_15)

        self.comloc = QLineEdit(self.tab_3)
        self.comloc.setObjectName(u"comloc")
        self.comloc.setFont(font2)
        self.comloc.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid grey;\n"
"border-radius: 18px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"background: white;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(48,50,62);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(85, 170, 255);\n"
"background-color: white;\n"
"}")

        self.verticalLayout_4.addWidget(self.comloc)

        self.verticalSpacer = QSpacerItem(20, 47, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.comenter = QPushButton(self.tab_3)
        self.comenter.setObjectName(u"comenter")
        self.comenter.setFont(font2)

        self.verticalLayout_4.addWidget(self.comenter)

        self.gotolog2 = QPushButton(self.tab_3)
        self.gotolog2.setObjectName(u"gotolog2")
        self.gotolog2.setFont(font2)

        self.verticalLayout_4.addWidget(self.gotolog2)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title.setText("")
        self.labellog.setText(QCoreApplication.translate("Form", u"Log-in", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Username", None))
        self.logusername.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Username", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Password", None))
        self.logpassword.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Password", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"What type of user are you?", None))
        self.userrad.setText(QCoreApplication.translate("Form", u"Job Seeker", None))
        self.comrad.setText(QCoreApplication.translate("Form", u"Company", None))
        self.logenter.setText(QCoreApplication.translate("Form", u"Enter", None))
        self.gotosign.setText(QCoreApplication.translate("Form", u"Don't have account? Sign-up here", None))
        self.gotosigncom.setText(QCoreApplication.translate("Form", u"Sign-up for Company", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"log-in", None))
        self.labelsign.setText(QCoreApplication.translate("Form", u"Sign-up", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Username", None))
        self.signusername.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Password", None))
        self.signpassword.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Email address", None))
        self.signemail.setPlaceholderText(QCoreApplication.translate("Form", u"Email Address", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"First name", None))
        self.signfirst.setPlaceholderText(QCoreApplication.translate("Form", u"Firstname", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Last name", None))
        self.signlast.setPlaceholderText(QCoreApplication.translate("Form", u"Lastname", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Date of birth", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Day", None))
        self.signday.setItemText(0, QCoreApplication.translate("Form", u"01", None))
        self.signday.setItemText(1, QCoreApplication.translate("Form", u"02", None))
        self.signday.setItemText(2, QCoreApplication.translate("Form", u"03", None))
        self.signday.setItemText(3, QCoreApplication.translate("Form", u"04", None))
        self.signday.setItemText(4, QCoreApplication.translate("Form", u"05", None))
        self.signday.setItemText(5, QCoreApplication.translate("Form", u"06", None))
        self.signday.setItemText(6, QCoreApplication.translate("Form", u"07", None))
        self.signday.setItemText(7, QCoreApplication.translate("Form", u"08", None))
        self.signday.setItemText(8, QCoreApplication.translate("Form", u"09", None))
        self.signday.setItemText(9, QCoreApplication.translate("Form", u"10", None))
        self.signday.setItemText(10, QCoreApplication.translate("Form", u"11", None))
        self.signday.setItemText(11, QCoreApplication.translate("Form", u"12", None))
        self.signday.setItemText(12, QCoreApplication.translate("Form", u"13", None))
        self.signday.setItemText(13, QCoreApplication.translate("Form", u"14", None))
        self.signday.setItemText(14, QCoreApplication.translate("Form", u"15", None))
        self.signday.setItemText(15, QCoreApplication.translate("Form", u"16", None))
        self.signday.setItemText(16, QCoreApplication.translate("Form", u"17", None))
        self.signday.setItemText(17, QCoreApplication.translate("Form", u"18", None))
        self.signday.setItemText(18, QCoreApplication.translate("Form", u"19", None))
        self.signday.setItemText(19, QCoreApplication.translate("Form", u"20", None))
        self.signday.setItemText(20, QCoreApplication.translate("Form", u"21", None))
        self.signday.setItemText(21, QCoreApplication.translate("Form", u"22", None))
        self.signday.setItemText(22, QCoreApplication.translate("Form", u"23", None))
        self.signday.setItemText(23, QCoreApplication.translate("Form", u"24", None))
        self.signday.setItemText(24, QCoreApplication.translate("Form", u"25", None))
        self.signday.setItemText(25, QCoreApplication.translate("Form", u"26", None))
        self.signday.setItemText(26, QCoreApplication.translate("Form", u"27", None))
        self.signday.setItemText(27, QCoreApplication.translate("Form", u"28", None))
        self.signday.setItemText(28, QCoreApplication.translate("Form", u"29", None))
        self.signday.setItemText(29, QCoreApplication.translate("Form", u"30", None))
        self.signday.setItemText(30, QCoreApplication.translate("Form", u"31", None))

        self.label.setText(QCoreApplication.translate("Form", u"Month", None))
        self.signmonth.setItemText(0, QCoreApplication.translate("Form", u"01", None))
        self.signmonth.setItemText(1, QCoreApplication.translate("Form", u"02", None))
        self.signmonth.setItemText(2, QCoreApplication.translate("Form", u"03", None))
        self.signmonth.setItemText(3, QCoreApplication.translate("Form", u"04", None))
        self.signmonth.setItemText(4, QCoreApplication.translate("Form", u"05", None))
        self.signmonth.setItemText(5, QCoreApplication.translate("Form", u"06", None))
        self.signmonth.setItemText(6, QCoreApplication.translate("Form", u"07", None))
        self.signmonth.setItemText(7, QCoreApplication.translate("Form", u"08", None))
        self.signmonth.setItemText(8, QCoreApplication.translate("Form", u"09", None))
        self.signmonth.setItemText(9, QCoreApplication.translate("Form", u"10", None))
        self.signmonth.setItemText(10, QCoreApplication.translate("Form", u"11", None))
        self.signmonth.setItemText(11, QCoreApplication.translate("Form", u"12", None))

        self.label_2.setText(QCoreApplication.translate("Form", u"Year", None))
        self.signyear.setPlaceholderText(QCoreApplication.translate("Form", u"e.g. 2000", None))
        self.signenter.setText(QCoreApplication.translate("Form", u"Enter", None))
        self.gotolog.setText(QCoreApplication.translate("Form", u"Have account already? Log-in here", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"sign-up", None))
        self.labelcom.setText(QCoreApplication.translate("Form", u"Sign-up", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Username", None))
        self.comusername.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Password", None))
        self.compassword.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Email Address", None))
        self.comemail.setPlaceholderText(QCoreApplication.translate("Form", u"Email Address", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Company Name", None))
        self.comname.setPlaceholderText(QCoreApplication.translate("Form", u"Company Name", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Location", None))
        self.comloc.setPlaceholderText(QCoreApplication.translate("Form", u"City/ Lacation", None))
        self.comenter.setText(QCoreApplication.translate("Form", u"Enter", None))
        self.gotolog2.setText(QCoreApplication.translate("Form", u"Have account already? Log-in here", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"company Sign-up", None))
    # retranslateUi

