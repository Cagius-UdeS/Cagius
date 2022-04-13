import sys

from matplotlib import animation

sys.path.insert(0, '/home/pi/Documents/Cagius/Code/Main')
import init_stop_Sequences as iss

import threading
import time
import serial
import datetime as dt

from glob            import glob
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5           import *

from mainWindow_geometry           import Ui_MainWindow
from popup_geometry                import Ui_Dialog

""" Counter of the number of cleaning cycles
"""
COMPTEUR = 0

""" Variable of the number of animals set
"""
ANIMAUX = 0

""" Boolean confirming the cage is ready to start
"""
AUTO = False

""" Start of the activity hours
"""
DEBUT = 0

""" End of the activity hours
"""
FIN = 0

""" Value of the quantity of ... to trash (1, 2, 3)
"""
POURCENTAGE = 0



# Class defining the pop-up window object
class MyDialog(QDialog):
    def __init__(self):
        """ Initialization of the window

        Call communication between windows function in loop
        """

        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


        self.ui.Fait.clicked.connect(self.change)


    def change(self):
        """ Function for transition between pop-up window and main window

        Close pop-up window and open the main one
        Put the counter variable at 0
        """

        self.close()
        #self.mywindow = MyWindow.__new__(MyWindow)
        #self.mywindow.show()

        
        global COMPTEUR
        COMPTEUR = 0
        print("Réinistialisation du compteur\n")


# Class defining the main window object
class MyWindow(QMainWindow):
    def __init__(self):
        """ Initialization of the window

        Initialize the communication between Pi and other composants
        Initialize the variable in the windows
        Call communication between windows and componants functions in loop
        """

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

        port, ser = iss.init_sequence()
        
        
        # self.initAnimals()
        self.commWindows(ser)
        self.getActivityHours()
        self.numAnimals()
        self.buttonstartCage(ser)
        self.buttonactiveCage(ser)
        self.buttonclean(ser)
        self.buttonstopCage(ser)
        self.buttontrash(ser)

    def buttonstartCage(self, ser):
        """ Actions tied to the Lancement button
        """

        self.ui.Lancement.clicked.connect(lambda:self.startCage(ser))

    
    def startCage(self, ser):
        """ Get the cage in the starting state
        """

        #iss.start_state(ser)
        self.numAnimals()
        self.getActivityHours()
        print("Les heures d'activités et le nombre d'animaux sont enregistrés")


    def buttonactiveCage(self, ser):
        """ Actions tied to the Activation button
        """

        self.ui.Activation.clicked.connect(lambda:self.activeCage(ser))

    
    def activeCage(self, ser):
        """ Get the cage in the activated state
        """

        global AUTO
        AUTO = iss.activate_state(ser)


    def buttonstopCage(self, ser):
        """ Actions tied to the Desactivation button
        """

        self.ui.Desactivation.clicked.connect(lambda:self.stopCage(ser))

    
    def stopCage(self, ser):
        """ Get the cage in the stop state
        """

        iss.stop_state(ser)

        global AUTO
        AUTO = False

    
    def buttontrash(self, ser):
        """ Actions tied to the Viderpoubelle button
        """

        self.ui.Viderpoubelle.clicked.connect(lambda:self.trashCage(ser))


    def trashCage(self, ser):
        """ Get the cage in the trash state

        Call function opening the pop-up window
        """

        self.dialogbox
        iss.trash_state(ser)


    def buttonclean(self, ser):
        """ Actions tied to the Nettoyage button
        """

        self.ui.Nettoyage.clicked.connect(lambda:self.cleanCage(ser))

    
    def cleanCage(self, ser):
        """ Get the cage in the clean state

        Increment the counter variable and print it
        """

        global COMPTEUR, POURCENTAGE

        bool, POURCENTAGE = iss.clean_state(ser)

        COMPTEUR = COMPTEUR + POURCENTAGE/3
        print("Nettoyage numéro " + str(COMPTEUR) + "\n")

        lambda:self.commWindows(ser)


    # def initAnimals(self):
    #     """ Initialize the animals check-boxes
    #     """
    #     self.ui.Animal1.setChecked(0)
    #     self.ui.Animal2.setChecked(0)
    #     self.ui.Animal3.setChecked(0)


    def numAnimals(self):
        """ Get the number of animals set by the user
        """
        
        global ANIMAUX
        if self.ui.Animal3.isChecked():
            ANIMAUX = 3
        elif self.ui.Animal2.isChecked():
            ANIMAUX = 2
        elif self.ui.Animal1.isChecked():
            ANIMAUX = 1
        else:
            ANIMAUX = 0


    def commWindows(self, ser):
        """ Function opening the pop-up window when the counter COMPTEUR reach a certain value
        """

        global COMPTEUR
        if  COMPTEUR >= 3: 
            self.dialogbox
            print("Lancement de la vidange")
            #lambda:self.trashCage(ser)


    def dialogbox(self):
        """ Function for transition between main window and pop-up window

        Hide the main window and open the pop-up window
        """

        #self.hide()
        self.myDialog = MyDialog()
        self.myDialog.show()


    def getActivityHours(self):
        """ Get the activity hours set by the user

        Get starting time
        Get ending time
        """
        
        timeD = self.ui.Debut.time()
        timeF = self.ui.Fin.time()

        global DEBUT, FIN
        DEBUT = timeD.hour()
        FIN = timeF.hour()
        


def thread_function(name):
    """ Get the number of animals set by the user
    """

    ser = serial.Serial("/dev/ttyACM0", 57600)

    global ANIMAUX, AUTO, DEBUT, FIN, COMPTEUR
    VERIF = False

    while(True):

        DTime = dt.datetime.now().time()
        #print("L'heure actuelle est " + str(DTime.hour) + " et les intervalles sont " + str(DEBUT) + " et " + str(FIN))
        
        if(AUTO and DTime.hour >= DEBUT and DTime.hour <= FIN and not VERIF):
            
            bool, POURCENTAGE = iss.clean_state(ser)
            if(bool):
                VERIF = True

                COMPTEUR = COMPTEUR + POURCENTAGE/3
                print("Nettoyage numéro " + str(COMPTEUR) + "\n")
            else:
                time.sleep(15)    
        
        elif(DTime.hour <= DEBUT and DTime.hour >= FIN):
            VERIF = False
        
        time.sleep(1)
        
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    x = threading.Thread(target = thread_function, args =(1,), daemon=True)
    x.start()
    sys.exit(app.exec_())
