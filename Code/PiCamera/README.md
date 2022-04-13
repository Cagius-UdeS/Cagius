# Code Caméra
Ce présent document comporte les détails paramétrables et les informations pertinentes sur la caméra.
1.  [Support mécanique](#Supports)
2.  [Calibration](#Étapes-de-calibration-FishEye)
3.  [Modifications des paramètres](#Paramètres-modifiables)
4.  [Valeurs de retour](#Valeurs-de-retour)

## 1. Supports
Si vous utiliser la même caméra que nous utilisons, c'est à dire la RaspberryPi Camera Rev 2.2, vous pouver imprimer ce support en 3D afin de pouvoir fixer votre caméra au dessus de la litière :
1. [Support Caméra](https://github.com/Cagius-UdeS/Cagius/blob/main/CADs/SupportCamera.SLDPRT)
2. [Pied Caméra](https://github.com/Cagius-UdeS/Cagius/blob/main/CADs/PivotCamera.SLDPRT)

## 2. Étapes de calibration FishEye
1. Afin de calibrer la caméra, vous dever d'abord imprimer la [grille de calibration](https://github.com/Cagius-UdeS/Cagius/blob/main/Code/PiCamera/FECalibrationA4.png) et la coller sur une surface dure afin de pouvoir la manipuler sans que la feuille se plie.
2. Ensuite, il faut exécuter le code PatternCapture.py qui prend une photo toute les 3 secondes. Changer l'orientation et la position de la grille pour chacune des photo.
3. Une fois les photos prisent, exécuter le code CalibrationCam.py afin d'obtenir les variables de calibration de votre FishEye comme suit: ![image](https://user-images.githubusercontent.com/72098230/161605262-c62785ff-352e-4e21-ada1-8853365c203e.png)
4. Changer ensuite les valeurs présente dans la fonction undistort du code FonctionsCam.py

## 3. Paramètres modifiables
1.  Puisque nous utilisons les couleurs afin de détecter tout ce que nous avons à détecter, la luminosité à beaucoup d'impact sur la réussite oul'échec de la détection. Nous avons donc ajouter une bande DEL afin de rendre l'environnement stable. Par contre, si vous décider d'utiliser des couleurs différentes ou si la luminausité extérieur à trop d'impact sur la couleur, il est possible de changer ces lignes de code afin de changer ou peaufiner les couleurs à détecter:![image](https://user-images.githubusercontent.com/72098230/163251666-02f7357d-6e6e-4e52-b679-5f276fce0069.png) 


2.  Il est aussi possible de changer les dimenssions des objet à trouver afin de filtrer les résidus involontaires. Pour ce faire, vous pouvez changer les valeurs suivantes pour augmenter ou diminuer l'aire des zones à trouver: ![image](https://user-images.githubusercontent.com/72098230/163252441-32740975-1bd8-4aa3-b7c9-2250f7ee5540.png) 

## 4. Valeurs de retour
Ce code est une fonctions que l'on peut appeller soit Scan() qui retourne la fraction sur 3 donc (0,1,2 ou 3) ainsi que le nombre de lapin présent dans la zone.
