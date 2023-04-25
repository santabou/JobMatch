import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from config import firebaseConfig
from PySide6.QtGui import *
import pyrebase
from enternumber import Ui_Form
import subprocess

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

class ChatU(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.ok.clicked.connect(self.go)

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
            subprocess.check_output(['python', 'chat.py',arg1,rn])
        else:
            QMessageBox.information(self,"ERROR", f"Wrong Password.")
        
    

        
def main():
    app = QApplication(sys.argv)

    w = ChatU()
    w.show()
    return app.exec()

if __name__ == "__main__":
    arg1 = sys.argv[1]
    # arg1="u1"
    sys.exit(main())