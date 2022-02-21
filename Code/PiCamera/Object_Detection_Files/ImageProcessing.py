#Importation des librairies
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#Chargement de l'image
# 1 pour couleur, 0 pour grayscale
image = cv.imread('LitiereSouiller.jpg',1)
#Création d'une image pour pouvoir la modifier
OG_image = image

#Applique un filtre couleur sur l'image
ModifImage = cv.applyColorMap(image,cv.COLORMAP_PARULA)






#Affiche les images
cv.imshow('Image OG', OG_image)
cv.imshow('Image Color', ModifImage)
cv.waitKey(0)
cv.destroyAllWindows()