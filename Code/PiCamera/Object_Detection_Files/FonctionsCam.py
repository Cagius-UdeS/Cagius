#Ce fichier contient toute les fonctions nécéssaire pour la caméra 

from cmath import inf
import cv2 as cv
import numpy as np
import RPi.GPIO as GPIO


LED = 11
# Une classe qui permet de stocker les informations des zones souillées.
class Zone :
     
   
    # Une méthode utilisée pour créer l'objet (Contructor).
    def __init__(self, largeur, hauteur, centreX, centreY):
        
        self.largeur= largeur
        self.hauteur = hauteur
        self.centreX = centreX
        self.centreY = centreY
   
    
    
    def getLargeur(self):        
        return self.largeur
    
    
    def getHauteur(self):        
        return self.hauteur

    def getCentreX(self):
        return self.centreX
    
    def getCentreY(self):
        return self.centreY

#Initialisation GPIO
def InitGPIO():
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(LED, GPIO.OUT)

# Définition permet de coriger le fisheye de la caméra
def undistort(img):
    DIM=(640, 480)
    K=np.array([[256.5223090219522, 0.0, 300.8492878302576], [0.0, 255.95393505302218, 200.83738221162403], [0.0, 0.0, 1.0]])
    D=np.array([[-0.03309970266931218], [-0.035713407140983686], [0.03466182058100104], [-0.014366025635664394]])
    #img = cv.imread(img_path)
    h,w = img.shape[:2]
    map1, map2 = cv.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv.CV_16SC2)
    undistorted_img = cv.remap(img, map1, map2, interpolation=cv.INTER_LINEAR, borderMode=cv.BORDER_CONSTANT)
    #cv.imshow("undistorted", undistorted_img)
    #cv.waitKey(0)
    #cv.destroyAllWindows()
    return undistorted_img

#Trouver toute les zones qui dépasse un aire minimum
def findZones(contours,LimiteAireMin,LimiteAireMax,image):
  Liste = []
  for c in contours:
    Aire = cv.contourArea(c)
    # print(Aire) #Débug
    #Trouve le centre et le contour des zones souillées et les affiche sur l'image
    if (Aire > LimiteAireMin) & (Aire < LimiteAireMax):
      x,y,h,w = cv.boundingRect(c)
      #Ajoute la position dans la liste
      Z = Zone(w, h, x+(w//2), y+(h//2))
      Liste.append(Z)

      #Affiche les zones sur l'image
      cv.rectangle(image, (x, y), (x+w, y+h),(0,255,0),5)
      cv.circle(image,(x+(w//2),y+(h//2)),1,(0,0,255),10)
  return Liste

def Scan():
  print("Scan en cour...")
  "Ouverture des LED:"
  GPIO.output(LED, GPIO.HIGH)
  "Variables:"
  #Assignation de la caméra pi
  #cam = cv.VideoCapture(0)

  # Définie la couleur à trouvé en HSV pour les zones souillées
  lower_brown = np.array([10,100,100])
  upper_brown = np.array([40,200,200])

  # Définie la couleur rouge à trouvé en HSV pour les ancrages
  lower_red = np.array([160,50,50])
  upper_red = np.array([180,255,255])

  # Définie la couleur bleu à trouvé en HSV pour les lapins
  lower_blue = np.array([110,200,0])
  upper_blue = np.array([130,255,100])


  "Démarage du scan de l'image"
  #Code pour tests sans cam
  im = cv.imread("Rouge0.jpg",1)
  im = undistort(im)

  """ #Prise de la photo de la litière
  result, image = cam.read()
  #Corection du fishEye
  im = undistort(image)
  #Nom de l'image
  filename = 'Litiere' + '.jpg'

  # Enregistrement de l'image pour observation
  cv.imwrite(filename, im) """

  "Fermeture des LED:"
  #GPIO.output(LED, GPIO.LOW)

  #Application de filtre sur l'image pour facilité la recherche de zones souillées
  #image = cv.GaussianBlur(im, (5,5),1)
  #image = cv.medianBlur(im,5)
  #kernel = np.ones((5,5),np.float32)/25
  #image = cv.filter2D(im,-1,kernel)

  #Applique un filtre couleur sur l'image
  hsv = cv.cvtColor(im, cv.COLOR_BGR2HSV)

  # Créer les images en binaire sur les couleurs recherchés
  # maskSouille = cv.inRange(hsv, lower_brown, upper_brown)
  maskAncrage = cv.inRange(hsv, lower_red, upper_red)
  maskLapin = cv.inRange(hsv, lower_blue, upper_blue)

  #Trouve les contours dans les masks
  # contoursSouille, hierarchy = cv.findContours(maskSouille, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
  contoursAncrage, hierarchy = cv.findContours(maskAncrage, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
  contoursLapin, hierarchy = cv.findContours(maskLapin, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

  #Trouver toute les zones souilées qui dépasse un aire minimum
  # ListeSouille = findZones(contoursSouille,1000,inf,im)

  #Trouver toute les Ancrages qui dépasse un aire minimum
  ListeAncrage = findZones(contoursAncrage,300,500,im)

  #Trouver toute les Ancrages qui dépasse un aire minimum
  ListeLapin = findZones(contoursLapin,100,800,im)

  "Calcul du nombre de lapin dans la cage"
  nbrLapin = len(ListeLapin)

  "Calcul du pourcentage(%) à vider"
  #Initialise la valeux de la distance du convoyeur
  Xmax = 0
  #Affiche les zones souillées et calcul la plus loin de la poubelle
  # for z in ListeSouille:
  #   if z.getCentreX() > Xmax:
  #     Xmax = z.getCentreX()
  #   print('CentreX : {}, CentreY : {}'.format(z.getCentreX(),z.getCentreY()))

  XAncrage = 0
  for z in ListeAncrage:
    if z.getCentreX() > XAncrage:
      XAncrage = z.getCentreX()
    print('CentreX : {}, CentreY : {}'.format(z.getCentreX(),z.getCentreY()))
  

  #Affiche la zone la plus loin de la poubelle
  print('Xmax : {}'.format(Xmax))
  Pourcentage = 25
  #Pourcentage = Xmax/XAncrage *100
  
  #Affiche les images pour débugage
  cv.imshow('Image Color', maskAncrage)
  cv.imshow('Image HSV', hsv)
  cv.imshow('Image Contour', im)
  cv.waitKey(0)
  cv.destroyAllWindows()
  "Fermeture des LED:"
  GPIO.output(LED, GPIO.LOW)
  print("Scan terminé!")
  "Retourne la valeur en % à vider"
  return Pourcentage,nbrLapin