from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
import sys
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
        
class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("rechcinnn.ui",self)
        self.label_3.setText("")
        self.label_3.adjustSize()
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.tableWidget.setColumnWidth(0,150)
        self.tableWidget.setColumnWidth(1,150)
        self.tableWidget.setColumnWidth(2,150)
        self.tableWidget.setColumnWidth(3,150)
        self.tableWidget.setColumnWidth(4,150)
        self.tableWidget.setColumnWidth(5,150)
        self.tableWidget.setColumnWidth(6,150)
        self.pushButton.clicked.connect(self.lire)
    def lire(self):
        l1=['0','1','2']
        if ((self.lineEdit.text().isnumeric()==False)or(len(self.lineEdit.text())!=8)or (self.lineEdit.text()=='00000000') or((self.lineEdit.text()[0] in l1)==False)  ):
            self.tableWidget.setRowCount(7)
            self.tableWidget.setItem(-1,1,QtWidgets.QTableWidgetItem(""))
            self.tableWidget.setItem(0,1,QtWidgets.QTableWidgetItem(""))
            self.tableWidget.setItem(1,1,QtWidgets.QTableWidgetItem(""))
            self.tableWidget.setItem(2,1,QtWidgets.QTableWidgetItem(""))
            self.tableWidget.setItem(3,1,QtWidgets.QTableWidgetItem(""))
            self.tableWidget.setItem(4,1,QtWidgets.QTableWidgetItem(""))
            self.tableWidget.setItem(5,1,QtWidgets.QTableWidgetItem(""))
            self.label_3.setText("CIN invalide")
            self.label_3.adjustSize()
        else:
            self.label_3.setText("")
            self.label_3.adjustSize()
        filename1="clients.txt"
        l1=[]
        l2=[]
        d={}
        with open(filename1) as f1:
            for line in f1:
                l1=line.split()
                b=l1[0]
                l2=l1[1:]
                d[b]=l2
        cle=list(d.keys())
        if(((self.lineEdit.text() in cle)==False)and(self.label_3.text()=="")):
            self.tableWidget.setRowCount(7)
            self.tableWidget.setItem(-1,1,QtWidgets.QTableWidgetItem(""))
            self.tableWidget.setItem(0,1,QtWidgets.QTableWidgetItem(""))
            self.tableWidget.setItem(1,1,QtWidgets.QTableWidgetItem(""))
            self.tableWidget.setItem(2,1,QtWidgets.QTableWidgetItem(""))
            self.tableWidget.setItem(3,1,QtWidgets.QTableWidgetItem(""))
            self.tableWidget.setItem(4,1,QtWidgets.QTableWidgetItem(""))
            self.tableWidget.setItem(5,1,QtWidgets.QTableWidgetItem(""))
            msg=QMessageBox()
            msg.setWindowTitle("Erreur")
            msg.setText("CIN introuvable")
            x=msg.exec_()
        
        if ((self.lineEdit.text() in cle)==True):
            self.tableWidget.setRowCount(7)
            for c,valeur in d.items():
                if (c==self.lineEdit.text()):
                    self.tableWidget.setItem(-1,1,QtWidgets.QTableWidgetItem(c))
                    self.tableWidget.setItem(0,1,QtWidgets.QTableWidgetItem(valeur[0]))
                    self.tableWidget.setItem(1,1,QtWidgets.QTableWidgetItem(valeur[1]))
                    self.tableWidget.setItem(2,1,QtWidgets.QTableWidgetItem(valeur[2]))
                    self.tableWidget.setItem(3,1,QtWidgets.QTableWidgetItem(valeur[3]))
                    self.tableWidget.setItem(4,1,QtWidgets.QTableWidgetItem(valeur[4]))
                    self.tableWidget.setItem(5,1,QtWidgets.QTableWidgetItem(valeur[5]))
            
        
app=QApplication(sys.argv)
mainwindow=MainWindow()
widget= QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(450)
widget.setFixedWidth(580)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")