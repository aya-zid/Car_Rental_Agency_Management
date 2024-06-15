from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0552764 rgba(0, 85, 127, 206), stop:0.351759 rgba(170, 170, 255, 80), stop:0.4 rgba(170, 170, 255, 80), stop:0.44 rgba(170, 170, 255, 80), stop:0.447236 rgba(170, 170, 255, 80), stop:1 rgba(255, 255, 255, 0));\n"
"")
    
        font_3 = QtGui.QFont()
        font_3.setPointSize(20)
        font = QtGui.QFont()
        font.setPointSize(16)
        font_2 = QtGui.QFont()
        font_2.setPointSize(9)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50,20,411,41))
        self.label_3.setFont(font_3)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("color : pink")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130,90,500,23))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color : white")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(100,200,211,51))
        self.label_7.setObjectName("label_7")
        self.label_7.setStyleSheet("color : red")
        self.label_7.setFont(font_2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100,140,211,51))
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")

        self.pushButton= QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100,250,190,50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")

        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton.clicked.connect(self.lire)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow","CIN : "))
        self.label.adjustSize()
        self.label_7.setText(_translate("MainWindow",""))
        self.label_7.adjustSize()
        self.label_3.setText(_translate("MainWindow","Suppresion d'un client"))
        self.label_3.adjustSize()
      
        
        self.pushButton.setText(_translate("MainWindow","supprimer"))
    def lire(self):
        l1=['0','1','2']
        if ((self.lineEdit.text().isnumeric()==False)or(len(self.lineEdit.text())!=8) or (self.lineEdit.text()=='00000000') or((self.lineEdit.text()[0] in l1)==False)):
            self.label_7.setText("CIN invalide")
            self.label_7.adjustSize()
        else:
            self.label_7.setText("")
            self.label_7.adjustSize()
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
        if ((self.lineEdit.text() in cle)==True):
            del d[self.lineEdit.text()]
            msg=QMessageBox()
            msg.setWindowTitle("Succés")
            msg.setText("Supression effectuée avec succés")
            x=msg.exec_()
        if(((self.lineEdit.text() in cle)==False)and(self.label_7.text()=="")):
            msg=QMessageBox()
            msg.setWindowTitle("Erreur")
            msg.setText("CIN introuvable")
            x=msg.exec_()
            
        with open ('clients.txt','w') as f:
            for cle,valeur in d.items():
                f.write(cle+" ")
                f.write(valeur[0]+" ")
                f.write(valeur[1]+" ")
                f.write(valeur[2]+" ")
                f.write(valeur[3]+" ")
                f.write(valeur[4]+" ")
                f.write(valeur[5]+'\n')     
        
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())