from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 572)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.09, y1:0.0855455, x2:1, y2:1, stop:0.135678 rgba(7, 33, 181, 206), stop:0.351759 rgba(85, 0, 255, 80), stop:0.376884 rgba(170, 170, 255, 80), stop:0.452261 rgba(119, 119, 255, 80), stop:0.603015 rgba(85, 170, 255, 80), stop:0.723618 rgba(170, 170, 255, 80), stop:1 rgba(255, 126, 182, 0));;\n"
#"")
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0552764 rgba(0, 85, 127, 206), stop:0.351759 rgba(170, 170, 255, 80), stop:0.4 rgba(170, 170, 255, 80), stop:0.44 rgba(170, 170, 255, 80), stop:0.447236 rgba(170, 170, 255, 80), stop:1 rgba(255, 255, 255, 0));\n"
"")
        #MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(150, 76, 170, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162,80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));\n"
#"")
        font_3 = QtGui.QFont()
        font_3.setPointSize(20)
        font_2 = QtGui.QFont()
        font_2.setPointSize(9)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50,30,411,41))
        self.label_3.setFont(font_3)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("color : pink")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180,100,411,41))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color : white")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140,140,211,61))
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setGeometry(QtCore.QRect(140,280,211,61))
        self.comboBox_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")

        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(125,240,411,41))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("color : white")
        
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(140,210,211,61))
        self.label_7.setObjectName("label_7")
        self.label_7.setStyleSheet("color : red")
        self.label_7.setFont(font_2)
        self.pushButton= QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150,430,201,61))
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
        self.label.setText(_translate("MainWindow","Matricule"))
        self.label.adjustSize()
        self.label_2.setText(_translate("MainWindow","Etat  "))
        self.label_2.adjustSize()
        self.label_3.setText(_translate("MainWindow","Modfier l'état d'une voiture "))
        self.label_3.adjustSize()
        self.label_7.setText(_translate("MainWindow",""))
        self.label_7.adjustSize()
        self.comboBox_3.setItemText(0, _translate("Form", "Disponible"))
        self.comboBox_3.setItemText(1, _translate("Form", "Louée"))
        self.pushButton.setText(_translate("MainWindow","Modifier"))
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
        mat1=self.lineEdit.text()[0:3]
        mat2=self.lineEdit.text()[3:5]
        mat3=self.lineEdit.text()[5:]
        if ((len(self.lineEdit.text())!=9)or(mat1.isnumeric()==False)or(mat3.isnumeric()==False)or(mat2!="tu" ) ):
            self.label_7.setText("Matricule invalide")
            self.label_7.adjustSize()
            
        else:
            self.label_7.setText("")
            self.label_7.adjustSize()
        cle=list(d.keys())
        if(((self.lineEdit.text() in cle)==False)and(self.label_7.text()=="")):
            msg=QMessageBox()
            msg.setWindowTitle("Erreur")
            msg.setText("Matricule introuvable")
            x=msg.exec_()
            
        if ((self.label_7.text()=="")and((self.lineEdit.text() in cle)==True)):
            
            for c,v in d.items():
                if (c==self.lineEdit.text()):
                    v[2]=self.comboBox_3.currentText()
           
            msg=QMessageBox()
            msg.setWindowTitle("Succés")
            msg.setText("Modification effectuée avec succés")
            x=msg.exec_()
            
        with open ('voitures.txt','w') as f:
            for c,valeur in d.items():
                f.write(c+" ")
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
