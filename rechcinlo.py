
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("contenu_locations.ui",self)
        self.tableWidget.setColumnWidth(0,150)
        self.tableWidget.setColumnWidth(1,150)
        self.tableWidget.setColumnWidth(2,150)
        self.tableWidget.setColumnWidth(3,150)
        self.tableWidget.setColumnWidth(4,150)
        self.contenu()
    def contenu(self):
        filename1="locations.txt"
        l1=[]
        l2=[]
        dl={}
        with open(filename1) as f1:
            for line in f1:
                l1=line.split()
                b=l1[0];c=l1[1];d=l1[2]
                l2=l1[3:]
                dl[b,c,d]=l2
        filename="enregistrer.txt"
        l=[]
        with open(filename) as f2:
            for line in f2:
                l=line.split()
                a=l[0]
        row=0
        self.tableWidget.setRowCount(len(dl))
        for cle,valeur in dl.items():
            if (cle[0]==a):
                
                self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(cle[0]))
                self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(cle[1]))
                self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(cle[2]))
                self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(valeur[0]))
                self.tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(valeur[1]))
                row=row+1
    
app=QApplication(sys.argv)
mainwindow=MainWindow()
widget= QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(650)
widget.setFixedWidth(765)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")