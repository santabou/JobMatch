# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'jobnumber.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(602, 136)
        Form.setStyleSheet(u"background-color: rgb(184, 246, 255)\n"
"")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)

        self.ok = QPushButton(Form)
        self.ok.setObjectName(u"ok")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.ok.setFont(font1)
        self.ok.setStyleSheet(u"background-color: #4E97D1;\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.ok, 2, 1, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.label.setFont(font2)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(False)
        self.comboBox.setFont(font3)
        self.comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Note: One company can only have 3 Job Application", None))
        self.ok.setText(QCoreApplication.translate("Form", u"OK", None))
        self.label.setText(QCoreApplication.translate("Form", u"Enter Job Application Number", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"3", None))

    # retranslateUi

