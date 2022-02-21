#Importation de librairies
import cv2 as cv
import os

PiCam = cv.VideoCapture(0)
#Vérifie la connection
if not PiCam.isOpened():
    print("Problème avec la caméra")
    exit()

#Création de nos objets à ajouter dans la listes des objets
Labels = ["LitierePropre","LitiereSale"]
#Création des fichier pour stocker les images
for label in Labels:
    if not os.path.exists(label):
        os.mkdir(label)

# Prise de photos
for folder in Labels:
    #Nom de l'image avec le numero
    count = 0

    #Demande à l'utilisateur quand il est prêt
    print("Appuyer sur 's' pour débuter la prise de photo de "+folder)

    userinput = input()
    if userinput != 's':
        print("Wrong Input..........")
        exit()

    #Nombre d'image à prendre de l'objet    
    while count<200:
        #read returns two values one is the exit code and other is the frame
        status, frame = PiCam.read()

        #check if we get the frame or not
        if not status:
            print("Frame is not been captured..Exiting...")
            break

        #Convertion de l'image en noir et blanc pour une vitesse de calcul plus grand
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        #affichage de l'image
        cv.imshow("Video Window",gray)

        #Changement de taille de l'image pour l'enregistrement
        #gray = cv.resize(gray, (28,28))

        #Emplacement de la sauvegarde de l'image
        cv.imwrite('/home/pi/Documents/Cagius/Code/PiCamera/Object_Detection_Files/'+folder+'/img'+str(count)+'.png',gray)
        count=count+1

        #Pour quitter, appuyer sur 'q'
        if cv.waitKey(1) == ord('q'):
            break

# Libère la caméra quand tout est fini
PiCam.release()
cv.destroyAllWindows()        