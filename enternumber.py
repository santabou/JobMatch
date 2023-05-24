# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'enternumber.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(602, 156)
        Form.setStyleSheet(u"background-color: rgb(184, 246, 255)\n"
"")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        font = QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.ok = QPushButton(Form)
        self.ok.setObjectName(u"ok")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.ok.setFont(font1)
        self.ok.setStyleSheet(u"background-color: #4E97D1;\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.ok, 3, 1, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.label.setFont(font2)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setPointSize(10)
        self.label_2.setFont(font3)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.passline = QLineEdit(Form)
        self.passline.setObjectName(u"passline")
        self.passline.setFont(font)
        self.passline.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.passline, 1, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.ok.setText(QCoreApplication.translate("Form", u"OK", None))
        self.label.setText(QCoreApplication.translate("Form", u"Enter Room Number", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Note: When enter a room number, if it exist, it will enter that room else it will create new", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Password", None))
    # retranslateUi

