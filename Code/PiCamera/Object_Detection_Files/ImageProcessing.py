#Importation des librairies
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#Chargement de l'image
# 1 pour couleur, 0 pour grayscale
image = cv.imread('LitiereColorer.jpg',1)
#Création d'une image pour pouvoir la modifier
OG_image = image.copy()

#Application de filtre sur l'image pour facilité la recherche de zones souillées
image = cv.GaussianBlur(image, (5,5),1)
#image = cv.medianBlur(image,5)
kernel = np.ones((5,5),np.float32)/25
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

maxC = max(contours, key = cv.contourArea)


#Trouver toute les zones souilées qui dépasse un aire minimum
for c in contours:
    area = cv.contourArea(c)
    
    #Trouve le centre et le contour des zones souillées et les affiche sur l'image
    if area > 1000:
        x,y,h,w = cv.boundingRect(c)
        cv.rectangle(image, (x, y), (x+w, y+h),(0,255,0),5)
        cv.circle(image,(x+(w//2),y+(h//2)),1,(0,0,255),10)

#Affiche les images
cv.imshow('Image OG', OG_image)
cv.imshow('Image Color', mask)
cv.imshow('Image Contour', image)
cv.waitKey(0)
cv.destroyAllWindows()