import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from jobnumber import Ui_Form
from editjobapp import JobUI

class GoUI(QWidget):
    def __init__(self,u):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.ok.clicked.connect(self.go)
        self.user=u

    def go(self):
        jn=self.ui.comboBox.currentText()
        self.openedituser(jn)

    def openedituser(self,jn):
        self.open=QWidget()
        self.eui=JobUI(self.user,jn)
        self.eui.show()

        
def main():
    app = QApplication(sys.argv)

    w = GoUI()
    w.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())