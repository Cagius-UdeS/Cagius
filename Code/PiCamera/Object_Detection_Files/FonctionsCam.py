#Ce fichier contient toute les fonctions nécéssaire pour la caméra 

from cmath import inf
import cv2 as cv
import numpy as np
import RPi.GPIO as GPIO
import time


LED = 11
# Une classe qui permet de stocker les informations des zones souillées.
class Zone :
     
   
    # Une méthode utilisée pour créer l'objet (Contructor).
    def __init__(self, largeur, hauteur, centreX, centreY, aire):
        
      self.largeur= largeur
      self.hauteur = hauteur
      self.centreX = centreX
      self.centreY = centreY
      self.aire    = aire
   
    
    
    def getLargeur(self):        
        return self.largeur
    
    
    def getHauteur(self):        
        return self.hauteur

    def getCentreX(self):
        return self.centreX
    
    def getCentreY(self):
        return self.centreY
    
    def getAire(self):
        return self.aire

#Initialisation GPIO
def InitGPIO():
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(LED, GPIO.OUT)
  GPIO.setwarnings(False)

# Définition permet de coriger le fisheye de la caméra
def undistort(img):
    DIM=(640, 480)
    K=np.array([[256.5223090219522, 0.0, 300.8492878302576], [0.0, 255.95393505302218, 200.83738221162403], [0.0, 0.0, 1.0]])
    D=np.array([[-0.03309970266931218], [-0.035713407140983686], [0.03466182058100104], [-0.014366025635664394]])
    #img = cv.imread(img_path)
    # img = cv.imread(img)
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
      Z = Zone(w, h, x+(w//2), y+(h//2),Aire)
      Liste.append(Z)

      #Affiche les zones sur l'image
      cv.rectangle(image, (x, y), (x+h, y+w),(0,255,0),5)
      cv.circle(image,(x+(w//2),y+(h//2)),1,(0,0,255),10)
  return Liste

def Scan():
  print("Scan en cours...")
  "Ouverture des LED:"
  GPIO.output(LED, GPIO.HIGH)
  time.sleep(1)
  "Variables:"
  #Assignation de la caméra pi
  cam = cv.VideoCapture(0)

  # Définie la couleur à trouvé en HSV pour les zones souillées
  lower_orange = np.array([0,30,200])
  upper_orange = np.array([15,100,255])


  # Définie la couleur rouge à trouvé en HSV pour les ancrages
  lower_red = np.array([160,100,50])
  upper_red = np.array([180,200,200])

  # Définie la couleur bleu à trouvé en HSV pour les lapins
  lower_blue = np.array([80,200,0])
  upper_blue = np.array([130,255,255])

  
  "Démarage du scan de l'image"
  #Code pour tests sans cam
  # path = r'/home/pi/Documents/Cagius/Code/PiCamera/Object_Detection_Files/Litiere.jpg'
  # im = cv.imread(path,1)
  
  #Prise de la photo de la litière
  result, img = cam.read()
  #Nom de l'image
  filename = 'Litiere1' + '.jpg'
  #Corection du fishEye
  im = undistort(img) 

  # Enregistrement de l'image pour observation
  cv.imwrite(filename, im) 

  #Resize de l'image
  im = im[80:350,150:450]
  

  #Application de filtre sur l'image pour facilité la recherche de zones souillées
  #image = cv.GaussianBlur(im, (5,5),1)
  #image = c  v.medianBlur(im,5)
  #kernel = np.ones((5,5),np.float32)/25
  #image = cv.filter2D(im,-1,kernel)

  #Applique un filtre couleur sur l'image
  hsv = cv.cvtColor(im, cv.COLOR_BGR2HSV)

  # Créer les images en binaire sur les couleurs recherchés
  maskSouille = cv.inRange(hsv, lower_orange, upper_orange)
  maskAncrage = cv.inRange(hsv, lower_red, upper_red)
  maskLapin = cv.inRange(hsv, lower_blue, upper_blue)

  #Trouve les contours dans les masks
  contoursSouille, hierarchy = cv.findContours(maskSouille, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
  contoursAncrage, hierarchy = cv.findContours(maskAncrage, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
  contoursLapin, hierarchy = cv.findContours(maskLapin, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

  #Trouver toute les zones souilées qui dépasse un aire minimum
  # print("Aire Souille")
  ListeSouille = findZones(contoursSouille,200,8000,im)

  #Trouver toute les Ancrages qui dépasse un aire minimum
  # print("Aire Ancrage")
  ListeAncrage = findZones(contoursAncrage,150,500,im)

  #Trouver toute les Lapins qui dépasse un aire minimum
  # print("Aire Lapin")
  ListeLapin = findZones(contoursLapin,400,5000,im)

  "Calcul du nombre de lapin dans la cage"
  nbrLapin = len(ListeLapin)

  "Calcul du pourcentage(%) à vider"
  #Initialise la valeux de la distance du convoyeur
  Ymax = 0
  AireSouille = 0
  #Affiche les zones souillées et calcul la plus loin de la poubelle
  for z in ListeSouille:
    if z.getCentreY() > Ymax:
      Ymax = z.getCentreY()
    AireSouille = AireSouille + z.getAire()
    # print('CentreX : {}, CentreY : {}'.format(z.getCentreX(),z.getCentreY()))

  YAncrageMax = 0
  YAncrageMin = inf
  for z in ListeAncrage:
    if z.getCentreY() > YAncrageMax:
      YAncrageMax = z.getCentreY()
    if z.getCentreY() < YAncrageMin:
      YAncrageMin = z.getCentreY() 
    #print('CentreX : {}, CentreY : {}'.format(z.getCentreX(),z.getCentreY()))
  

  #Affiche la zone la plus loin de la poubelle
  # print('Ymax : {}'.format(Ymax))
  # Pourcentage = 25
  # Pourcentage = Ymax/(YAncrageMax-YAncrageMin) * 100
  Pourcentage = (Ymax/YAncrageMax) * 100
  # print('AireSouille : {}'.format(AireSouille))

  AireTotale = 30000
  print('PourHMI: {}'.format((AireSouille*100/AireTotale)))
  if((AireSouille*100/AireTotale) >= 0):
    # Vidage de la cage
    if(Pourcentage <= 40):
      Vidange = 1
    elif((Pourcentage > 40) and (Pourcentage <= 70)):
      Vidange = 2
    else: 
      Vidange = 3
  else: 
    Vidange = 0    
  
  print('BitVidange : {}, NbrLapin : {}'.format(Vidange,nbrLapin))
  "Fermeture des LED:"
  GPIO.output(LED, GPIO.LOW)
  #Affiche les images pour débugage
  #cv.imshow('Image Mask Ancrage', maskAncrage)
  #cv.imshow('Image Mask Lapin', maskLapin)
  #cv.imshow('Image Mask Souille', maskSouille)
  #cv.imshow('Image HSV', hsv)
  #cv.imshow('Image Contour', im)
  #cv.waitKey(0)
  #cv.destroyAllWindows()
  filenameC = 'LitiereContours' + '.jpg'
  cv.imwrite(filenameC, im) 
  

  print("Scan terminé!")
  "Retourne la valeur en % à vider"
  return Vidange,nbrLapin