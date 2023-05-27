import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from allapp import Ui_Form
from config import firebaseConfig
from PySide6.QtGui import *
import pyrebase
from chat import ChatUI
from viewuserprofile import VUserUI
from db import Company,User,Job,Session,engine

local_session=Session(bind=engine)
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

class AllUI(QWidget):
    def __init__(self,u):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.user=u
        self.showapplist(local_session.query(Job).all())

    def removeAll(self):
        for i in reversed(range(self.ui.gridLayout.count())):
            widget = self.ui.gridLayout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
                self.ui.gridLayout.removeWidget(widget)

    def reloadlist(self):
        self.removeAll()
        self.showapplist(local_session.query(Job).all())

    def showapplist(self,data,count=0):
        for key in data:
            # Check if the current user matches the username
            if(self.user == key.username and key.apply!=""):
                af=key.position
                ap=key.apply
                eachap = ap.split("\n")
                for n in eachap:
                    k=key.jobid
                    # Retrieve user information based on the username
                    user = local_session.query(User).filter_by(username=n).first()
                    name=user.firstname+" "+user.lastname
                    phone=user.phone_number
                    email=user.email
                    self.createNewWindow(count,af,name,phone,email,n,k)
                    count=count+1


    def createNewWindow(self,rowNo,af,name,phone,email,n,key):
        # Generate unique object names
        framename = "frame_" + str(rowNo)
        appname = "appn_" + str(rowNo)
        posnam = "posn_" + str(rowNo)
        phoname = "phon_" + str(rowNo)
        emailname = "eman_" + str(rowNo)
        morenam = "morn_" + str(rowNo)
        accname = "accn_" + str(rowNo)
        denname = "denn_" + str(rowNo)

        # Create a QFrame widget
        self.frame = QFrame(self.ui.scrollAreaWidgetContents)
        self.frame.setObjectName(framename)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(700, 100))
        self.frame.setMaximumSize(QSize(700, 100))
        self.frame.setStyleSheet(u"background-color: #4E97D1;")
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
        self.label_4.setMinimumSize(QSize(200, 20))
        self.label_4.setMaximumSize(QSize(200, 20))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.button = QPushButton(self.frame)
        self.frame.setObjectName(morenam)
        self.button.setObjectName(u"button")
        self.button.setMinimumSize(QSize(200, 20))
        self.button.setMaximumSize(QSize(200, 20))
        self.button.setStyleSheet(u"background-color: #4E97D1; color: rgb(255, 255, 255);")

        self.button2 = QPushButton(self.frame)
        self.frame.setObjectName(accname)
        self.button2.setObjectName(u"button2")
        self.button2.setMinimumSize(QSize(200, 20))
        self.button2.setMaximumSize(QSize(200, 20))
        self.button2.setStyleSheet(u"background-color: #4E97D1; color: rgb(255, 255, 255);")

        self.button3 = QPushButton(self.frame)
        self.frame.setObjectName(denname)
        self.button3.setObjectName(u"button3")
        self.button3.setMinimumSize(QSize(200, 20))
        self.button3.setMaximumSize(QSize(200, 20))
        self.button3.setStyleSheet(u"background-color: #4E97D1; color: rgb(255, 255, 255);")

        self.label.setText(QCoreApplication.translate("MainWindow", "Name: "+name, None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", "Applied for: "+af, None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", "Phone Number: "+phone, None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", "Email address: "+ email, None))
        self.button.setText(QCoreApplication.translate("MainWindow", u"view more", None))
        self.button2.setText(QCoreApplication.translate("MainWindow", u"Accept", None))
        self.button3.setText(QCoreApplication.translate("MainWindow", u"Deny", None))

        # Set object names for each widget
        setattr(self.ui, framename, self.frame)
        setattr(self.ui, appname, self.label)
        setattr(self.ui, posnam, self.label_2)
        setattr(self.ui, phoname, self.label_3)
        setattr(self.ui, emailname, self.label_4)
        setattr(self.ui, morenam, self.button)
        setattr(self.ui, accname, self.button2)
        setattr(self.ui, accname, self.button3)

        # Add widgets to layouts
        self.ui.gridLayout.addWidget(self.frame, rowNo, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.button, 2, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.button2, 1, 2, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.button3, 2, 2, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)
        
        # Set properties for the buttons
        self.button.setProperty("usdes", n)
        self.button2.setProperty("accn", n)
        self.button2.setProperty("jobn", key)
        self.button3.setProperty("accn", n)
        self.button3.setProperty("jobn", key)
        # Connect button
        self.button.clicked.connect(self.more)
        self.button2.clicked.connect(self.accept)
        self.button3.clicked.connect(self.deny)

    def openchat(self,rn):
        self.open=QWidget()
        self.eui=ChatUI(self.user,rn)
        self.eui.show()

    def accept(self):
        # Get the button that triggered the signal
        button=self.sender()
        # Get the value
        cnt=button.property("accn")
        jobt= button.property("jobn")
        # Create message
        message=self.user+": Hello thankyou for applying to our company. We are happy to inform you that you are selected as one of the candidate. Please tell use when you are free to interview\n"
        
        # Create a unique room name for the chat
        rn=str(jobt)+"&"+str(cnt)
        # Create a chat and send the message
        self.create_chat(rn,cnt,jobt,message,self.user)
        # Reload the list
        self.reloadlist()
        # Open the chat
        self.openchat(rn)

    def deny(self):
        # Get the button that triggered the signal
        button=self.sender()
        # Get the value
        cnt=button.property("accn")
        jobt=button.property("jobn")
        # Create message
        message=self.user+": Hello thankyou for applying to our company. We are sorry to inform you that you are NOT selected as one of the candidate. We encourage you to apply next time\n"
        # Create a unique room name for the chat
        rn=str(jobt)+"&"+str(cnt)
        # Create a chat and send the message
        self.create_chat(rn,cnt,jobt,message,self.user)
        # Reload the list
        self.reloadlist()
        # Open the chat
        self.openchat(rn)

    def more(self):
        # Get the button that triggered the signal
        button=self.sender()
        #get the value
        jobd=button.property("usdes")
        self.openviewuser(jobd)

    def openviewuser(self,j):
        self.open=QWidget()
        self.vui=VUserUI(j)
        self.vui.show()
    
    def create_chat(self,rn,cnt,jobt,message,u):
        user = local_session.query(User).filter_by(username=cnt).first()
        com = local_session.query(Company).filter_by(username=u).first()
        job = local_session.query(Job).filter_by(jobid=jobt).first()
        # Check if the chat room already exists
        if(db.child("ms").child(rn).get().val()==None):
                # Create a new chat room and update the message
                data = {
                    "message": message,
                }
                db.child("ms").child(rn).update(data)
                # Update the user's chat list with the new chat room
                if user.chat!= "":
                    c1=user.chat
                    if user:
                        user.chat = c1+"\n"+rn
                        local_session.commit()
                else:
                    if user:
                        user.chat = rn
                        local_session.commit()
                # Update the company's chat list with the new chat room
                if com.chat!= "":
                    c2=com.chat
                    if com:
                        com.chat=c2+"\n"+rn
                        local_session.commit()
                else:
                    if com:
                        com.chat=rn
                        local_session.commit()

                # Update the job's application list by removing the accepted candidate
                ap=job.apply
                repl=cnt+"\n"
                newap=ap.replace(repl,"")
                if(newap==ap):
                    repl="\n"+cnt
                    newap=ap.replace(repl,"")
                if(newap==ap):
                    repl=cnt
                    newap=ap.replace(repl,"")
                data = {
                    "apply": newap
                }
                if job:
                    job.apply=newap
                    local_session.commit()

def main():    
    app = QApplication(sys.argv)
    w = AllUI()
    w.show()

    return app.exec()

if __name__ == "__main__":
    sys.exit(main())