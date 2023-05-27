import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from jobedit import Ui_Form
from PySide6.QtGui import *
from db import Company,Job,Session,engine

local_session=Session(bind=engine)

class JobUI(QWidget):
    def __init__(self,c,i):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.comname=c
        self.id=i
        self.ind= self.comname+"_"+self.id
        if local_session.query(Job).filter_by(jobid=self.ind).first() is None:
            self.create_job(self.comname,self.ind)

        self.ui.dateedit.setCalendarPopup(True)
        self.ui.dateedit.setDisplayFormat("dd/MM/yyyy")
        job = local_session.query(Job).filter_by(jobid=self.ind).first()
        if job:
            # Set the date in the QDateEdit widget
            date_str = job.due
            date_format = "dd/MM/yyyy"
            date = QDate.fromString(date_str, date_format)
            self.ui.dateedit.setDate(date)

            self.ui.savebutton.clicked.connect(self.update)
            # Set the text
            self.ui.posedit.setText(job.position)
            self.ui.eduedit.setText(job.education)
            self.ui.saledit.setText(job.salary)
            self.ui.avaedit.setText(job.available)
            self.ui.phoedit.setText(job.phone)
            self.ui.reqedit.setText(job.requirement)

    def update(self):
        # Get the updated values
        pos = self.ui.posedit.text()
        edu = self.ui.eduedit.text()
        sal = self.ui.saledit.text()
        ava = self.ui.avaedit.text()
        pho= self.ui.phoedit.text()
        due=self.ui.dateedit.text()
        req=self.ui.reqedit.toPlainText()

        # Update the information
        if(self.edit_item(pos,edu,sal,ava,pho,due,req,self.ind)):
            QMessageBox.information(self,"Success", f"update successful!")
        else:
            QMessageBox.information(self,"ERROR", f"update failed.")

    def create_job(self,cn,jid):
        com = local_session.query(Company).filter_by(username=cn).first()
        job = Job(
                    jobid= jid,
                    username= com.username,
                    comname= com.companyname,
                    position="",
                    salary="",
                    available="",
                    due="",
                    email=com.email,
                    phone="",
                    location=com.location,
                    education="",
                    requirement="",
                    apply=""
        )
        local_session.add(job)
        local_session.commit()

    def edit_item(self,pos, edu, sal, ava, pho, due, req,ind):
        job = local_session.query(Job).filter_by(jobid=ind).first()
        if job:
            job.position = pos
            job.education = edu
            job.salary = sal
            job.available = ava
            job.phone = pho
            job.due = due
            job.requirement = req
            local_session.commit()
            return True
        return False

def main():
    app = QApplication(sys.argv)
    w = JobUI()
    w.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())