# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'useredit.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(834, 538)
        Form.setStyleSheet(u"background-color: rgb(184, 246, 255);\n"
"font: 700 11pt \"Segoe UI\";")
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 11, 791, 521))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.phoneedit = QLineEdit(self.verticalLayoutWidget)
        self.phoneedit.setObjectName(u"phoneedit")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.phoneedit.setFont(font)
        self.phoneedit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.phoneedit, 7, 3, 1, 1)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.firstedit = QLineEdit(self.verticalLayoutWidget)
        self.firstedit.setObjectName(u"firstedit")
        self.firstedit.setFont(font)
        self.firstedit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.firstedit, 0, 3, 1, 1)

        self.emailedit = QLineEdit(self.verticalLayoutWidget)
        self.emailedit.setObjectName(u"emailedit")
        self.emailedit.setFont(font)
        self.emailedit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.emailedit, 8, 3, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.malebutton = QRadioButton(self.verticalLayoutWidget)
        self.malebutton.setObjectName(u"malebutton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.malebutton.sizePolicy().hasHeightForWidth())
        self.malebutton.setSizePolicy(sizePolicy)
        self.malebutton.setFont(font)
        self.malebutton.setStyleSheet(u"background-color: rgb(184, 246, 255)\n"
"")

        self.horizontalLayout_4.addWidget(self.malebutton)

        self.femalebutton = QRadioButton(self.verticalLayoutWidget)
        self.femalebutton.setObjectName(u"femalebutton")
        sizePolicy.setHeightForWidth(self.femalebutton.sizePolicy().hasHeightForWidth())
        self.femalebutton.setSizePolicy(sizePolicy)
        self.femalebutton.setFont(font)
        self.femalebutton.setStyleSheet(u"background-color: rgb(184, 246, 255)\n"
"")

        self.horizontalLayout_4.addWidget(self.femalebutton)

        self.otherbutton = QRadioButton(self.verticalLayoutWidget)
        self.otherbutton.setObjectName(u"otherbutton")
        sizePolicy.setHeightForWidth(self.otherbutton.sizePolicy().hasHeightForWidth())
        self.otherbutton.setSizePolicy(sizePolicy)
        self.otherbutton.setFont(font)
        self.otherbutton.setStyleSheet(u"background-color: rgb(184, 246, 255)\n"
"")

        self.horizontalLayout_4.addWidget(self.otherbutton)


        self.gridLayout.addLayout(self.horizontalLayout_4, 5, 3, 1, 1)

        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout.addWidget(self.label_9, 5, 1, 1, 1)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 7, 1, 1, 1)

        self.skilledit = QTextEdit(self.verticalLayoutWidget)
        self.skilledit.setObjectName(u"skilledit")
        self.skilledit.setFont(font)
        self.skilledit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.skilledit, 16, 3, 1, 1)

        self.dobedit = QDateEdit(self.verticalLayoutWidget)
        self.dobedit.setObjectName(u"dobedit")
        self.dobedit.setFont(font)
        self.dobedit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.dobedit, 3, 3, 1, 1)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout.addWidget(self.label_6, 8, 1, 1, 1)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)

        self.lastedit = QLineEdit(self.verticalLayoutWidget)
        self.lastedit.setObjectName(u"lastedit")
        self.lastedit.setFont(font)
        self.lastedit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.lastedit, 1, 3, 1, 1)

        self.posedit = QLineEdit(self.verticalLayoutWidget)
        self.posedit.setObjectName(u"posedit")
        self.posedit.setFont(font)
        self.posedit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.posedit, 11, 3, 1, 1)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 11, 1, 1, 1)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout.addWidget(self.label_7, 13, 1, 1, 1)

        self.epredit = QTextEdit(self.verticalLayoutWidget)
        self.epredit.setObjectName(u"epredit")
        self.epredit.setFont(font)
        self.epredit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.epredit, 15, 3, 1, 1)

        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.gridLayout.addWidget(self.label_10, 16, 1, 1, 1)

        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout.addWidget(self.label_8, 15, 1, 1, 1)

        self.eduedit = QTextEdit(self.verticalLayoutWidget)
        self.eduedit.setObjectName(u"eduedit")
        self.eduedit.setFont(font)
        self.eduedit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.eduedit, 13, 3, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.updateedit = QPushButton(self.verticalLayoutWidget)
        self.updateedit.setObjectName(u"updateedit")
        self.updateedit.setFont(font)
        self.updateedit.setStyleSheet(u"\n"
"background-color: #4E97D1;\n"
"color: rgb(255, 255, 255);\n"
"")

        self.verticalLayout_3.addWidget(self.updateedit)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Last Name :", None))
        self.malebutton.setText(QCoreApplication.translate("Form", u"Male", None))
        self.femalebutton.setText(QCoreApplication.translate("Form", u"Female", None))
        self.otherbutton.setText(QCoreApplication.translate("Form", u"Prefer not to say", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Gender :", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Phone Number : ", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Email :", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Date Of Birth :", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Position :", None))
        self.label.setText(QCoreApplication.translate("Form", u"First Name :", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Education : ", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Skills : ", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Experience :", None))
        self.updateedit.setText(QCoreApplication.translate("Form", u"Update", None))
    # retranslateUi

