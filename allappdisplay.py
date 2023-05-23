import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from allapp import Ui_Form
from config import firebaseConfig
from PySide6.QtGui import *
import pyrebase
import subprocess

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

class AllUI(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.showapplist(db.child("job").get().val())

    
    def showapplist(self,data,count=0):
        for key in data:
            if(arg1 in key):
                ap=db.child("job").child(key).child("apply").get().val()
                af=db.child("job").child(key).child("position").get().val()
                eachap = ap.split("\n")
                for n in eachap:
                    # print(n)
                    name=db.child("users").child(n).child("firstname").get().val()+" "+db.child("users").child(n).child("lastname").get().val()
                    phone=db.child("users").child(n).child("phone_number").get().val()
                    email=db.child("users").child(n).child("email").get().val()
                    self.createNewWindow(count,af,name,phone,email,n)
                    count=count+1


    def createNewWindow(self,rowNo,af,name,phone,email,n):
        framename = "frame_" + str(rowNo)
        appname = "appn_" + str(rowNo)
        posnam = "posn_" + str(rowNo)
        phoname = "phon_" + str(rowNo)
        emailname = "eman_" + str(rowNo)
        morenam = "morn_" + str(rowNo)
        accname = "accn_" + str(rowNo)
        denname = "denn_" + str(rowNo)

        self.frame = QFrame(self.ui.scrollAreaWidgetContents)
        self.frame.setObjectName(framename)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(500, 100))
        self.frame.setMaximumSize(QSize(500, 100))
        self.frame.setStyleSheet(u"background-color: grey;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.label = QLabel(self.frame)
        self.frame.setObjectName(appname)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(200, 20))
        self.label.setMaximumSize(QSize(200, 20))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.label_2 = QLabel(self.frame)
        self.frame.setObjectName(posnam)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(200, 20))
        self.label_2.setMaximumSize(QSize(200, 20))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.label_3 = QLabel(self.frame)
        self.frame.setObjectName(phoname)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(200, 20))
        self.label_3.setMaximumSize(QSize(200, 20))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.label_4 = QLabel(self.frame)
        self.frame.setObjectName(emailname)
        self.label_4.setObjectName(u"label_3")
        self.label_4.setMinimumSize(QSize(120, 20))
        self.label_4.setMaximumSize(QSize(120, 20))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.button = QPushButton(self.frame)
        self.frame.setObjectName(morenam)
        self.button.setObjectName(u"button")
        self.button.setMinimumSize(QSize(120, 20))
        self.button.setMaximumSize(QSize(120, 20))
        self.button.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.button2 = QPushButton(self.frame)
        self.frame.setObjectName(accname)
        self.button2.setObjectName(u"button2")
        self.button2.setMinimumSize(QSize(120, 20))
        self.button2.setMaximumSize(QSize(120, 20))
        self.button2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.button3 = QPushButton(self.frame)
        self.frame.setObjectName(denname)
        self.button3.setObjectName(u"button3")
        self.button3.setMinimumSize(QSize(120, 20))
        self.button3.setMaximumSize(QSize(120, 20))
        self.button3.setStyleSheet(u"color: rgb(255, 255, 255);")


        # print(com)
        self.label.setText(QCoreApplication.translate("MainWindow", "Name: "+name, None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", "Applied for: "+af, None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", "Phone Number: "+phone, None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", "Email address: "+ email, None))
        self.button.setText(QCoreApplication.translate("MainWindow", u"view more", None))
        self.button2.setText(QCoreApplication.translate("MainWindow", u"Accept", None))
        self.button3.setText(QCoreApplication.translate("MainWindow", u"Deny", None))


        setattr(self.ui, framename, self.frame)
        setattr(self.ui, appname, self.label)
        setattr(self.ui, posnam, self.label_2)
        setattr(self.ui, phoname, self.label_3)
        setattr(self.ui, emailname, self.label_4)
        setattr(self.ui, morenam, self.button)
        setattr(self.ui, accname, self.button2)
        setattr(self.ui, accname, self.button3)

        self.ui.gridLayout.addWidget(self.frame, rowNo, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.button, 2, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.button2, 1, 2, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.button3, 2, 2, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.button.setProperty("usdes", n)
        # self.button2.setProperty("jobdes", cnum2)
        self.button.clicked.connect(self.more)
        # self.button2.clicked.connect(self.sent)

    def more(self):
        button=self.sender()
        jobd=button.property("usdes")
        subprocess.run(['python', 'viewuserprofile.py', jobd])


def main():    
    app = QApplication(sys.argv)
    w = AllUI()
    w.show()

    return app.exec()

if __name__ == "__main__":
    arg1 = sys.argv[1]
    # arg1="c1"
    sys.exit(main())