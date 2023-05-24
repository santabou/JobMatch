# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'jobedit.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(935, 536)
        Form.setStyleSheet(u"background-color: rgb(184, 246, 255);\n"
"font: 700 11pt \"Segoe UI\";")
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 20, 871, 471))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.label_6.setFont(font)

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"background-color: rgb(184, 246, 255);\n"
"font: 700 11pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: rgb(184, 246, 255);\n"
"font: 700 11pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgb(184, 246, 255);\n"
"font: 700 11pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)

        self.reqedit = QTextEdit(self.verticalLayoutWidget)
        self.reqedit.setObjectName(u"reqedit")
        self.reqedit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.reqedit, 7, 1, 1, 1)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(184, 246, 255);\n"
"font: 700 11pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.avaedit = QLineEdit(self.verticalLayoutWidget)
        self.avaedit.setObjectName(u"avaedit")
        self.avaedit.setFont(font)
        self.avaedit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.avaedit, 3, 1, 1, 1)

        self.saledit = QLineEdit(self.verticalLayoutWidget)
        self.saledit.setObjectName(u"saledit")
        self.saledit.setFont(font)
        self.saledit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.saledit, 2, 1, 1, 1)

        self.eduedit = QLineEdit(self.verticalLayoutWidget)
        self.eduedit.setObjectName(u"eduedit")
        self.eduedit.setFont(font)
        self.eduedit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.eduedit, 1, 1, 1, 1)

        self.dateedit = QDateEdit(self.verticalLayoutWidget)
        self.dateedit.setObjectName(u"dateedit")
        self.dateedit.setFont(font)
        self.dateedit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.dateedit, 6, 1, 1, 1)

        self.posedit = QLineEdit(self.verticalLayoutWidget)
        self.posedit.setObjectName(u"posedit")
        self.posedit.setFont(font)
        self.posedit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.posedit, 0, 1, 1, 1)

        self.phoedit = QLineEdit(self.verticalLayoutWidget)
        self.phoedit.setObjectName(u"phoedit")
        self.phoedit.setFont(font)
        self.phoedit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.phoedit, 5, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.savebutton = QPushButton(self.verticalLayoutWidget)
        self.savebutton.setObjectName(u"savebutton")
        self.savebutton.setFont(font)
        self.savebutton.setStyleSheet(u"background-color: #4E97D1;\n"
"color: rgb(255, 255, 255);\n"
"")

        self.verticalLayout.addWidget(self.savebutton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Accept Until", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Seats Avaliable", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Salary", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Education Level", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Description", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Phone Number", None))
        self.label.setText(QCoreApplication.translate("Form", u"Position", None))
        self.savebutton.setText(QCoreApplication.translate("Form", u"Save", None))
    # retranslateUi

