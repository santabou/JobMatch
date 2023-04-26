# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewprofile.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
        Form.resize(679, 493)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 651, 461))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gdlabel = QLabel(self.gridLayoutWidget)
        self.gdlabel.setObjectName(u"gdlabel")

        self.gridLayout.addWidget(self.gdlabel, 0, 5, 1, 1)

        self.doblabel = QLabel(self.gridLayoutWidget)
        self.doblabel.setObjectName(u"doblabel")

        self.gridLayout.addWidget(self.doblabel, 1, 1, 1, 1)

        self.fnlabel = QLabel(self.gridLayoutWidget)
        self.fnlabel.setObjectName(u"fnlabel")

        self.gridLayout.addWidget(self.fnlabel, 0, 1, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.sklabel = QLabel(self.gridLayoutWidget)
        self.sklabel.setObjectName(u"sklabel")

        self.gridLayout.addWidget(self.sklabel, 6, 4, 1, 1, Qt.AlignTop)

        self.label_17 = QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 6, 3, 1, 1, Qt.AlignTop)

        self.lnlabel = QLabel(self.gridLayoutWidget)
        self.lnlabel.setObjectName(u"lnlabel")

        self.gridLayout.addWidget(self.lnlabel, 0, 3, 1, 1)

        self.eprlabel = QLabel(self.gridLayoutWidget)
        self.eprlabel.setObjectName(u"eprlabel")

        self.gridLayout.addWidget(self.eprlabel, 6, 1, 1, 1, Qt.AlignTop)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.edulabel = QLabel(self.gridLayoutWidget)
        self.edulabel.setObjectName(u"edulabel")

        self.gridLayout.addWidget(self.edulabel, 2, 4, 1, 1, Qt.AlignTop)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)

        self.pnblabel = QLabel(self.gridLayoutWidget)
        self.pnblabel.setObjectName(u"pnblabel")

        self.gridLayout.addWidget(self.pnblabel, 1, 3, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 1, 4, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 2, 0, 1, 1, Qt.AlignTop)

        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 2, 3, 1, 1, Qt.AlignTop)

        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 6, 0, 1, 1, Qt.AlignTop)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)

        self.emlabel = QLabel(self.gridLayoutWidget)
        self.emlabel.setObjectName(u"emlabel")

        self.gridLayout.addWidget(self.emlabel, 1, 5, 1, 1)

        self.poslabel = QLabel(self.gridLayoutWidget)
        self.poslabel.setObjectName(u"poslabel")

        self.gridLayout.addWidget(self.poslabel, 2, 1, 1, 1, Qt.AlignTop)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.gdlabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.doblabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.fnlabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Phone Number :", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Lastname :", None))
        self.sklabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Skills :", None))
        self.lnlabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.eprlabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("Form", u"Firstname :", None))
        self.edulabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Gender :", None))
        self.pnblabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Email :", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Position :", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Education :", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Experience :", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Date Of Birth :", None))
        self.emlabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.poslabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

