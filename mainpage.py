# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainpage.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QStatusBar, QTabWidget,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"background-color: rgb(184, 246, 255)")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.searchEdit = QLineEdit(self.tab)
        self.searchEdit.setObjectName(u"searchEdit")
        self.searchEdit.setStyleSheet(u"background-color: #white")

        self.gridLayout_2.addWidget(self.searchEdit, 0, 1, 1, 1)

        self.searchButton = QPushButton(self.tab)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setFont(font)
        self.searchButton.setStyleSheet(u"background-color: #4E97D1;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.searchButton, 0, 2, 1, 1)

        self.clearButton = QPushButton(self.tab)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setFont(font)
        self.clearButton.setStyleSheet(u"background-color: #4E97D1;\n"
"color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_2.addWidget(self.clearButton, 0, 3, 1, 1)

        self.scrollArea = QScrollArea(self.tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 748, 430))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_2.addWidget(self.scrollArea, 1, 1, 1, 3)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.usn = QLabel(self.tab_2)
        self.usn.setObjectName(u"usn")
        self.usn.setGeometry(QRect(20, 10, 721, 41))
        font1 = QFont()
        font1.setPointSize(20)
        self.usn.setFont(font1)
        self.usn.setStyleSheet(u"color: #4E97D1;\n"
"\n"
"")
        self.uppro = QPushButton(self.tab_2)
        self.uppro.setObjectName(u"uppro")
        self.uppro.setGeometry(QRect(220, 120, 261, 41))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setKerning(True)
        self.uppro.setFont(font2)
        self.uppro.setStyleSheet(u"background-color: #4E97D1;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.vipro = QPushButton(self.tab_2)
        self.vipro.setObjectName(u"vipro")
        self.vipro.setGeometry(QRect(220, 190, 261, 41))
        self.vipro.setFont(font)
        self.vipro.setStyleSheet(u"background-color: #4E97D1;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.gochat = QPushButton(self.tab_2)
        self.gochat.setObjectName(u"gochat")
        self.gochat.setGeometry(QRect(220, 260, 261, 41))
        self.gochat.setFont(font)
        self.gochat.setStyleSheet(u"background-color: #4E97D1;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.log_out = QPushButton(self.tab_2)
        self.log_out.setObjectName(u"log_out")
        self.log_out.setGeometry(QRect(220, 330, 261, 41))
        self.log_out.setFont(font)
        self.log_out.setStyleSheet(u"background-color: #4E97D1;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.searchEdit.setText("")
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"Clear/Reload", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Home", None))
        self.usn.setText(QCoreApplication.translate("MainWindow", u"Hello", None))
        self.uppro.setText(QCoreApplication.translate("MainWindow", u"Update Profile", None))
        self.vipro.setText(QCoreApplication.translate("MainWindow", u"View Profile", None))
        self.gochat.setText(QCoreApplication.translate("MainWindow", u"Create/Enter Chat Room", None))
        self.log_out.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Setting", None))
    # retranslateUi

