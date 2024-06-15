dc={}
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 635)
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
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(200,10,411,41))
        self.label_9.setFont(font_3)
        self.label_9.setObjectName("label_3")
        self.label_9.setStyleSheet("color : pink")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50,80,201,31))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color : white")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50,150,201,31))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("color : white")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50,220,201,31))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("color : white")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50,290,201,31))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("color : white")
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50,360,201,31))
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet("color : white")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50,430,201,31))
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet("color : white")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50,500,201,31))
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_6")
        self.label_7.setStyleSheet("color : white")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(180,117,201,31))
        self.label_10.setObjectName("label_10")
        self.label_10.setStyleSheet("color : red")
        self.label_10.setFont(font_2)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(180,187,201,31))
        self.label_11.setObjectName("label_11")
        self.label_11.setStyleSheet("color : red")
        self.label_11.setFont(font_2)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(180,257,201,31))
        self.label_12.setObjectName("label_12")
        self.label_12.setStyleSheet("color : red")
        self.label_12.setFont(font_2)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(180,327,201,31))
        self.label_13.setObjectName("label_13")
        self.label_13.setStyleSheet("color : red")
        self.label_13.setFont(font_2)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(180,397,201,31))
        self.label_14.setObjectName("label_15")
        self.label_14.setStyleSheet("color : red")
        self.label_14.setFont(font_2)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(180,467,201,31))
        self.label_15.setObjectName("label_15")
        self.label_15.setStyleSheet("color : red")
        self.label_15.setFont(font_2)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(180,537,201,31))
        self.label_16.setObjectName("label_16")
        self.label_16.setStyleSheet("color : red")
        self.label_16.setFont(font_2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180,70,300,41))
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(180,140,300,41))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(180,210,300,41))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(180,280,300,41))
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(180,350,300,41))
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(180,420,300,41))
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(180,490,300,41))
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.pushButton= QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200,570,191,51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFont(font)
        
        
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
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.pushButton.clicked.connect(self.lire)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow","CIN : "))
        self.label.adjustSize()
        self.label_9.setText(_translate("MainWindow","Ajouter un client "))
        self.label_9.adjustSize()
        self.label_2.setText(_translate("MainWindow","Nom : "))
        self.label_2.adjustSize()
        self.label_3.setText(_translate("MainWindow","Prenom : "))
        self.label_3.adjustSize()
        self.label_4.setText(_translate("MainWindow","Age : "))
        self.label_4.adjustSize()
        self.label_5.setText(_translate("MainWindow","Adresse : "))
        self.label_5.adjustSize()
        self.label_6.setText(_translate("MainWindow","Mail : "))
        self.label_6.adjustSize()
        self.label_7.setText(_translate("MainWindow","Telephone : "))
        self.label_7.adjustSize()
        self.label_10.setText(_translate("MainWindow",""))
        self.label_10.adjustSize()
        self.label_11.setText(_translate("MainWindow",""))
        self.label_11.adjustSize()
        self.label_12.setText(_translate("MainWindow",""))
        self.label_12.adjustSize()
        self.label_13.setText(_translate("MainWindow",""))
        self.label_13.adjustSize()
        self.label_14.setText(_translate("MainWindow",""))
        self.label_14.adjustSize()
        self.label_15.setText(_translate("MainWindow",""))
        self.label_15.adjustSize()
        self.label_16.setText(_translate("MainWindow",""))
        self.label_16.adjustSize()
     
        self.pushButton.setText(_translate("MainWindow","ajouter"))
        
    def lire(self):
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
        box=0
        l1=['0','1','2']
        l2=['2','9','5']
        l3=['@yahoo.com','@gmail.com'];ad1='@hotmail.fr';ad2='@hotmail.com'
        if ((self.lineEdit.text().isnumeric()==False)or(len(self.lineEdit.text())!=8) or (self.lineEdit.text()=='00000000') or((self.lineEdit.text()[0] in l1)==False)):
            self.label_10.setText("CIN invalide")
            self.label_10.adjustSize()
        
        elif ((self.lineEdit.text() in cle)==True):
            self.label_10.setText("")
            self.label_10.adjustSize()
            msg=QMessageBox()
            msg.setWindowTitle("existant")
            msg.setText("CIN existe déja !")
            x=msg.exec_()
            box=1
        else:
            self.label_10.setText("")
            self.label_10.adjustSize()
        if(self.lineEdit_2.text().isalpha()==False):
            self.label_11.setText("Nom invalide")
            self.label_11.adjustSize()
        elif(self.lineEdit_2.text()[0].isupper()==False):
            self.label_11.setText("Le nom doit commencer par une majuscule ")
            self.label_11.adjustSize()
        else:
            self.label_11.setText("")
            self.label_11.adjustSize()
        if(self.lineEdit_3.text().isalpha()==False):
            self.label_12.setText("Prenom invalide")
            self.label_12.adjustSize()
        elif(self.lineEdit_3.text()[0].isupper()==False):
            self.label_12.setText("Le prenom doit commencer par une majuscule ")
            self.label_12.adjustSize()
        else:
            self.label_12.setText("")
            self.label_12.adjustSize()
        if ((self.lineEdit_4.text().isnumeric()==False)or(len(self.lineEdit_4.text())!=2) ):
            self.label_13.setText("Age invalide")
            self.label_13.adjustSize()
        
        elif ((int(self.lineEdit_4.text()))<18):
            self.label_13.setText("L'age doit etre superieur à 18 ")
            self.label_13.adjustSize()
            
        else:
            self.label_13.setText("")
            self.label_13.adjustSize()
            
        if(self.lineEdit_5.text().isalpha()==False):
            self.label_14.setText("Adresse invalide")
            self.label_14.adjustSize()
        elif(self.lineEdit_5.text()[0].isupper()==False):
            self.label_14.setText("L'adresse doit commencer par une majuscule ")
            self.label_14.adjustSize()
        else:
            self.label_14.setText("")
            self.label_14.adjustSize()
        if(len(self.lineEdit_6.text())<15):
            self.label_15.setText("Adresse mail invalide")
            self.label_15.adjustSize()
        elif(((self.lineEdit_6.text()[-10:] )in l3 ==False)):
            if(self.lineEdit_6.text()[-11:]!=ad1):
                if(self.lineEdit_6.text()[-12:]!=ad2):
                    self.label_15.setText("Adresse mail invalide")
                    self.label_15.adjustSize()
        else:
            self.label_15.setText("")
            self.label_15.adjustSize()
            
        if ((self.lineEdit_7.text().isnumeric()==False)or(len(self.lineEdit_7.text())!=8) or((self.lineEdit_7.text()[0] in l2)==False)):
            self.label_16.setText("Numero invalide")
            self.label_16.adjustSize()
        else:
            self.label_16.setText("")
            self.label_16.adjustSize()
           
        if((box==0)and(self.label_10.text()=="")and(self.label_11.text()=="")and(self.label_12.text()=="")and(self.label_13.text()=="")and(self.label_14.text()=="")and(self.label_15.text()=="")and(self.label_16.text()=="")):
            dc[self.lineEdit.text()]=[self.lineEdit_2.text(),self.lineEdit_3.text(),self.lineEdit_4.text(),self.lineEdit_5.text(),self.lineEdit_6.text(),self.lineEdit_7.text()]
            msg=QMessageBox()
            msg.setWindowTitle("Succés")
            msg.setText("Client ajouté avec succés")
            x=msg.exec_()
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.lineEdit_7.clear()
            
            with open ('clients.txt','w') as f:
                for cle,valeur in dc.items():
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