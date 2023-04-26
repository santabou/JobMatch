import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from useredit import Ui_Form
from PySide6.QtGui import *
import pyrebase
from config import firebaseConfig


firebase = pyrebase.initialize_app(firebaseConfig)

# Connect to the Firebase Realtime Database
db = firebase.database()

def edit_item(username, email, firstname, lastname, dob,pos,pho):
    data = {
        "email": email,
        "firstname": firstname,
        "lastname": lastname,
        "dob": dob,
        "position":pos,
        "phone_number":pho
    }
    # db.child("users").push(data)
    db.child("users").child(username).update(data)
    return True

class UserUI(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.dobedit.setCalendarPopup(True)
        self.ui.dobedit.setDisplayFormat("dd/MM/yyyy")
        date_str = db.child("users").child(arg1).child("dob").get().val()
        date_format = "dd/MM/yyyy"
        date = QDate.fromString(date_str, date_format)
        self.ui.dobedit.setDate(date)

        self.ui.updateedit.clicked.connect(self.update)
        self.ui.firstedit.setText(db.child("users").child(arg1).child("firstname").get().val())
        self.ui.lastedit.setText(db.child("users").child(arg1).child("lastname").get().val())
        self.ui.emailedit.setText(db.child("users").child(arg1).child("email").get().val())
        self.ui.phoneedit.setText(db.child("users").child(arg1).child("phone_number").get().val())
        self.ui.posedit.setText(db.child("users").child(arg1).child("position").get().val())

    def update(self):
        firstname = self.ui.firstedit.text()
        lastname = self.ui.lastedit.text()
        dob = self.ui.dobedit.text()
        email = self.ui.emailedit.text()
        pos= self.ui.posedit.text()
        pho=self.ui.phoneedit.text() 
        username= arg1

        if(edit_item(username, email, firstname, lastname, dob,pos,pho)):
            QMessageBox.information(self,"Success", f"update successful!")
        else:
            QMessageBox.information(self,"ERROR", f"update failed.")


def main():
    app = QApplication(sys.argv)

    w = UserUI()
    w.show()

    return app.exec()

if __name__ == "__main__":
    arg1 = sys.argv[1]
    # arg1= "u1"
    sys.exit(main())