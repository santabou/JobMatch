import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from viewprofile import Ui_Form
from PySide6.QtGui import *
from db import User,Session,engine

local_session=Session(bind=engine)

class VUserUI(QWidget):
    def __init__(self,u):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.user=u
        user = local_session.query(User).filter_by(username=self.user).first()
        if user:
            self.ui.fnlabel.setText(user.firstname)
            self.ui.lnlabel.setText(user.lastname)
            self.ui.emlabel.setText(user.email)
            self.ui.doblabel.setText(user.dob)
            self.ui.gdlabel.setText(user.gender)
            self.ui.pnblabel.setText(user.phone_number)
            self.ui.poslabel.setText(user.position)
            self.ui.edulabel.setText(user.education)
            self.ui.eprlabel.setText(user.experience)
            self.ui.sklabel.setText(user.skill)

def main():    
    app = QApplication(sys.argv)
    w = VUserUI()
    w.show()

    return app.exec()

if __name__ == "__main__":
    sys.exit(main())