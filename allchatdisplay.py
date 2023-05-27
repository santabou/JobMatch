import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from allchat import Ui_Form
from PySide6.QtGui import *
from chat import ChatUI
from goroom import GoCUI
from db import Company,User,Job,Session,engine

local_session=Session(bind=engine)

class AllCUI(QWidget):
    def __init__(self,u,t):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.username=u
        self.userType=t
        self.ui.openroom.clicked.connect(self.open)
        #check user type
        if self.userType=="0":
            self.user = local_session.query(User).filter_by(username=self.username).first()
            if(self.user.chat!=""):
                self.showchatlist(self.user.chat)
        else:
            self.com = local_session.query(Company).filter_by(username=self.username).first()
            if(self.com.chat!=""):
                self.showchatlist(self.com.chat)
    
    def showchatlist(self,data,count=0):
            x=data.split("\n")
            for n in x:
                n2=n.split("&")
                for m in n2:
                    job = local_session.query(Job).filter_by(jobid=n2[0]).first()
                    # Check if the job object exists and retrieve the position
                    if job:
                        if job.position!="":
                            pos=job.position
                    else:
                        pos="Any"
                    if m!=self.username:
                        #create chat list with n=room name m=the person chatting with, pos= position
                        self.createNewWindow(count,n,m,pos)
                count=count+1

    def createNewWindow(self,rowNo,n,n2,pos):
        # Generate unique object names
        framename = "frame_" + str(rowNo)
        chatname = "cnam_" + str(rowNo)
        withname = "wnam_" + str(rowNo)
        posname = "posnam_" + str(rowNo)
        opennam = "chat_" + str(rowNo)

        # Create a QFrame widget
        self.frame = QFrame(self.ui.scrollAreaWidgetContents)
        self.frame.setObjectName(framename)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(500, 100))
        self.frame.setMaximumSize(QSize(500, 100))
        self.frame.setStyleSheet(u"background-color: #4E97D1;")
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
        self.button.setStyleSheet(u"background-color: #4E97D1; color: rgb(255, 255, 255);")

        self.label.setText(QCoreApplication.translate("MainWindow", "Room Name: "+n, None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", "Chat with: "+n2, None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", "Position "+pos, None))
        self.button.setText(QCoreApplication.translate("MainWindow", u"Chat", None))

        # Set object names for each widget
        setattr(self.ui, framename, self.frame)
        setattr(self.ui, chatname, self.label)
        setattr(self.ui, withname, self.label_2)
        setattr(self.ui, posname, self.label_3)
        setattr(self.ui, opennam, self.button)

        # Add widgets to layouts
        self.ui.gridLayout.addWidget(self.frame, rowNo, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.button, 2, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        # Set properties for the buttons
        self.button.setProperty("romna", n)
        # Connect button
        self.button.clicked.connect(self.more)

    def more(self):
        # Get the button that triggered the signal
        button=self.sender()
        # Get the value
        rn=button.property("romna")
        self.openchat(rn)

    def open(self):
        self.openroom()

    def openchat(self,rn):
        self.open=QWidget()
        self.eui=ChatUI(self.username,rn)
        self.eui.show()

    def openroom(self):
        self.open=QWidget()
        self.eui=GoCUI(self.username)
        self.eui.show()


def main():    
    app = QApplication(sys.argv)
    w = AllCUI()
    w.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())