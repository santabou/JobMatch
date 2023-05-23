import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from viewjob import Ui_Form
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
        self.ui.cnlabel.setText(db.child("job").child(arg1).child("companyname").get().val())
        self.ui.reqlabel.setText(db.child("job").child(arg1).child("requirement").get().val())
        self.ui.emlabel.setText(db.child("job").child(arg1).child("email").get().val())
        self.ui.seatlabel.setText(db.child("job").child(arg1).child("avaliable").get().val())
        self.ui.sallabel.setText(db.child("job").child(arg1).child("salary").get().val())
        self.ui.pnblabel.setText(db.child("job").child(arg1).child("phone").get().val())
        self.ui.poslabel.setText(db.child("job").child(arg1).child("position").get().val())
        self.ui.edulabel.setText(db.child("job").child(arg1).child("education").get().val())
        self.ui.loclabel.setText(db.child("job").child(arg1).child("location").get().val())
        self.ui.avalabel.setText(db.child("job").child(arg1).child("due").get().val())

def main():    
    app = QApplication(sys.argv)
    w = UserUI()
    w.show()

    return app.exec()

if __name__ == "__main__":
    arg1 = sys.argv[1]
    # arg1= "c1_1"
    sys.exit(main())