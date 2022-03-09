#Importation des librairies
from cmath import inf
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from ZoneInfo import Zone

#Chargement de l'image
# 1 pour couleur, 0 pour grayscale
image = cv.imread('LitiereColorer.jpg',1)
#Création d'une image pour pouvoir la modifier
OG_image = image.copy()

#Application de filtre sur l'image pour facilité la recherche de zones souillées
image = cv.GaussianBlur(image, (5,5),1)
#image = cv.medianBlur(image,5)
#kernel = np.ones((5,5),np.float32)/25
#image = cv.filter2D(image,-1,kernel)

#Applique un filtre couleur sur l'image
hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

# Définie la couleur à trouvé en HSV
lower_brown = np.array([10,100,100])
upper_brown = np.array([40,200,200])

# Créer l'image en binaire sur la couleur rechercher
mask = cv.inRange(hsv, lower_brown, upper_brown)

contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

#Affichage des contours
#cv.drawContours(image, contours, -1, (0,255,0), 3)

#maxC = max(contours, key = cv.contourArea)

ListeSouille = []
#Trouver toute les zones souilées qui dépasse un aire minimum
for c in contours:
    area = cv.contourArea(c)
    
    #Trouve le centre et le contour des zones souillées et les affiche sur l'image
    if area > 1000:
        x,y,h,w = cv.boundingRect(c)
        #Ajoute la position dans la liste
        Z = Zone(w, h, x+(w//2), y+(h//2))
        ListeSouille.append(Z)

        #Affiche les zones sur l'image
        cv.rectangle(image, (x, y), (x+w, y+h),(0,255,0),5)
        cv.circle(image,(x+(w//2),y+(h//2)),1,(0,0,255),10)

#Initialise la valeux de la distance du convoyeur
Xmax = 0
#Affiche les zones souillées
for z in ListeSouille:
    if z.getCentreX() > Xmax:
        Xmax = z.getCentreX()

    print('CentreX : {}, CentreY : {}'.format(z.getCentreX(),z.getCentreY()))

#Affiche la zone la plus loin de la poubelle
print('Xmax : {}'.format(Xmax))

#Affiche les images
cv.imshow('Image OG', OG_image)
cv.imshow('Image Color', mask)
cv.imshow('Image Contour', image)
cv.waitKey(0)
cv.destroyAllWindows()