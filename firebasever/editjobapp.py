import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from jobedit import Ui_Form
from PySide6.QtGui import *
import pyrebase
from config import firebaseConfig


firebase = pyrebase.initialize_app(firebaseConfig)

# Connect to the Firebase Realtime Database
db = firebase.database()

def edit_item(pos,edu,sal,ava,pho,due,req):
    data = {
        "position": pos,
        "education": edu,
        "salary": sal,
        "avaliable": ava,
        "phone": pho,
        "due":due,
        "requirement":req,
        "username":comname,
        "companyname":db.child("companies").child(comname).child("companyname").get().val(),
        "email":db.child("companies").child(comname).child("email").get().val(),
        "location":db.child("companies").child(comname).child("location").get().val()
    }
    db.child("job").child(ind).update(data)
    return True

class JobUI(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.dateedit.setCalendarPopup(True)
        self.ui.dateedit.setDisplayFormat("dd/MM/yyyy")
        date_str = db.child("job").child(ind).child("due").get().val()
        date_format = "dd/MM/yyyy"
        date = QDate.fromString(date_str, date_format)
        self.ui.dateedit.setDate(date)

        self.ui.savebutton.clicked.connect(self.update)
        self.ui.posedit.setText(db.child("job").child(ind).child("position").get().val())
        self.ui.eduedit.setText(db.child("job").child(ind).child("education").get().val())
        self.ui.saledit.setText(db.child("job").child(ind).child("salary").get().val())
        self.ui.avaedit.setText(db.child("job").child(ind).child("avaliable").get().val())
        self.ui.phoedit.setText(db.child("job").child(ind).child("phone").get().val())
        self.ui.reqedit.setText(db.child("job").child(ind).child("requirement").get().val())

    def update(self):
        pos = self.ui.posedit.text()
        edu = self.ui.eduedit.text()
        sal = self.ui.saledit.text()
        ava = self.ui.avaedit.text()
        pho= self.ui.phoedit.text()
        due=self.ui.dateedit.text()
        req=self.ui.reqedit.toPlainText()

        if(edit_item(pos,edu,sal,ava,pho,due,req)):
            QMessageBox.information(self,"Success", f"update successful!")
        else:
            QMessageBox.information(self,"ERROR", f"update failed.")


def main():
    app = QApplication(sys.argv)

    w = JobUI()
    w.show()

    return app.exec()

if __name__ == "__main__":
    comname = sys.argv[1]
    jobid = sys.argv[2]
    ind= comname+"_"+jobid
    sys.exit(main())