# Dossier *PiCamera*

Ce présent document comporte les détails paramétrables et les informations pertinentes sur la caméra.

1. [Supports](#1-supports)
2. [Étapes de calibration FishEye](#2-étapes-de-calibration-fisheye)
3. [Paramètres modifiables](#3-paramètres-modifiables)
4. [Valeurs de retour](#4-valeurs-de-retour)
5. [Algorithme de fonctionnement de la caméra](#5-algorithme-de-fonctionnement-de-la-caméra)

## 1. Supports

Si vous utilisez la même caméra que nous utilisons, c'est-a-dire la Raspberry Pi Camera Rev 2.2, vous pouver imprimer ce support en 3D afin de pouvoir fixer votre caméra au dessus de la litière :

- [Support Caméra](https://github.com/Cagius-UdeS/Cagius/blob/main/CADs/SupportCamera.SLDPRT)
- [Pied Caméra](https://github.com/Cagius-UdeS/Cagius/blob/main/CADs/PivotCamera.SLDPRT)

## 2. Étapes de calibration FishEye

1. Afin de calibrer la caméra, vous dever d'abord imprimer la [grille de calibration](https://github.com/Cagius-UdeS/Cagius/blob/main/Code/PiCamera/FECalibrationA4.png) et la coller sur une surface dure afin de pouvoir la manipuler sans que la feuille se plie.

2. Ensuite, il faut exécuter le code PatternCapture.py qui prend une photo toute les 3 secondes. Changer l'orientation et la position de la grille pour chacune des photo.

3. Une fois les photos prisent, exécuter le code CalibrationCam.py afin d'obtenir les variables de calibration de votre FishEye comme suit : ![image](https://user-images.githubusercontent.com/72098230/161605262-c62785ff-352e-4e21-ada1-8853365c203e.png).

4. Changer ensuite les valeurs présente dans la fonction undistort du code FonctionsCam.py.

## 3. Paramètres modifiables

### 3.1 Couleurs des zones

Puisque nous utilisons les couleurs afin de détecter tout ce que nous avons à détecter, la luminosité a beaucoup d'impact sur la réussite ou l'échec de la détection. Nous avons donc ajouté une bande DEL afin de rendre l'environnement stable. Par contre, si vous décidez d'utiliser des couleurs différentes ou si la luminosité extérieure a trop d'impact sur la couleur, il est possible de changer ces lignes de code afin de changer ou peaufiner les couleurs à détecter : ![image](https://user-images.githubusercontent.com/72098230/163255912-d203a798-7fc6-4f1e-9b2a-50470546e7dd.png)

### 3.2 Aires des zones

Il est aussi possible de changer les dimenssions des objets à trouver afin de filtrer les résidus involontaires. Pour ce faire, vous pouvez changer les valeurs suivantes pour augmenter ou diminuer l'aire des zones à trouver : ![image](https://user-images.githubusercontent.com/72098230/163256289-5e120028-6ef1-4f03-8c61-63f407774081.png)

### 3.3 Pourcentage des zones souillées pour vider

Cette valeurs permet de changer le seuil que les zones souillées doivent atteindre au total avant de nécéssité un vidage de la litière : ![image](https://user-images.githubusercontent.com/72098230/163257047-ad308acc-94f3-4990-a199-06c5187182b2.png)
 
## 4. Valeurs de retour

Ce code est une fonction que l'on peut appeller soit Scan() qui retourne la fraction sur 3 donc (0,1,2 ou 3) ainsi que le nombre de lapins présents dans la zone. Ne pas oublier d'ajouter la fonction InitGPIO afin d'activer les I/O du Raspberry Pi.

## 5. Algorithme de fonctionnement de la caméra

<img src="../../Documentation/Images/AlgoCamera.jpg">