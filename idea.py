d={}
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(150, 76, 170, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162,80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));\n"
#"")
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0552764 rgba(0, 85, 127, 206), stop:0.351759 rgba(170, 170, 255, 80), stop:0.4 rgba(170, 170, 255, 80), stop:0.44 rgba(170, 170, 255, 80), stop:0.447236 rgba(170, 170, 255, 80), stop:1 rgba(255, 255, 255, 0));\n"
"")
        #MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.09, y1:0.0855455, x2:1, y2:1, stop:0.135678 rgba(7, 33, 181, 206), stop:0.351759 rgba(85, 0, 255, 80), stop:0.376884 rgba(170, 170, 255, 80), stop:0.452261 rgba(119, 119, 255, 80), stop:0.603015 rgba(85, 170, 255, 80), stop:0.723618 rgba(170, 170, 255, 80), stop:1 rgba(255, 126, 182, 0));;\n"
#"")

        font_3 = QtGui.QFont()
        font_3.setPointSize(23)
        font = QtGui.QFont()
        font.setPointSize(14)
        font_2 = QtGui.QFont()
        font_2.setPointSize(9)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(250,10,411,41))
        self.label_9.setFont(font_3)
        self.label_9.setObjectName("label_9")
        self.label_9.setStyleSheet("color : pink")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50,80,201,31))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color : white")
        
        #self.label.setStyleSheet("color : white")
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
        self.label_7.setGeometry(QtCore.QRect(570,84,201,31))
        self.label_7.setObjectName("label_7")
        self.label_7.setStyleSheet("color : red")
        self.label_7.setFont(font_2)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(570,434,201,31))
        self.label_8.setObjectName("label_8")
        self.label_8.setStyleSheet("color : red")
        self.label_8.setFont(font_2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250,70,300,41))
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setGeometry(QtCore.QRect(250,140,300,41))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setGeometry(QtCore.QRect(250,210,300,41))
        self.comboBox_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")

        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setFont(font)
        self.comboBox.setGeometry(QtCore.QRect(250,280,300,41))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")

        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(250,350,300,41))
        self.dateEdit.setStyleSheet("")
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250,420,300,41))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")

        self.pushButton= QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300,510,191,51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")

        #self.pushButton_2= QtWidgets.QPushButton(self.centralwidget)
        #self.pushButton_2.setGeometry(QtCore.QRect(500,500,191,51))
        #self.pushButton_2.setObjectName("pushButton_2")
        #self.pushButton_2.setFont(font)
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
        #self.pushButton_2.clicked.connect(lambda:MainWindow.close()) #function binded to the button self.b1
        #MainWindow.setCentralWidget(self.pushButton_2)
        
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow","La matricule : "))
        self.label.adjustSize()
        self.label_9.setText(_translate("MainWindow","Ajouter une voiture "))
        self.label_9.adjustSize()
        self.label_2.setText(_translate("MainWindow","La marque : "))
        self.label_2.adjustSize() 
        self.label_3.setText(_translate("MainWindow","La couleur : "))
        self.label_3.adjustSize()
        self.label_4.setText(_translate("MainWindow","L'etat : "))
        self.label_4.adjustSize()
        self.label_5.setText(_translate("MainWindow","La date d'achat : "))
        self.label_5.adjustSize()
        self.label_6.setText(_translate("MainWindow","Le prix de location : "))
        self.label_6.adjustSize()
        self.label_7.setText(_translate("MainWindow",""))
        self.label_7.adjustSize()
        self.label_8.setText(_translate("MainWindow",""))
        self.label_8.adjustSize()
        self.comboBox.setItemText(0, _translate("Form", "Disponible"))
        self.comboBox.setItemText(1, _translate("Form", "Louée"))
        self.comboBox_2.setItemText(0, _translate("Form", "Astra"))
        self.comboBox_2.setItemText(1, _translate("Form", "Audi"))
        self.comboBox_2.setItemText(2, _translate("Form", "BMW"))
        self.comboBox_2.setItemText(3, _translate("Form", "Citroen"))
        self.comboBox_2.setItemText(4, _translate("Form", "Fiat"))
        self.comboBox_2.setItemText(5, _translate("Form", "Golf"))
        self.comboBox_2.setItemText(6, _translate("Form", "Isuzu"))
        self.comboBox_2.setItemText(7, _translate("Form", "Kia"))
        self.comboBox_2.setItemText(8, _translate("Form", "Peugeot"))
        self.comboBox_2.setItemText(9, _translate("Form", "Rangerover"))
        self.comboBox_2.setItemText(10, _translate("Form", "Renault"))
        self.comboBox_2.setItemText(11, _translate("Form", "Volkswagen"))
        
        self.comboBox_3.setItemText(0, _translate("Form", "Blanc"))
        self.comboBox_3.setItemText(1, _translate("Form", "Bleu"))
        self.comboBox_3.setItemText(2, _translate("Form", "Gris"))
        self.comboBox_3.setItemText(3, _translate("Form", "Noir"))
        self.comboBox_3.setItemText(4, _translate("Form", "Marron"))
        self.comboBox_3.setItemText(5, _translate("Form", "Rose"))
        self.comboBox_3.setItemText(6, _translate("Form", "Rouge"))
        self.comboBox_3.setItemText(7, _translate("Form", "Vert"))
        self.comboBox_3.setItemText(8, _translate("Form", "Violet"))
        self.pushButton.setText(_translate("MainWindow","ajouter"))
        #self.pushButton_2.setText(_translate("MainWindow","quitter"))
        
    def lire(self):
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
        mat1=self.lineEdit.text()[0:3]
        mat2=self.lineEdit.text()[3:5]
        mat3=self.lineEdit.text()[5:]
        if ((len(self.lineEdit.text())!=9)or(mat1.isnumeric()==False)or(mat3.isnumeric()==False)or(mat2!="tu" ) ):
            self.label_7.setText("Matricule invalide")
            self.label_7.adjustSize()
        elif ((self.lineEdit.text() in cle)==True):
            self.label_7.setText("")
            self.label_7.adjustSize()
            msg=QMessageBox()
            msg.setWindowTitle("existant")
            msg.setText("Cette matricule existe déja !")
            x=msg.exec_()
            box=1
        else:
            self.label_7.setText("")
            self.label_7.adjustSize()
        liste=['0','1','2','3','4','5','6','7','8','9']
        if ((self.lineEdit_2.text().isnumeric()==False)or((self.lineEdit_2.text()in liste)==True)  ):
            self.label_8.setText("Prix invalide")
            self.label_8.adjustSize()
        else:
            self.label_8.setText("")
            self.label_8.adjustSize()
        tm=self.dateEdit.date()
        var=tm.toPyDate()
        var=str(var)
        if ((self.label_7.text()=="")and(self.label_8.text()=="")and(box==0)):
            d[self.lineEdit.text()]=[self.comboBox_2.currentText(),self.comboBox_3.currentText(),self.comboBox.currentText(),var,self.lineEdit_2.text()]
            msg=QMessageBox()
            msg.setWindowTitle("Succés")
            msg.setText("Voiture ajoutée avec succés")
            x=msg.exec_()
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            
            

        with open ('voitures.txt','w') as f:
            for cle,valeur in d.items():
                f.write(cle+" ")
                f.write(valeur[0]+" ")
                f.write(valeur[1]+" ")
                f.write(valeur[2]+" ")
                f.write(valeur[3]+" ")
                f.write(valeur[4]+'\n')
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())