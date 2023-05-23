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
            self.createjoblist(db.child("job").get().val())
        else:
            self.ui.usn.setText("Welcome, "+db.child("companies").child(self.user).child("companyname").get().val())
            self.ui.uppro.setText("Create/Edit Job Application")
            self.ui.vipro.setText("View Job Application")

        self.ui.uppro.clicked.connect(self.logging)
        self.ui.gochat.clicked.connect(self.cha)
        self.ui.vipro.clicked.connect(self.view)
        self.ui.clearButton.clicked.connect(self.reloadlist)
        self.ui.searchButton.clicked.connect(self.searching)

    def removeAll(self):
        for i in reversed(range(self.ui.gridLayout.count())):
            widget = self.ui.gridLayout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
                self.ui.gridLayout.removeWidget(widget)

    def searching(self):
        self.removeAll()
        if(self.userType=="0"):
            search=self.ui.searchEdit.text()
            self.createjoblist(db.child("job").get().val(),search)

    def reloadlist(self):
        self.removeAll()
        if(self.userType=="0"):
            self.ui.searchEdit.setText("")
            self.createjoblist(db.child("job").get().val())

    def createjoblist(self,data,sear="",section="",count=0):
        for key in data:
            if isinstance(data[key], dict):
                count=count+1
                self.createjoblist(data[key],sear, section + key + "/",count)
                
            else:
                if(sear!=""):
                    if(sear.lower() in db.child("job").child(section[:-1]).child(key).get().val().lower()):
                        comp=db.child("job").child(section[:-1]).child("companyname").get().val()
                        cnum2=section[:-1]
                        pos=db.child("job").child(section[:-1]).child("position").get().val()
                        sal=db.child("job").child(section[:-1]).child("salary").get().val()
                        self.createNewWindow(count,comp,pos,sal,cnum2)
                else:
                    if(key=="username"):
                        comp=db.child("job").child(section[:-1]).child("companyname").get().val()
                        cnum2=section[:-1]
                        pos=db.child("job").child(section[:-1]).child("position").get().val()
                        sal=db.child("job").child(section[:-1]).child("salary").get().val()
                        self.createNewWindow(count,comp,pos,sal,cnum2)




    def createNewWindow(self,rowNo,com,pos,sal,cnum2):

        framename = "frame_" + str(rowNo)
        comnam = "comn_" + str(rowNo)
        posnam = "posn_" + str(rowNo)
        salnam = "saln_" + str(rowNo)
        morenam = "morn_" + str(rowNo)
        subnam = "subn_" + str(rowNo)

        self.frame = QFrame(self.ui.scrollAreaWidgetContents_4)
        self.frame.setObjectName(framename)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(500, 100))
        self.frame.setMaximumSize(QSize(500, 100))
        self.frame.setStyleSheet(u"background-color: grey;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.label = QLabel(self.frame)
        self.frame.setObjectName(comnam)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(200, 20))
        self.label.setMaximumSize(QSize(200, 20))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.label_2 = QLabel(self.frame)
        self.frame.setObjectName(posnam)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(200, 20))
        self.label_2.setMaximumSize(QSize(200, 20))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.label_3 = QLabel(self.frame)
        self.frame.setObjectName(salnam)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(200, 20))
        self.label_3.setMaximumSize(QSize(200, 20))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.button = QPushButton(self.frame)
        self.frame.setObjectName(morenam)
        self.button.setObjectName(u"button")
        self.button.setMinimumSize(QSize(120, 20))
        self.button.setMaximumSize(QSize(120, 20))
        self.button.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.button2 = QPushButton(self.frame)
        self.frame.setObjectName(subnam)
        self.button2.setObjectName(u"button2")
        self.button2.setMinimumSize(QSize(120, 20))
        self.button2.setMaximumSize(QSize(120, 20))
        self.button2.setStyleSheet(u"color: rgb(255, 255, 255);")


        # print(com)
        self.label.setText(QCoreApplication.translate("MainWindow", "Company: "+com, None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", "Position: "+pos, None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", "Salary: "+sal, None))
        self.button.setText(QCoreApplication.translate("MainWindow", u"view more", None))
        self.button2.setText(QCoreApplication.translate("MainWindow", u"submit Application", None))


        setattr(self.ui, framename, self.frame)
        setattr(self.ui, comnam, self.label)
        setattr(self.ui, posnam, self.label_2)
        setattr(self.ui, salnam, self.label_3)
        setattr(self.ui, morenam, self.button)
        setattr(self.ui, subnam, self.button2)

        self.ui.gridLayout.addWidget(self.frame, rowNo, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.button, 2, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_2.addWidget(self.button2, 2, 2, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.button.setProperty("jobdes", cnum2)
        self.button.clicked.connect(self.more)
    
    def more(self):
        button=self.sender()
        comna=button.property("comname")
        jobd=button.property("jobdes")
        # j=db.child("job").child(jobd).get().val()
        # self.print_values(j)
        subprocess.run(['python', 'viewjobdetail.py', jobd])
        

    
    def print_values(self,data, section=""):
        for key in data:
            if isinstance(data[key], dict):
                self.print_values(data[key], section + key + "/")
            else:
                if (key=="username"):
                    pass
                else:
                    if section:
                        print(section[:-1])
                    print(key+":"+data[key])

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