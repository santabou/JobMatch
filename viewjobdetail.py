import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from viewjob import Ui_Form
from PySide6.QtGui import *
from db import Job,Session,engine

local_session=Session(bind=engine)

class VJobUI(QWidget):
    def __init__(self,u):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.jid=u
        job = local_session.query(Job).filter_by(jobid=self.jid).first()
        if job:
            self.ui.cnlabel.setText(job.comname)
            self.ui.reqlabel.setText(job.requirement)
            self.ui.emlabel.setText(job.email)
            self.ui.seatlabel.setText(job.available)
            self.ui.sallabel.setText(job.salary)
            self.ui.pnblabel.setText(job.phone)
            self.ui.poslabel.setText(job.position)
            self.ui.edulabel.setText(job.education)
            self.ui.loclabel.setText(job.location)
            self.ui.avalabel.setText(job.due)
        else:
            QMessageBox.information(self, "ERROR", f"Job Not Found")

def main():    
    app = QApplication(sys.argv)
    w = VJobUI()
    w.show()

    return app.exec()

if __name__ == "__main__":
    sys.exit(main())