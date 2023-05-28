import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from config import firebaseConfig
from PySide6.QtGui import *
import pyrebase
from text import Ui_Form
from db import Message,Session,engine

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

local_session=Session(bind=engine)

class ChatUI(QWidget):
    def __init__(self,u,r,p=""):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.user=u
        self.room=r
        self.password=p
        # Set up the UI
        self.ui.roomnum.setText(self.room)
        self.ui.myname.setText(self.user)
        self.ui.pushButton.clicked.connect(self.send)
        self.ui.textEdit.setText(db.child("ms").child(self.room).child("message").get().val())

        # Start streaming updates from the Firebase database
        self.stream=db.child("ms").stream(self.stream_handler)
    
    def stop_stream(self):
        # Stop streaming updates from the Firebase database
        self.stream.close()

    def closeEvent(self, event):
        # Handle the close event by stopping the stream and accepting the event
        if local_session.query(Message).filter_by(roomNo=self.room).first() is None:
            self.create_mess(db.child("ms").child(self.room).child("message").get().val())
        else:
            self.add_mess(db.child("ms").child(self.room).child("message").get().val())
        self.stop_stream()
        event.accept()

    def send(self):
        # Get the message from the input line edit and send it to the Firebase database
        mess=str(self.user)+": "+str(self.ui.lineEdit.text())
        self.message(mess,self.room)
        self.ui.lineEdit.setText("")

    def stream_handler(self,message):
        if message["event"] == "patch":
            # Update the text in the text edit widget with the updated message from the database
            QMetaObject.invokeMethod(self.ui.textEdit, "setText", 
                                     Qt.QueuedConnection,
                                     Q_ARG(str, db.child("ms").child(self.room).child("message").get().val()))
            
    def message(self,mess,rn):
        # Update the message in the Firebase database for the given room number
        if(db.child("ms").child(rn).child("message").get().val()==None):
            mess1=mess
        else:
            mess1= str(db.child("ms").child(rn).child("message").get().val())+str(mess)
        data = {
            "message": mess1+"\n"
        }
        db.child("ms").child(rn).update(data)

    def create_mess(self,ms):
        message = Message(
            roomNo=self.room,
            mess=ms,
            password=self.password
        )
        local_session.add(message)
        local_session.commit()

    def add_mess(self,ms):
        mass = local_session.query(Message).filter_by(roomNo=self.room).first()
        if mass:
            mass.mess = ms
            local_session.commit()
            return True
        return False
        
def main():
    app = QApplication(sys.argv)
    w = ChatUI()
    w.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())