import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from config import firebaseConfig
from PySide6.QtGui import *
import pyrebase
from jobnumber import Ui_Form
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
        jn=self.ui.comboBox.currentText()
        if(db.child("job").child(comname+"_"+jn).get().val()==None):
            data = {
                "position": "",
                "education": "",
                "salary": "",
                "avaliable": "",
                "phone": "",
                "due":"",
                "requirement":"",
                "company":comname
            }
            db.child("job").child(comname+"_"+jn).update(data)
        subprocess.check_output(['python', 'editjobapp.py',comname,jn])
        
    

        
def main():
    app = QApplication(sys.argv)

    w = ChatU()
    w.show()
    return app.exec()

if __name__ == "__main__":
    comname = sys.argv[1]
    # arg1="u1"
    sys.exit(main())