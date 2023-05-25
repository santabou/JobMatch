import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from config import firebaseConfig
from PySide6.QtGui import *
import pyrebase
from text import Ui_Form

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

class ChatUI(QWidget):
    def __init__(self,u,r):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.user=u
        self.room=r
        self.ui.roomnum.setText(self.room)
        self.ui.myname.setText(self.user)
        self.ui.pushButton.clicked.connect(self.send)
        self.ui.textEdit.setText(db.child("ms").child(self.room).child("message").get().val())
        self.stream=db.child("ms").stream(self.stream_handler)
    
    def stop_stream(self):
        self.stream.close()

    def closeEvent(self, event):
        self.stop_stream()
        event.accept()

    def send(self):
        mess=str(self.user)+": "+str(self.ui.lineEdit.text())
        self.message(mess,self.room)
        self.ui.lineEdit.setText("")

    def stream_handler(self,message):
        if message["event"] == "patch":
            QMetaObject.invokeMethod(self.ui.textEdit, "setText", 
                                     Qt.QueuedConnection,
                                     Q_ARG(str, db.child("ms").child(self.room).child("message").get().val()))
            
    def message(self,mess,rn):
        if(db.child("ms").child(rn).child("message").get().val()==None):
            mess1=mess
        else:
            mess1= str(db.child("ms").child(rn).child("message").get().val())+str(mess)
        data = {
            "message": mess1+"\n"
        }
        db.child("ms").child(rn).update(data)
        
def main():
    app = QApplication(sys.argv)
    w = ChatUI()
    w.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())