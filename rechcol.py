from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400,350 )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0552764 rgba(0, 85, 127, 206), stop:0.351759 rgba(170, 170, 255, 80), stop:0.4 rgba(170, 170, 255, 80), stop:0.44 rgba(170, 170, 255, 80), stop:0.447236 rgba(170, 170, 255, 80), stop:1 rgba(255, 255, 255, 0));\n"
"")
        font = QtGui.QFont()
        font.setPointSize(16)
        font_3 = QtGui.QFont()
        font_3.setPointSize(20)
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
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setGeometry(QtCore.QRect(100,140,211,51))
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
        
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
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
        self.label.setText(_translate("MainWindow","Couleur : "))
        self.label.adjustSize()
        self.label_3.setText(_translate("MainWindow","Recherche d'une voiture"))
        self.label_3.adjustSize()
        self.comboBox_2.setItemText(0, _translate("Form", "Blanc"))
        self.comboBox_2.setItemText(1, _translate("Form", "Bleu"))
        self.comboBox_2.setItemText(2, _translate("Form", "Gris"))
        self.comboBox_2.setItemText(3, _translate("Form", "Noir"))
        self.comboBox_2.setItemText(4, _translate("Form", "Marron"))
        self.comboBox_2.setItemText(5, _translate("Form", "Rose"))
        self.comboBox_2.setItemText(6, _translate("Form", "Rouge"))
        self.comboBox_2.setItemText(7, _translate("Form", "Vert"))
        self.comboBox_2.setItemText(8, _translate("Form", "Violet"))
        self.pushButton.setText(_translate("MainWindow","rechercher"))
        
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
        s=[]
        for cle,valeur in d.items():
            if (valeur[1]==self.comboBox_2.currentText()):
                s.append(cle)
        if(len(s)==0):
            msg=QMessageBox()
            msg.setWindowTitle("Erreur")
            msg.setText("couleur introuvable")
            x=msg.exec_()
        else:
            with open ('enregistrer.txt','w') as f:
                f.write(self.comboBox_2.currentText())
            from subprocess import call
            call(["python", "rechcolo.py"])   
        
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())