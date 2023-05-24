# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewjob.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(379, 524)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 30, 341, 461))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        font = QFont()
        font.setBold(True)
        self.label_13.setFont(font)

        self.gridLayout.addWidget(self.label_13, 2, 0, 1, 1, Qt.AlignTop)

        self.loclabel = QLabel(self.gridLayoutWidget)
        self.loclabel.setObjectName(u"loclabel")

        self.gridLayout.addWidget(self.loclabel, 6, 1, 1, 1, Qt.AlignTop)

        self.pnblabel = QLabel(self.gridLayoutWidget)
        self.pnblabel.setObjectName(u"pnblabel")

        self.gridLayout.addWidget(self.pnblabel, 8, 1, 1, 1)

        self.edulabel = QLabel(self.gridLayoutWidget)
        self.edulabel.setObjectName(u"edulabel")

        self.gridLayout.addWidget(self.edulabel, 9, 1, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.gridLayout.addWidget(self.label_16, 6, 0, 1, 1, Qt.AlignTop)

        self.seatlabel = QLabel(self.gridLayoutWidget)
        self.seatlabel.setObjectName(u"seatlabel")

        self.gridLayout.addWidget(self.seatlabel, 1, 1, 1, 1)

        self.reqlabel = QLabel(self.gridLayoutWidget)
        self.reqlabel.setObjectName(u"reqlabel")

        self.gridLayout.addWidget(self.reqlabel, 10, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.gridLayout.addWidget(self.label_15, 9, 0, 1, 1)

        self.poslabel = QLabel(self.gridLayoutWidget)
        self.poslabel.setObjectName(u"poslabel")

        self.gridLayout.addWidget(self.poslabel, 7, 1, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.gridLayout.addWidget(self.label_17, 10, 0, 1, 1)

        self.emlabel = QLabel(self.gridLayoutWidget)
        self.emlabel.setObjectName(u"emlabel")

        self.gridLayout.addWidget(self.emlabel, 12, 1, 1, 1)

        self.sallabel = QLabel(self.gridLayoutWidget)
        self.sallabel.setObjectName(u"sallabel")

        self.gridLayout.addWidget(self.sallabel, 11, 1, 1, 1)

        self.avalabel = QLabel(self.gridLayoutWidget)
        self.avalabel.setObjectName(u"avalabel")

        self.gridLayout.addWidget(self.avalabel, 2, 1, 1, 1, Qt.AlignTop)

        self.cnlabel = QLabel(self.gridLayoutWidget)
        self.cnlabel.setObjectName(u"cnlabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cnlabel.sizePolicy().hasHeightForWidth())
        self.cnlabel.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.cnlabel, 0, 1, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 11, 0, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.gridLayout.addWidget(self.label_11, 12, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Avaliable till :", None))
        self.loclabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pnblabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.edulabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Location :", None))
        self.seatlabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.reqlabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Position :", None))
        self.label.setText(QCoreApplication.translate("Form", u"Company Name :", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Phone Number :", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Education :", None))
        self.poslabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Requirements :", None))
        self.emlabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.sallabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.avalabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.cnlabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Seats Left :", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Salary :", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Email :", None))
    # retranslateUi

