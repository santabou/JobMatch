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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(576, 433)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 561, 411))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.firstedit = QLineEdit(self.formLayoutWidget)
        self.firstedit.setObjectName(u"firstedit")
        self.firstedit.setFont(font)

        self.horizontalLayout.addWidget(self.firstedit)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lastedit = QLineEdit(self.formLayoutWidget)
        self.lastedit.setObjectName(u"lastedit")
        self.lastedit.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lastedit)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.dobedit = QLineEdit(self.formLayoutWidget)
        self.dobedit.setObjectName(u"dobedit")
        self.dobedit.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.dobedit)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_4)

        self.posedit = QLineEdit(self.formLayoutWidget)
        self.posedit.setObjectName(u"posedit")
        self.posedit.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.posedit)

        self.updateedit = QPushButton(self.formLayoutWidget)
        self.updateedit.setObjectName(u"updateedit")
        self.updateedit.setFont(font)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.updateedit)

        self.emailedit = QLineEdit(self.formLayoutWidget)
        self.emailedit.setObjectName(u"emailedit")
        self.emailedit.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.emailedit)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.phoneedit = QLineEdit(self.formLayoutWidget)
        self.phoneedit.setObjectName(u"phoneedit")
        self.phoneedit.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.phoneedit)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_6)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"First Name", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Last Name", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"D.O.B.", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Position", None))
        self.updateedit.setText(QCoreApplication.translate("Form", u"Update", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Phone No.", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Email", None))
    # retranslateUi

