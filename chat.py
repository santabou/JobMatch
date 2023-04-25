import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from config import firebaseConfig
from PySide6.QtGui import *
import pyrebase
from text import Ui_Form

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

def message(mess):
    if(db.child("ms").child(rn).child("message").get().val()==None):
        mess1=mess
    else:
        mess1= str(db.child("ms").child(rn).child("message").get().val())+str(mess)
    data = {
        "message": mess1+"\n"
    }
    db.child("ms").child(rn).update(data)



class ChatU(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.roomnum.setText(rn)
        self.ui.myname.setText(arg1)
        self.ui.pushButton.clicked.connect(self.send)
        self.ui.textEdit.setText(db.child("ms").child(rn).child("message").get().val())
        self.stream=db.child("ms").stream(self.stream_handler)

    
    def stop_stream(self):
        self.stream.close()

    def closeEvent(self, event):
        self.stop_stream()
        event.accept()

    def send(self):
        mess=str(arg1)+": "+str(self.ui.lineEdit.text())
        message(mess)
        self.ui.lineEdit.setText("")

    def stream_handler(self,message):
        if message["event"] == "patch":
            QMetaObject.invokeMethod(self.ui.textEdit, "setText", 
                                     Qt.QueuedConnection,
                                     Q_ARG(str, db.child("ms").child(rn).child("message").get().val()))
    

        
def main():
    app = QApplication(sys.argv)

    w = ChatU()
    w.show()
    return app.exec()

if __name__ == "__main__":
    arg1 = sys.argv[1]
    rn = sys.argv[2]
    # arg1="u1"
    # rn="1234"
    sys.exit(main())