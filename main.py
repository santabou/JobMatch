import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from mainpage import Ui_MainWindow
from config import firebaseConfig
from PySide6.QtGui import *
import pyrebase
import subprocess


firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()


class MainUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Call the subprocess file
        output = subprocess.check_output(['python', 'logsignpypyrebase.py'])

        # Convert the output bytes to a string and split it into two parts
        output_str = output.decode('utf-8').strip().split(" and ")
        
        # Extract the two input values from the output
        self.user = output_str[0]
        self.userType = output_str[1]

        if(self.userType=="0"):
            self.ui.usn.setText("Hello, "+db.child("users").child(self.user).child("firstname").get().val()+" "+db.child("users").child(self.user).child("lastname").get().val())
        else:
            self.ui.usn.setText("Welcome, "+db.child("companies").child(self.user).child("companyname").get().val())
            self.ui.uppro.setText("Create/Edit Job Application")
            self.ui.vipro.setText("View Job Application")

        self.ui.uppro.clicked.connect(self.logging)
        self.ui.gochat.clicked.connect(self.cha)



    def logging(self):
        if(self.userType=="0"):
            subprocess.run(['python', 'edituserprofile.py', self.user])
        else:
            subprocess.run(['python', 'gojob.py', self.user])
    
    def cha(self):
        if(self.userType=="0"):
            subprocess.run(['python', 'goroom.py', self.user])
        else:
            pass


def main():
    app = QApplication(sys.argv)

    w = MainUI()
    w.setWindowFlags(w.windowFlags() | Qt.WindowStaysOnTopHint)
    w.show()
    w.setWindowFlags(w.windowFlags() & ~(Qt.WindowStaysOnTopHint) | Qt.WindowCloseButtonHint)
    w.activateWindow()
    w.show()
    
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())