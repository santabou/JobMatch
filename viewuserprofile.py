import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from viewprofile import Ui_Form
from PySide6.QtGui import *
import pyrebase
from config import firebaseConfig


firebase = pyrebase.initialize_app(firebaseConfig)

# Connect to the Firebase Realtime Database
db = firebase.database()
class UserUI(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.fnlabel.setText(db.child("users").child(arg1).child("firstname").get().val())
        self.ui.lnlabel.setText(db.child("users").child(arg1).child("lastname").get().val())
        self.ui.emlabel.setText(db.child("users").child(arg1).child("email").get().val())
        self.ui.doblabel.setText(db.child("users").child(arg1).child("dob").get().val())
        self.ui.gdlabel.setText(db.child("users").child(arg1).child("gender").get().val())
        self.ui.pnblabel.setText(db.child("users").child(arg1).child("phone_number").get().val())
        self.ui.poslabel.setText(db.child("users").child(arg1).child("position").get().val())
        self.ui.edulabel.setText(db.child("users").child(arg1).child("education").get().val())
        self.ui.eprlabel.setText(db.child("users").child(arg1).child("experience").get().val())
        self.ui.sklabel.setText(db.child("users").child(arg1).child("skills").get().val())

def main():    
    app = QApplication(sys.argv)
    w = UserUI()
    w.show()

    return app.exec()

if __name__ == "__main__":
    # arg1 = sys.argv[1]
    arg1= "u1"
    sys.exit(main())