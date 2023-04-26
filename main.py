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
        self.ui.vipro.clicked.connect(self.view)

        def print_values(data, section="",count=0):
            for key in data:
                if isinstance(data[key], dict):
                    count=count+1
                    print_values(data[key], section + key + "/",count)
                    
                else:
                    if(key=="company"):
                        comp="Company: "+db.child("companies").child(data[key]).child("companyname").get().val()
                        pos="Position: "+db.child("job").child(section[:-1]).child("position").get().val()
                        sal="Salary: "+db.child("job").child(section[:-1]).child("salary").get().val()
                        self.createNewWindow(count,comp,pos,sal)


        print_values(db.child("job").get().val())

    def createNewWindow(self,rowNo,com,pos,sal):

        newName = "frame" + str(rowNo)
        newName2 = "text1_" + str(rowNo)
        newName3 = "text2_" + str(rowNo)
        newName4 = "text2_" + str(rowNo)
        self.frame = QFrame(self.ui.scrollAreaWidgetContents_4)
        self.frame.setObjectName(newName)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(500, 100))
        self.frame.setMaximumSize(QSize(500, 100))
        self.frame.setStyleSheet(u"background-color: grey;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(200, 40))
        self.label.setMaximumSize(QSize(200, 40))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(200, 40))
        self.label_2.setMaximumSize(QSize(200, 40))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(200, 40))
        self.label_3.setMaximumSize(QSize(200, 40))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")


        # print(com)
        self.label.setText(QCoreApplication.translate("MainWindow", com, None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", pos, None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", sal, None))


        setattr(self.ui, newName, self.frame)
        setattr(self.ui, newName2, self.label)
        setattr(self.ui, newName3, self.label_2)
        setattr(self.ui, newName4, self.label_2)

        self.ui.gridLayout.addWidget(self.frame, rowNo, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

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
    
    def view(self):
        if(self.userType=="0"):
            subprocess.run(['python', 'viewuserprofile.py', self.user])
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