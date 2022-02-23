#Importation des librairies
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#Chargement de l'image
# 1 pour couleur, 0 pour grayscale
image = cv.imread('LitiereColorer.jpg',1)
#Création d'une image pour pouvoir la modifier
OG_image = image.copy()

#Applique un filtre couleur sur l'image
hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_brown = np.array([10,100,100])
upper_brown = np.array([40,200,200])
# Threshold the HSV image to get only blue colors
mask = cv.inRange(hsv, lower_brown, upper_brown)
# Bitwise-AND mask and original image
res = cv.bitwise_and(image,image, mask= mask)

#Affiche les images
cv.imshow('Image OG', OG_image)
cv.imshow('Image Color', mask)
cv.waitKey(0)
cv.destroyAllWindows()