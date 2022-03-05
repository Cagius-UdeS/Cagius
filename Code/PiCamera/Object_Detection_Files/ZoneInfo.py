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