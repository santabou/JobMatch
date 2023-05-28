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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
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
        self.ok = QPushButton(Form)
        self.ok.setObjectName(u"ok")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.ok.setFont(font)
        self.ok.setStyleSheet(u"background-color: #4E97D1;\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.ok, 1, 1, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.comboBox = QLineEdit(Form)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.ok.setText(QCoreApplication.translate("Form", u"OK", None))
        self.label.setText(QCoreApplication.translate("Form", u"Enter Job Application Number", None))
        self.comboBox.setPlaceholderText(QCoreApplication.translate("Form", u"enter number here", None))
    # retranslateUi

