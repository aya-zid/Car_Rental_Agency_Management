from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
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
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30,20,201,31))
        self.label_2.setFont(font_3)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("color : pink")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90,100,500,23))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color : white")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80,150,211,51))
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80,210,300,41))
        self.label_3.setFont(font_2)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("color : red")
        self.pushButton= QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120,250,141,81))
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
        self.label_3.setText(_translate("MainWindow",""))
        self.label_3.adjustSize()
        self.label_2.setText(_translate("MainWindow","Recherche d'une location"))
        self.label_2.adjustSize()
        self.pushButton.setText(_translate("MainWindow","rechercher"))
    def lire(self):
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
        l1=['0','1','2']
        if ((self.lineEdit.text().isnumeric()==False)or(len(self.lineEdit.text())!=8)or (self.lineEdit.text()=='00000000') or((self.lineEdit.text()[0] in l1)==False)  ):
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
            msg=QMessageBox()
            msg.setWindowTitle("Erreur")
            msg.setText("CIN introuvable")
            x=msg.exec_()
        
        if ((self.lineEdit.text() in cle)==True):
            for c,valeur in dl.items():
                if (c[0]==self.lineEdit.text()):
                    with open ('enregistrer.txt','w') as f:
                        f.write(self.lineEdit.text())
            from subprocess import call
            call(["python", "rechcinlo.py"])
            
        
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())