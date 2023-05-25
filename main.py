import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from mainpage import Ui_MainWindow
from PySide6.QtGui import *
from db import Company,Job,User,Session,engine
from config import firebaseConfig
import pyrebase
from edituserprofile import UserUI
from gojob import GoUI
from viewjobdetail import VJobUI
from viewuserprofile import VUserUI
from chat import ChatUI
from allappdisplay import AllUI
from allchatdisplay import AllCUI

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
local_session=Session(bind=engine)

class MainUI(QMainWindow):
    def __init__(self,u,t):
        QMainWindow.__init__(self, None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.userType=t
        self.user=u
        if(self.userType=="0"):
            user = local_session.query(User).filter_by(username=self.user).first()
            if user:
                self.ui.usn.setText("Hello, "+user.firstname+" "+user.lastname)
            self.createjoblist(local_session.query(Job).all())
        else:
            com = local_session.query(Company).filter_by(username=self.user).first()
            if com:
                self.ui.usn.setText("Welcome, "+com.companyname)
            self.ui.uppro.setText("Create/Edit Job Application")
            self.ui.vipro.setText("View Applicant")
            self.createuserlist(local_session.query(User).all())

        self.ui.uppro.clicked.connect(self.logging)
        self.ui.gochat.clicked.connect(self.cha)
        self.ui.vipro.clicked.connect(self.view)
        self.ui.clearButton.clicked.connect(self.reloadlist)
        self.ui.searchButton.clicked.connect(self.searching)
        self.ui.log_out.clicked.connect(self.logout)

    def logout(self):
        from logsignpy import LoginUI
        self.log=QWidget()
        self.lui=LoginUI()
        self.lui.show()
        self.close()

    def removeAll(self):
        for i in reversed(range(self.ui.gridLayout.count())):
            widget = self.ui.gridLayout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
                self.ui.gridLayout.removeWidget(widget)

    def searching(self):
        self.removeAll()
        search=self.ui.searchEdit.text()
        if(self.userType=="0"):
            self.createjoblist(local_session.query(Job).all(),search)
        else:
            self.createuserlist(local_session.query(User).all(),search)

    def reloadlist(self):
        self.removeAll()
        self.ui.searchEdit.setText("")
        if(self.userType=="0"):
            self.createjoblist(local_session.query(Job).all())
        else:
            self.createuserlist(local_session.query(User).all())

    def createjoblist(self,data,sear="",count=0):
        for key in data:
            if(sear!=""):
                if(sear.lower() in str(key).lower()):
                    comp=key.comname
                    cnum2=key.jobid
                    pos=key.position
                    sal=key.salary
                    loc=key.location
                    self.createNewWindow(count,comp,pos,sal,loc,cnum2)
            else:
                comp=key.comname
                cnum2=key.jobid
                pos=key.position
                sal=key.salary
                loc=key.location
                self.createNewWindow(count,comp,pos,sal,loc,cnum2)
            count=count+1

    def createuserlist(self,data,sear="",count=0):
        for key in data:
            if(sear!=""):
                if(sear.lower() in str(key).lower()):
                    usn=key.username
                    name=key.firstname+" "+key.lastname
                    phone=key.phone_number
                    email=key.email
                    pos=key.position
                    self.createNewWindow(count,name,phone,email,pos,usn)
            else:
                usn=key.username
                name=key.firstname+" "+key.lastname
                phone=key.phone_number
                email=key.email
                pos=key.position
                self.createNewWindow(count,name,phone,email,pos,usn)
            count=count+1

    def logging(self):
        if(self.userType=="0"):
            self.openedituser()
        else:
            self.openeditjob()

    def openedituser(self):
        self.open=QWidget()
        self.eui=UserUI(self.user)
        self.eui.show()

    def openeditjob(self):
        self.open=QWidget()
        self.eui=GoUI(self.user)
        self.eui.show()
    
    def cha(self):
        self.openallchat()
    
    def openallchat(self):
        self.open=QWidget()
        self.vui=AllCUI(self.user,self.userType)
        self.vui.show()
    
    def view(self):
        if(self.userType=="0"):
            self.openviewuser(self.user)
        else:
            self.openallapp()

    def openallapp(self):
        self.open=QWidget()
        self.oui=AllUI(self.user)
        self.oui.show()

    def createNewWindow(self,rowNo,com,pos,sal,loc,cnum2):

        framename = "frame_" + str(rowNo)
        comnam = "comn_" + str(rowNo)
        posnam = "posn_" + str(rowNo)
        salnam = "saln_" + str(rowNo)
        locnam = "locn_" + str(rowNo)
        morenam = "morn_" + str(rowNo)
        subnam = "subn_" + str(rowNo)

        self.frame = QFrame(self.ui.scrollAreaWidgetContents_4)
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
        self.frame.setObjectName(comnam)
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
        self.frame.setObjectName(salnam)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(200, 20))
        self.label_3.setMaximumSize(QSize(200, 20))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.label_4 = QLabel(self.frame)
        self.frame.setObjectName(locnam)
        self.label_4.setObjectName(u"label_3")
        self.label_4.setMinimumSize(QSize(200, 20))
        self.label_4.setMaximumSize(QSize(200, 20))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.button = QPushButton(self.frame)
        self.frame.setObjectName(morenam)
        self.button.setObjectName(u"button")
        self.button.setMinimumSize(QSize(200, 20))
        self.button.setMaximumSize(QSize(200, 20))
        self.button.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.button2 = QPushButton(self.frame)
        self.frame.setObjectName(subnam)
        self.button2.setObjectName(u"button2")
        self.button2.setMinimumSize(QSize(200, 20))
        self.button2.setMaximumSize(QSize(200, 20))
        self.button2.setStyleSheet(u"color: rgb(255, 255, 255);")

        if(self.userType=="0"):
            self.label.setText(QCoreApplication.translate("MainWindow", "Company: "+com, None))
            self.label_2.setText(QCoreApplication.translate("MainWindow", "Position: "+pos, None))
            self.label_3.setText(QCoreApplication.translate("MainWindow", "Salary: "+sal, None))
            self.label_4.setText(QCoreApplication.translate("MainWindow", "location: "+loc, None))
            self.button.setText(QCoreApplication.translate("MainWindow", u"view more", None))
            self.button2.setText(QCoreApplication.translate("MainWindow", u"submit Application", None))
        else:
            self.label.setText(QCoreApplication.translate("MainWindow", "Name: "+com, None))
            self.label_2.setText(QCoreApplication.translate("MainWindow", "phone Number: "+pos, None))
            self.label_3.setText(QCoreApplication.translate("MainWindow", "Email Address: "+sal, None))
            self.label_4.setText(QCoreApplication.translate("MainWindow", "Position: "+loc, None))
            self.button.setText(QCoreApplication.translate("MainWindow", u"view more", None))
            self.button2.setText(QCoreApplication.translate("MainWindow", u"Contact", None))

        setattr(self.ui, framename, self.frame)
        setattr(self.ui, comnam, self.label)
        setattr(self.ui, posnam, self.label_2)
        setattr(self.ui, salnam, self.label_3)
        setattr(self.ui, locnam, self.label_4)
        setattr(self.ui, morenam, self.button)
        setattr(self.ui, subnam, self.button2)

        self.ui.gridLayout.addWidget(self.frame, rowNo, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.button, 2, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.button2, 2, 2, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.button.setProperty("jobdes", cnum2)
        self.button2.setProperty("jobdes", cnum2)
        self.button.clicked.connect(self.more)
        self.button2.clicked.connect(self.sent)

    def sent(self):
        button=self.sender()
        comp=button.property("jobdes")
        if self.userType=="0":
            checkchat=comp+"&"+self.user
            user = local_session.query(User).filter_by(username=self.user).first()
            ch=user.chat
            if(checkchat in ch):
                QMessageBox.information(self, "ERROR", f"Already Submit")
            else:
                job = local_session.query(Job).filter_by(jobid=comp).first()
                app=job.apply
                if(self.user in app):
                    QMessageBox.information(self, "ERROR", f"Already Submit")
                else:
                    self.add_apply(comp,self.user)
                    QMessageBox.information(self, "SUCCESS", f"Submit Complete")
        else:
            cnt=button.property("jobdes")
            jobt=self.user
            checkchat=jobt+"&"+cnt
            com = local_session.query(Company).filter_by(username=self.user).first()
            ch=com.chat
            if(checkchat in ch):
                QMessageBox.information(self, "ERROR", f"Already Sent")
            else:
                message=self.user+": Hello We are impress by your profile are you willing to interview with us?\n"
                rn=jobt+"&"+cnt
                self.create_chat(rn,cnt,jobt,message)
                self.openchat(rn)

    def openchat(self,rn):
        self.open=QWidget()
        self.eui=ChatUI(self.user,rn)
        self.eui.show()
    
    def more(self):
        button=self.sender()
        jobd=button.property("jobdes")
        if self.userType=="0":
            self.openviewjob(jobd)
        else:
            self.openviewuser(jobd)

    def openviewjob(self,j):
        self.open=QWidget()
        self.vui=VJobUI(j)
        self.vui.show()

    def openviewuser(self,j):
        self.open=QWidget()
        self.vui=VUserUI(j)
        self.vui.show()

    def create_chat(self,rn,cnt,jobt,message):
        user = local_session.query(User).filter_by(username=cnt).first()
        com = local_session.query(Company).filter_by(username=jobt).first()

        if(db.child("ms").child(rn).get().val()==None):
                data = {
                    "message": message,
                }
                db.child("ms").child(rn).update(data)
                if user.chat!= "":
                    c1=user.chat
                    if user:
                        user.chat = c1+"\n"+rn
                        local_session.commit()
                else:
                    if user:
                        user.chat = rn
                        local_session.commit()
                if com.chat!= "":
                    c2=com.chat
                    if com:
                        com.chat=c2+"\n"+rn
                        local_session.commit()
                else:
                    if com:
                        com.chat=rn
                        local_session.commit()

    def add_apply(self,comname,user):
        job = local_session.query(Job).filter_by(jobid=comname).first()
        if job.apply!= "":
            if job:
                j1=job.apply
                job.apply=j1+"\n"+user
                local_session.commit()
        else:
            if job:
                j1=job.apply
                job.apply=user
                local_session.commit()

def main():
    app = QApplication(sys.argv)
    w = MainUI()
    w.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())