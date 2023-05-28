import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from loginsignup import Ui_Form
from PySide6.QtGui import *
from main import MainUI
from db import User,Company,Session,engine,Base

local_session=Session(bind=engine)

class LoginUI(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        if not engine.dialect.has_table(engine.connect(), 'DATA.db'):
            # Create the table if it doesn't exist
            Base.metadata.create_all(engine)
        self.ui.gotolog.clicked.connect(self.change0)
        self.ui.gotolog2.clicked.connect(self.change0)
        self.ui.gotosign.clicked.connect(self.change1)
        self.ui.gotosigncom.clicked.connect(self.change2)
        self.ui.signenter.clicked.connect(self.signingup)
        self.ui.comenter.clicked.connect(self.signingupcom)
        self.ui.logenter.clicked.connect(self.loggingin)

    def change0(self):
        self.ui.tabWidget.setCurrentIndex(0)
    
    def change1(self):
        self.ui.tabWidget.setCurrentIndex(1)

    def change2(self):
        self.ui.tabWidget.setCurrentIndex(2)


    #signing up for job seeker
    def signingup(self):
        username = self.ui.signusername.text()
        password = self.ui.signpassword.text()
        email = self.ui.signemail.text()
        firstname = self.ui.signfirst.text()
        lastname = self.ui.signlast.text()
        dob = (str(self.ui.signday.currentText())+"/"+str(self.ui.signmonth.currentText())+"/"+str(self.ui.signyear.text()))
        is_com=0
        
        if self.user_exists(username, is_com):
            QMessageBox.information(self, "ERROR", f"Username already exists.")
        elif self.email_exists(email, is_com):
            QMessageBox.information(self, "ERROR", f"Email already exists.")
        else:
            #add_user
            user = User(
                username=username,
                password=password,
                email=email,
                firstname=firstname,
                lastname=lastname,
                dob=dob,
                position="",
                phone_number="",
                skill="",
                gender="",
                experience="",
                education="",
                chat=""
            )
            local_session.add(user)
            local_session.commit()
            QMessageBox.information(self, "Success", f"Account created successfully!")
            self.ui.tabWidget.setCurrentIndex(0)

    #signing up for company
    def signingupcom(self):
        username = self.ui.comusername.text()
        password = self.ui.compassword.text()
        email = self.ui.comemail.text()
        companyname = self.ui.comname.text()
        location = self.ui.comloc.text()
        is_com=1

        if self.user_exists(username, is_com):
            QMessageBox.information(self, "ERROR", f"Username already exists.")
        elif self.email_exists(email, is_com):
            QMessageBox.information(self, "ERROR", f"Email already exists.")
        else:
            #add_company
            company = Company(
                username=username,
                password=password,
                email=email,
                companyname=companyname,
                location=location,
                chat=""
            )
            local_session.add(company)
            local_session.commit()
            QMessageBox.information(self, "Success", f"Account created successfully!")
            self.ui.tabWidget.setCurrentIndex(0)
    
    def loggingin(self):
        username = self.ui.logusername.text()
        password = self.ui.logpassword.text()
        if(self.ui.comrad.isChecked()):
            is_user=1
        elif(self.ui.userrad.isChecked()):
            is_user=0
        else:
             QMessageBox.information(self,"ERROR", f"Please select the radio button.")
            
        
        if self.authenticate(is_user, username, password):
            QMessageBox.information(self,"Success", f"Login successful!")
            self.openmain(username,is_user)
            self.close()
        else:
            QMessageBox.information(self, "ERROR", f"Incorrect username or password.")

    def openmain(self,u,t):
        self.main=QMainWindow()
        self.mui=MainUI(str(u).strip(),str(t).strip())
        self.mui.show()

    def user_exists(self, usn, is_com):
        print(usn)
        if is_com == 1:
            return local_session.query(Company).filter_by(username=usn).first() is not None
        else:
            return local_session.query(User).filter_by(username=usn).first() is not None
        
    def email_exists(self, eml, is_com):
        if is_com == 1:
            return local_session.query(Company).filter_by(email=eml).first() is not None
        else:
            return local_session.query(User).filter_by(email=eml).first() is not None

    def authenticate(self, is_user, usn, pwd):
        if is_user == 1:
            user = local_session.query(Company).filter_by(username=usn).first()
        else:
            user = local_session.query(User).filter_by(username=usn).first()
        return user is not None and user.password == pwd

def main():
    app = QApplication(sys.argv)
    w = LoginUI()
    w.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())