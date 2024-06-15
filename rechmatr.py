from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
import sys
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
        
class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("rechmattt.ui",self)
        self.label_3.setText("")
        self.label_3.adjustSize()
        self.tableWidget.setColumnWidth(0,150)
        self.tableWidget.setColumnWidth(1,150)
        self.tableWidget.setColumnWidth(2,150)
        self.tableWidget.setColumnWidth(3,150)
        self.tableWidget.setColumnWidth(4,150)
        self.tableWidget.setColumnWidth(5,150)
        self.pushButton.clicked.connect(self.lire)
    def lire(self):
        mat1=self.lineEdit.text()[0:3]
        mat2=self.lineEdit.text()[3:5]
        mat3=self.lineEdit.text()[5:]
        if ((len(self.lineEdit.text())!=9)or(mat1.isnumeric()==False)or(mat3.isnumeric()==False)or(mat2!="tu" ) ):
            self.label_3.setText("Matricule invalide")
            self.label_3.adjustSize()
            self.tableWidget.setRowCount(6)
            self.tableWidget.setItem(-1,1,QtWidgets.QTableWidgetItem(""))
            self.tableWidget.setItem(0,1,QtWidgets.QTableWidgetItem(""))
            self.tableWidget.setItem(1,1,QtWidgets.QTableWidgetItem(""))
            self.tableWidget.setItem(2,1,QtWidgets.QTableWidgetItem(""))
            self.tableWidget.setItem(3,1,QtWidgets.QTableWidgetItem(""))
            self.tableWidget.setItem(4,1,QtWidgets.QTableWidgetItem(""))
        else:
            self.label_3.setText("")
            self.label_3.adjustSize()
        filename1="voitures.txt"
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
            self.tableWidget.setRowCount(6)
            self.tableWidget.setItem(-1,1,QtWidgets.QTableWidgetItem(""))
            self.tableWidget.setItem(0,1,QtWidgets.QTableWidgetItem(""))
            self.tableWidget.setItem(1,1,QtWidgets.QTableWidgetItem(""))
            self.tableWidget.setItem(2,1,QtWidgets.QTableWidgetItem(""))
            self.tableWidget.setItem(3,1,QtWidgets.QTableWidgetItem(""))
            self.tableWidget.setItem(4,1,QtWidgets.QTableWidgetItem(""))
            msg=QMessageBox()
            msg.setWindowTitle("Erreur")
            msg.setText("Matricule introuvable")
            x=msg.exec_()
        
        if ((self.lineEdit.text() in cle)==True):
            self.tableWidget.setRowCount(6)
            for c,valeur in d.items():
                if (c==self.lineEdit.text()):
                    self.tableWidget.setItem(-1,1,QtWidgets.QTableWidgetItem(c))
                    self.tableWidget.setItem(0,1,QtWidgets.QTableWidgetItem(valeur[0]))
                    self.tableWidget.setItem(1,1,QtWidgets.QTableWidgetItem(valeur[1]))
                    self.tableWidget.setItem(2,1,QtWidgets.QTableWidgetItem(valeur[2]))
                    self.tableWidget.setItem(3,1,QtWidgets.QTableWidgetItem(valeur[3]))
                    self.tableWidget.setItem(4,1,QtWidgets.QTableWidgetItem(valeur[4]))
            
        
app=QApplication(sys.argv)
mainwindow=MainWindow()
widget= QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(470)
widget.setFixedWidth(550)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")