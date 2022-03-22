import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5           import *

from mainWindow_geometry import Ui_MainWindow
from popup_geometry      import Ui_Dialog
from commFunctions       import *

ID_OPENCR = 1;

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.Fait.clicked.connect(self.change)


    def change(self):
        self.close()
        self.myWindow = MyWindow()
        self.myWindow.show()


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.messageIO = MessageIO()
        self.messageIO.addDevice(SerialComm("/dev/ttyACM0", 57600))

        ##Initialisation de la fenêtre principale
        self.initAnimals()
        self.commWindows()
        self.setActivityHours()
        
        #Fonctions de communication
        self.numAnimals()
        self.buttonactiveCage()
        self.buttonstopCage()


    def buttonactiveCage(self):
        self.ui.Activation.clicked.connect(self.activeCage)
        self.ui.Nettoyage.clicked.connect(self.activeCage)

    
    def activeCage(self):
        ##Activer les moteurs et attendre fin de mouvement
        self.messageIO.sendMessage(ID_OPENCR,"0START")
        self.messageIO.readMessage(ID_OPENCR)
        print('Cage en mouvement')

    def buttonstopCage(self):
        self.ui.Desactivation.clicked.connect(self.stopCage)

    
    def stopCage(self):
        ##Arreter les moteurs et attendre fin de mouvement
        print('Cage en cours darret')


    def initAnimals(self):
        self.ui.Animal1.setChecked(0)
        self.ui.Animal2.setChecked(0)
        self.ui.Animal3.setChecked(0)

    def numAnimals(self):
        if True :
            self.ui.Animal1.setChecked(0)
        if True :
            self.ui.Animal2.setChecked(1)
        if True :
            self.ui.Animal3.setChecked(0)


    def commWindows(self):
        #self.ui.Nettoyage.clicked.connect(self.dialogbox)
        self.ui.Viderpoubelle.clicked.connect(self.dialogbox)


    def dialogbox(self):
        self.hide()
        self.myDialog = MyDialog()
        self.myDialog.show()


    def setActivityHours(self):
        timeD = QTime()
        timeD.setHMS(8,00,00)
        self.ui.Debut.setTime(timeD)
        timeF = QTime()
        timeF.setHMS(20,00,00)
        self.ui.Fin.setTime(timeF)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())