import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from loginsignup import Ui_Form
from config import firebaseConfig
from PySide6.QtGui import *
import pyrebase
import subprocess


firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

def user_exists(username, is_com):
    if is_com==1:
        user = db.child("companies").child(username).get().val()
    else:
        user = db.child("users").child(username).get().val()
    return (user is not None)

def email_exists(email, is_com):
    if is_com==1:
        for user in db.child("companies").get().each():
            if user.val()["email"] == email:
                return True
    else:
        for user in db.child("users").get().each():
            if user.val()["email"] == email:
                return True
            
    return False
        

def add_user(username, password, email, firstname, lastname, dob):
    data = {
        "password": password,
        "email": email,
        "firstname": firstname,
        "lastname": lastname,
        "dob": dob,
        "position":"",
        "phone_number":""
    }
    db.child("users").child(username).set(data)

def add_com(username, password, email, companyname, location):
    data = {
        "username": username,
        "password": password,
        "email": email,
        "companyname": companyname,
        "location": location
    }
    db.child("companies").child(username).set(data)

def authenticate(is_user, username, password):
    if is_user==1:
        user = db.child("companies").child(username).get().val()
    else:
        user = db.child("users").child(username).get().val()
    return (user is not None and user["password"] == password)

class LoginUI(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

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
    
    def signingup(self):
        username = self.ui.signusername.text()
        password = self.ui.signpassword.text()
        email = self.ui.signemail.text()
        firstname = self.ui.signfirst.text()
        lastname = self.ui.signlast.text()
        dob = (str(self.ui.signday.currentText())+"/"+str(self.ui.signmonth.currentText())+"/"+str(self.ui.signyear.text()))
        is_com=0
        
        if user_exists(username, is_com):
            QMessageBox.information(self, "ERROR", f"Username already exists.")
        elif email_exists(email, is_com):
            QMessageBox.information(self, "ERROR", f"Email already exists.")
        else:
            add_user(username, password,email,firstname,lastname,dob)
            QMessageBox.information(self,"Success", f"Account created successfully!")

    def signingupcom(self):
        username = self.ui.comusername.text()
        password = self.ui.compassword.text()
        email = self.ui.comemail.text()
        companyname = self.ui.comname.text()
        location = self.ui.comloc.text()
        is_com=1

        if user_exists(username, is_com):
            QMessageBox.information(self, "ERROR", f"Username already exists.")
        elif email_exists(email, is_com):
            QMessageBox.information(self, "ERROR", f"Email already exists.")
        else:
            add_com(username, password,email,companyname,location)
            QMessageBox.information(self,"Success", f"Account created successfully!")
    
    def loggingin(self):
        username = self.ui.logusername.text()
        password = self.ui.logpassword.text()
        if(self.ui.comrad.isChecked()):
            is_user=1
        elif(self.ui.userrad.isChecked()):
            is_user=0
        else:
             QMessageBox.information(self,"ERROR", f"Please select the radio button.")
            
        
        if authenticate(is_user, username, password):
            QMessageBox.information(self,"Success", f"Login successful!")
            self.close()
            print(username, "and", is_user)
        else:
            QMessageBox.information(self, "ERROR", f"Incorrect username or password.")

def main():
    app = QApplication(sys.argv)

    w = LoginUI()
    w.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())