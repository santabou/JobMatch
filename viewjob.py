# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewJob.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLayout, QSizePolicy, QTextBrowser, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 700)
        font = QFont()
        font.setPointSize(11)
        Form.setFont(font)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"border-color: #4E97D1;\n"
"gridline-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(184, 246, 255)\n"
"\n"
"")
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.loclabel = QLabel(Form)
        self.loclabel.setObjectName(u"loclabel")

        self.gridLayout.addWidget(self.loclabel, 6, 1, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.gridLayout.addWidget(self.label_11, 4, 0, 1, 1)

        self.label_17 = QLabel(Form)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)

        self.gridLayout.addWidget(self.label_17, 18, 0, 1, 1)

        self.label_16 = QLabel(Form)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.gridLayout.addWidget(self.label_16, 6, 0, 1, 1)

        self.cnlabel = QLabel(Form)
        self.cnlabel.setObjectName(u"cnlabel")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cnlabel.sizePolicy().hasHeightForWidth())
        self.cnlabel.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.cnlabel, 0, 1, 1, 1)

        self.label_15 = QLabel(Form)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.gridLayout.addWidget(self.label_15, 5, 0, 1, 1)

        self.emlabel = QLabel(Form)
        self.emlabel.setObjectName(u"emlabel")
        self.emlabel.setStyleSheet(u"gridline-color: rgb(0, 0, 0);")
        self.emlabel.setFrameShape(QFrame.NoFrame)

        self.gridLayout.addWidget(self.emlabel, 4, 1, 1, 1)

        self.pnblabel = QLabel(Form)
        self.pnblabel.setObjectName(u"pnblabel")

        self.gridLayout.addWidget(self.pnblabel, 3, 1, 1, 1)

        self.edulabel = QLabel(Form)
        self.edulabel.setObjectName(u"edulabel")

        self.gridLayout.addWidget(self.edulabel, 5, 1, 1, 1)

        self.poslabel = QLabel(Form)
        self.poslabel.setObjectName(u"poslabel")

        self.gridLayout.addWidget(self.poslabel, 2, 1, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.sallabel = QLabel(Form)
        self.sallabel.setObjectName(u"sallabel")

        self.gridLayout.addWidget(self.sallabel, 1, 1, 1, 1)

        self.reqlabel = QTextBrowser(Form)
        self.reqlabel.setObjectName(u"reqlabel")
        self.reqlabel.setMinimumSize(QSize(0, 0))
        self.reqlabel.setMaximumSize(QSize(16777215, 100))

        self.gridLayout.addWidget(self.reqlabel, 18, 1, 1, 1)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.gridLayout.addWidget(self.label_9, 10, 0, 1, 1)

        self.label_13 = QLabel(Form)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.gridLayout.addWidget(self.label_13, 9, 0, 1, 1)

        self.seatlabel = QLabel(Form)
        self.seatlabel.setObjectName(u"seatlabel")

        self.gridLayout.addWidget(self.seatlabel, 10, 1, 1, 1)

        self.avalabel = QLabel(Form)
        self.avalabel.setObjectName(u"avalabel")

        self.gridLayout.addWidget(self.avalabel, 9, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.loclabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Position :", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Email :", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Requirements :", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Location :", None))
        self.cnlabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Education :", None))
        self.emlabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pnblabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.edulabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.poslabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("Form", u"Company Name :", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Phone Number :", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Salary :", None))
        self.sallabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.reqlabel.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Seats Left :", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Avaliable till :", None))
        self.seatlabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.avalabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

