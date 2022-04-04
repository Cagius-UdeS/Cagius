# Requis pour Caméra

## Support à caméra
Si vous utiliser la même caméra que nous utilisons, c'est à dire la RaspberryPi Camera Rev 2.2, vous pouver imprimer ce support en 3D afin de pouvoir fixer votre caméra au dessus de la litière :
1. [Support Caméra](https://github.com/Cagius-UdeS/Cagius/blob/main/CADs/SupportCamera.SLDPRT)
2. [Pied Caméra](https://github.com/Cagius-UdeS/Cagius/blob/main/CADs/PivotCamera.SLDPRT)

## Calibration caméra
1. Afin de calibrer la caméra, vous dever d'abord imprimer la [grille de calibration]() et la coller sur une surface dure afin de pouvoir la manipuler sans que la feuille se plie.
2. Ensuite, il faut exécuter le code PatternCapture.py qui prend une photo toute les 3 secondes. Changer l'orientation et la position de la grille pour chacune des photo.
3. Une fois les photos prisent, exécuter le code CalibrationCam.py afin d'obtenir les variables de calibration de votre FishEye comme suit: ![image](https://user-images.githubusercontent.com/72098230/161605262-c62785ff-352e-4e21-ada1-8853365c203e.png)
Changer ensuite les valeurs présente dans la fonction undistort du code FonctionsCam.py
