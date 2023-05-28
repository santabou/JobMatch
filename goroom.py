import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from config import firebaseConfig
from PySide6.QtGui import *
import pyrebase
from enternumber import Ui_Form
from chat import ChatUI

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

class GoCUI(QWidget):
    def __init__(self,u):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.ok.clicked.connect(self.go)
        self.user=u

    def go(self):
        rn=self.ui.lineEdit.text()
        pa=self.ui.passline.text()
        if(db.child("ms").child(rn).get().val()==None):
            data = {
                "message": "",
                "password":pa
            }
            db.child("ms").child(rn).update(data)
        if(pa==db.child("ms").child(rn).child("password").get().val()):
            self.openchat(rn,pa)
        else:
            QMessageBox.information(self,"ERROR", f"Wrong Password.")

    def openchat(self,rn,pas):
        self.open=QWidget()
        self.eui=ChatUI(self.user,rn,pas)
        self.eui.show()
    
def main():
    app = QApplication(sys.argv)

    w = GoCUI()
    w.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())