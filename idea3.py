dl={}
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0552764 rgba(0, 85, 127, 206), stop:0.351759 rgba(170, 170, 255, 80), stop:0.4 rgba(170, 170, 255, 80), stop:0.44 rgba(170, 170, 255, 80), stop:0.447236 rgba(170, 170, 255, 80), stop:1 rgba(255, 255, 255, 0));\n"
"")
        
        font_3 = QtGui.QFont()
        font_3.setPointSize(23)
        font = QtGui.QFont()
        font.setPointSize(14)
        font_2 = QtGui.QFont()
        font_2.setPointSize(9)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(150,20,201,31))
        self.label_5.setFont(font_3)
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet("color : pink")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50,100,201,31))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50,180,201,31))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50,260,201,31))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50,340,201,31))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label.setStyleSheet("color : white")
        self.label_2.setStyleSheet("color : white")
        self.label_3.setStyleSheet("color : white")
        self.label_4.setStyleSheet("color : white")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(220,140,300,41))
        self.label_6.setFont(font_2)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(220,220,300,41))
        self.label_7.setFont(font_2)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(220,380,300,41))
        self.label_8.setFont(font_2)
        self.label_8.setObjectName("label_8")
        self.label_6.setStyleSheet("color : red")
        self.label_7.setStyleSheet("color : red")
        self.label_8.setStyleSheet("color : red")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220,90,300,41))
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(220,170,300,41))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(220,250,300,41))
        self.dateEdit.setStyleSheet("")
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(220,330,300,41))
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.pushButton= QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240,420,191,51))
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
        self.label_5.setText(_translate("MainWindow","Ajouter une location "))
        self.label_5.adjustSize()
        self.label_6.setText(_translate("MainWindow",""))
        self.label_6.adjustSize()
        self.label_7.setText(_translate("MainWindow",""))
        self.label_7.adjustSize()
        self.label_8.setText(_translate("MainWindow",""))
        self.label_8.adjustSize()
        self.label.setText(_translate("MainWindow","CIN : "))
        self.label.adjustSize()
        self.label_2.setText(_translate("MainWindow","Matricule : "))
        self.label_2.adjustSize()
        self.label_3.setText(_translate("MainWindow","Date : "))
        self.label_3.adjustSize()
        self.label_4.setText(_translate("MainWindow","Durée (par jour) : "))
        self.label_4.adjustSize()
        self.pushButton.setText(_translate("MainWindow","ajouter"))
        
    def lire(self):
        if ((self.lineEdit_4.text().isnumeric()==False)or(self.lineEdit_4.text()=='0')):
            self.label_8.setText("Durée invalide")
            self.label_8.adjustSize()
        else:
            self.label_8.setText("")
            self.label_8.adjustSize()
        filename1="locations.txt"
        l1=[]
        l2=[]
        dl={}
        with open(filename1) as f1:
            for line in f1:
                l1=line.split()
                b=l1[0]
                c=l1[1]
                a=l1[2]
                l2=l1[3:]
                dl[b,c,a]=l2
        
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
        box=0
        mat1=self.lineEdit_2.text()[0:3]
        mat2=self.lineEdit_2.text()[3:5]
        mat3=self.lineEdit_2.text()[5:]
        if ((len(self.lineEdit_2.text())!=9)or(mat1.isnumeric()==False)or(mat3.isnumeric()==False)or(mat2!="tu" ) ):
            self.label_7.setText("Matricule invalide")
            self.label_7.adjustSize()
    
        elif ((self.lineEdit_2.text() in cle)==False):
            self.label_7.setText("")
            self.label_7.adjustSize()
            msg=QMessageBox()
            msg.setWindowTitle("erreur")
            msg.setText("Matricule introuvable")
            x=msg.exec_()
            box=1
        elif ((self.lineEdit_2.text() in cle)==True):
            self.label_7.setText("")
            self.label_7.adjustSize()
            for c,v in d.items():
                if (c==self.lineEdit_2.text()):
                    if(v[2]=="Louée"):
                        msg=QMessageBox()
                        msg.setWindowTitle("erreur")
                        msg.setText("cette voiture est louée")
                        x=msg.exec_()
                        box=1
                    else:
                        if(self.label_8.text()==""):
                            dure=int(self.lineEdit_4.text())
                            prix=v[4]
                            prix=int(prix)
                            montant=str(prix*dure)
                            print (montant)
                        
        
                    
        filename1="clients.txt"
        l1=[]
        l2=[]
        dc={}
        with open(filename1) as f1:
            for line in f1:
                l1=line.split()
                b=l1[0]
                l2=l1[1:]
                dc[b]=l2
        cle=list(dc.keys())
        box2=0
        l1=['0','1','2']
        
        if ((self.lineEdit.text().isnumeric()==False)or(len(self.lineEdit.text())!=8) or (self.lineEdit.text()=='00000000') or((self.lineEdit.text()[0] in l1)==False)):
            self.label_6.setText("CIN invalide")
            self.label_6.adjustSize()
        
        elif ((self.lineEdit.text() in cle)==False):
            self.label_6.setText("")
            self.label_6.adjustSize()
            msg=QMessageBox()
            msg.setWindowTitle("erreur")
            msg.setText("CIN introuvable")
            x=msg.exec_()
            box2=1
        else:
            self.label_6.setText("")
            self.label_6.adjustSize()
        tm=self.dateEdit.date()
        var=tm.toPyDate()
        var=str(var)
        if ((self.label_7.text()=="")and(self.label_6.text()=="")and(box==0)and(self.label_8.text()=="")and(box2==0)):
            dl[self.lineEdit.text(),self.lineEdit_2.text(),var]=[self.lineEdit_4.text(),montant]
            msg=QMessageBox()
            msg.setWindowTitle("Succés")
            msg.setText("Location ajoutée avec succés")
            x=msg.exec_()
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_4.clear()
            with open ('locations.txt','w') as f:
                for cle,valeur in dl.items():
                    f.write(cle[0]+" ")
                    f.write(cle[1]+" ")
                    f.write(cle[2]+" ")
                    f.write(valeur[0]+" ")
                    f.write(valeur[1]+'\n')
    
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())