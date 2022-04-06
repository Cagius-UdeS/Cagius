import sys
from glob            import glob
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5           import *

from mainWindow_geometry import Ui_MainWindow
from popup_geometry      import Ui_Dialog
from functions           import *
from init_stop_Cmds      import *

COMPTEUR = 0

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.Fait.clicked.connect(self.change)


    def change(self):
        self.close()
        self.mywindow = MyWindow.__new__(MyWindow)
        self.mywindow.show()
        
        global COMPTEUR
        COMPTEUR = 0
        print("Réinistialisation du compteur\n")


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


    
    def activeCage(self, ser):
        activate_state(ser)


    def buttonstopCage(self, ser):
        self.ui.Desactivation.clicked.connect(lambda:self.stopCage(ser))

    
    def stopCage(self, ser):
        stop_state(ser)

    
    def buttontrash(self, ser):
        self.ui.Viderpoubelle.clicked.connect(lambda:self.trashCage(ser))


    def trashCage(self, ser):
        trash_state(ser)

        """global COMPTEUR
        if  COMPTEUR >= 7: 
            self.dialogbox
            print("Lancement de la vidange")
            lambda:self.trashCage(ser)"""


    def buttonclean(self, ser):
        self.ui.Nettoyage.clicked.connect(lambda:self.cleanCage(ser))

    
    def cleanCage(self, ser):
        clean_state(ser)

        global COMPTEUR
        COMPTEUR = COMPTEUR + 1
        print("Nettoyage numéro " + str(COMPTEUR) + "\n")


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