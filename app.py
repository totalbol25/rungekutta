import sys, parser, math
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from untitled import Ui_Dialog

from runge import RungeKutta, parseEquation, f


class AppWindow(QDialog):
    
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.btnClicked)
        self.ui.pushButton.clicked.connect(self.btnClicked_2)
        self.show()
 
    

    def btnClicked(self):
        if (float(self.ui.lineEdit_3.text()) > float(self.ui.lineEdit_5.text())):
            self.ui.lineEdit_3.setText('x0 должно быть меньше xmax')
            self.ui.lineEdit_5.setText('x0 должно быть меньше xmax')
        else:
            self.exp = parseEquation(self.ui.lineEdit.text())
            self.y = float(self.ui.lineEdit_2.text())
            self.x = float(self.ui.lineEdit_3.text())
            self.h = float(self.ui.lineEdit_4.text())
            self.xmax = float(self.ui.lineEdit_5.text())

            self.ans = RungeKutta(self.xmax, self.exp, self.x, self.y, self.h)  

            self.track = self.h

            self.f = open('output.txt', 'w')

            for i in self.ans:
                self.ui.textEdit.append("y{:.2f} = {:.5f}".format(self.track, i))
                self.f.write("y{:.2f} = {:.5f}".format(self.track, i) + "\n")
                self.track += self.h    

    def btnClicked_2(self):
        with open ("data.txt", "r") as myfile:
            self.data = myfile.readlines()
            self.ui.lineEdit.setText(self.data[0])
            self.ui.lineEdit_2.setText(self.data[1])
            self.ui.lineEdit_3.setText(self.data[2])
            self.ui.lineEdit_4.setText(self.data[3])
            self.ui.lineEdit_5.setText(self.data[4])


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())