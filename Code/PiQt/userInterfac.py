from distutils.command.clean import clean
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5           import *

from mainWindow_geometry import Ui_MainWindow
from popup_geometry      import Ui_Dialog
from functions           import *
from init_stop_Cmds      import *


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
        
        
        #Initialisation de la commuication
        port, ser = init_sequence()
        

        ##Initialisation de la fenêtre principale
        self.initAnimals()
        self.commWindows()
        self.setActivityHours()
        
        
        #Fonctions de communication
        self.numAnimals()
        self.buttonactiveCage(ser)
        self.buttonclean(ser)
        self.buttonstopCage(ser)
        self.buttontrash(ser)


    def buttonactiveCage(self, ser):
        self.ui.Activation.clicked.connect(lambda:self.activeCage(ser))
        #self.ui.Nettoyage.clicked.connect(lambda:self.activeCage(ser))


    
    def activeCage(self, ser):
        ##Activer les moteurs et attendre fin de mouvement
        #print_sent_data(send_data(serial.Serial("/dev/ttyACM0", 57600), "START"))
        #print_received_data(get_data(serial.Serial("/dev/ttyACM0", 57600)))
        #print('Cage en mouvement')

        activate_state(ser)

    def buttonstopCage(self, ser):
        self.ui.Desactivation.clicked.connect(lambda:self.stopCage(ser))

    
    def stopCage(self, ser):
        ##Arreter les moteurs et attendre fin de mouvement
        #print('Cage en cours darret')

        stop_state(ser)

    
    def buttontrash(self, ser):
        self.ui.Viderpoubelle.clicked.connect(lambda:self.trashCage(ser))


    def trashCage(self, ser):
        trash_state(ser)


    def buttonclean(self, ser):
        self.ui.Nettoyage.clicked.connect(lambda:self.cleanCage(ser))

    
    def cleanCage(self, ser):
        clean_state(ser)


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