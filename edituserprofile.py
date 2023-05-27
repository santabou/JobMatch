import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from useredit import Ui_Form
from PySide6.QtGui import *
from db import User,Session,engine

local_session=Session(bind=engine)

class UserUI(QWidget):
    def __init__(self,u):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.user=u
        user = local_session.query(User).filter_by(username=self.user).first()

        if user:
            # Set the date in the QDateEdit widget
            date_str = user.dob
            date_format = "dd/MM/yyyy"
            date = QDate.fromString(date_str, date_format)
            self.ui.dobedit.setDate(date)

            self.ui.updateedit.clicked.connect(self.update)
            # Set the text
            self.ui.firstedit.setText(user.firstname)
            self.ui.lastedit.setText(user.lastname)
            self.ui.emailedit.setText(user.email)
            self.ui.phoneedit.setText(user.phone_number)
            self.ui.posedit.setText(user.position)
            self.ui.eduedit.setText(user.education)
            self.ui.epredit.setText(user.experience)
            self.ui.skilledit.setText(user.skill)

            # Set the appropriate gender radio button
            if user.gender == "Male":
                self.ui.malebutton.setChecked(True)
            elif user.gender == "Female":
                self.ui.femalebutton.setChecked(True)
            elif user.gender == "Prefer not to say":
                self.ui.otherbutton.setChecked(True)

    def update(self):
        # Get the updated values
        firstname = self.ui.firstedit.text()
        lastname = self.ui.lastedit.text()
        dob = self.ui.dobedit.text()
        gender = ""
        email = self.ui.emailedit.text()
        pos= self.ui.posedit.text()
        pho=self.ui.phoneedit.text()
        edu = self.ui.eduedit.toPlainText()
        epr = self.ui.epredit.toPlainText()
        sk =  self.ui.skilledit.toPlainText()
        username= self.user

        # Determine the selected gender
        if(self.ui.malebutton.isChecked()):
            gender = "Male"
        elif (self.ui.femalebutton.isChecked()):
            gender = "Female"
        elif (self.ui.otherbutton.isChecked()):
            gender = "Prefer not to say"

         # Update the user information
        if(self.edit_item(username, email, firstname, lastname, dob,pos,pho,gender,edu,epr,sk)):
            QMessageBox.information(self,"Success", f"update successful!")
        else:
            QMessageBox.information(self,"ERROR", f"update failed.")
    
    def edit_item(self,username, email, firstname, lastname, dob, pos, pho, gender, edu, epr, sk):
        # Retrieve the user from the database
        user = local_session.query(User).filter_by(username=username).first()
        if user:
            user.email = email
            user.firstname = firstname
            user.lastname = lastname
            user.dob = dob
            user.position = pos
            user.phone_number = pho
            user.gender = gender
            user.education = edu
            user.experience = epr
            user.skill = sk
            local_session.commit()
            return True
        return False

def main():
    app = QApplication(sys.argv)
    w = UserUI()
    w.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())