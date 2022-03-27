import cv2 as cv
import numpy as np

#Chemin pour la sauvegarde de l'image

cam = cv.VideoCapture(0)

for index in range(0,1):
    print(str(index) + ": Prise de photo dans 3 seconde")
    cv.waitKey(3000)

    result, image = cam.read()

    filename = 'Vert' + str(index) + '.jpg'
    print(filename)
    if result:
    
        # show the image
        #cv.imshow("Pattern", image)
    
        # save the image
        cv.imwrite(filename, image)
        
cv.destroyAllWindows()