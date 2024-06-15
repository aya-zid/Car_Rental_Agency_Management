
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("contenu_voitures.ui",self)
        self.tableWidget.setColumnWidth(0,150)
        self.tableWidget.setColumnWidth(1,150)
        self.tableWidget.setColumnWidth(2,150)
        self.tableWidget.setColumnWidth(3,150)
        self.tableWidget.setColumnWidth(4,150)
        self.tableWidget.setColumnWidth(5,150)
        self.contenu()
    
    def contenu(self):
        d={}
        filename="voitures.txt"
        l1=[]
        l2=[]
        with open(filename) as f:
            for line in f:
                l1=line.split()
                a=l1[0]
                l2=l1[1:]
                d[a]=l2    
        
        row=0
        self.tableWidget.setRowCount(len(d))
        for cle,valeur in d.items():
            if (valeur[2]=="Disponible"):
                self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(cle))
                self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(valeur[0]))
                self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(valeur[1]))
                self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(valeur[2]))
                self.tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(valeur[3]))
                self.tableWidget.setItem(row,5,QtWidgets.QTableWidgetItem(valeur[4]))
                row=row+1
        
app=QApplication(sys.argv)
mainwindow=MainWindow()
widget= QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(650)
widget.setFixedWidth(920)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")