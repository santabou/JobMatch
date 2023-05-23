import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from allchat import Ui_Form
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
        if(db.child(arg2).child(arg1).child("chat").get().val()!=None):

            self.showchatlist(db.child(arg2).child(arg1).child("chat").get().val())

    
    def showchatlist(self,data,count=0):
            x=data.split("\n")
            for n in x:
                 n2=n.split("&")
                 for m in n2:
                      pos=db.child("job").child(n2[0]).child("position").get().val()
                      if m!=arg1:
                        self.createNewWindow(count,n,m,pos)
                 count=count+1


    def createNewWindow(self,rowNo,n,n2,pos):
        framename = "frame_" + str(rowNo)
        chatname = "cnam_" + str(rowNo)
        withname = "wnam_" + str(rowNo)
        posname = "posnam_" + str(rowNo)
        opennam = "chat_" + str(rowNo)

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
        self.frame.setObjectName(chatname)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(200, 20))
        self.label.setMaximumSize(QSize(200, 20))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.label_2 = QLabel(self.frame)
        self.frame.setObjectName(withname)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(200, 20))
        self.label_2.setMaximumSize(QSize(200, 20))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.label_3 = QLabel(self.frame)
        self.frame.setObjectName(posname)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(200, 20))
        self.label_3.setMaximumSize(QSize(200, 20))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.button = QPushButton(self.frame)
        self.frame.setObjectName(opennam)
        self.button.setObjectName(u"button3")
        self.button.setMinimumSize(QSize(120, 20))
        self.button.setMaximumSize(QSize(120, 20))
        self.button.setStyleSheet(u"color: rgb(255, 255, 255);")


        # print(com)
        self.label.setText(QCoreApplication.translate("MainWindow", "Room Name: "+n, None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", "Chat with: "+n2, None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", "Position "+pos, None))
        self.button.setText(QCoreApplication.translate("MainWindow", u"Chat", None))


        setattr(self.ui, framename, self.frame)
        setattr(self.ui, chatname, self.label)
        setattr(self.ui, withname, self.label_2)
        setattr(self.ui, posname, self.label_3)
        setattr(self.ui, opennam, self.button)

        self.ui.gridLayout.addWidget(self.frame, rowNo, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.button, 2, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.button.setProperty("romna", n)
        self.button.clicked.connect(self.more)

    def more(self):
        button=self.sender()
        rn=button.property("romna")
        subprocess.run(['python', 'chat.py', arg1,rn])


def main():    
    app = QApplication(sys.argv)
    w = AllUI()
    w.show()

    return app.exec()

if __name__ == "__main__":
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    # arg1="u1"
    # arg2="users"
    sys.exit(main())