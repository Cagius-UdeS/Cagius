# Cagius

Cagius est un projet open source ayant comme objectif de concevoir et construire le mécanisme de gestion de la litière pour une cage à petits animaux automatisée et créer un interface programmable pour gérer les cycles de nettoyages.

## Table des matieres

1. [Composantes mecaniques et electroniques](#composantes-mecaniques-et-electroniques)
2. [Composantes informatiques](#composantes-informatiques)
3. [Assemblage](#assemblage)
4. [Installation logiciel](#installation-logiciel)
5. [Initialisation de la cage](#initialisation-de-la-cage)
6. [Autres informations](#autres-informations)
7. [License](#license)

## Composantes mecaniques et electroniques
### Mécaniques
- Courroie Synchrone : McMaster **1679K55** 
- Tige Filletée : Mcmaster **98957A154**
### Électroniques
- RaspberryPi 4
- RaspberryPi Caméra
- 3 x Dynamixel 
- 1 x Dynamixel

## Composantes informatiques


## Assemblage

Pour ce qui est de l'assemblage de la structure de base, il suffit de respecter l'assemblage de la pièce PoubelleV3.sldprt. En fait, un mélange de colle et de clou à finition ont été utilisé pour avoir un structure solide. De plus, le prototype actuelle est fait avec des planche de bois 1/4" découpé au laser et assembler par la suite. Ensuite, la pièce rail.sldprt et trape_horizontal.sldprt sont collé ensemble et forme la trappe en avant de la poubelle au niveau du plancher médian.

Pour ce qui est de l'assemblage du convoyeur, ...

[Pour les détails concernants les CADs et leurs pertinances](https://github.com/Cagius-UdeS/Cagius/blob/main/Documentation/Hierarchie_pieces.md)

## Installation logiciel

La section suivante couvre l'installation des logiciels et des librairies nécessaires à la compilation du code.

### Installation sur Ordinateur

Il est nécessaire de compiler et d'envoyer le code de la carte OpenCR a partir d'un ordinateur, car le Pi ne prend pas en charge les librairies de la carte OpenCR et des moteurs Dynamixel.

#### Installation de Arduino IDE

Afin d'installer Arduino IDE et les librairies nécessaires pour coder les moteurs, il suffit de suivre les étapes suivantes :

1. Télécharger l'application Arduino IDE [ici](https://www.arduino.cc/en/software)
2. Ouvrir l'application et se rendre dans *Fichier*, puis *Préférences*
3. Dans la section *URL de gestionnaire de cartes supplémentaires*, rajouter la ligne suivante:
	`https://raw.githubusercontent.com/ROBOTIS-GIT/OpenCR/master/arduino/opencr_release/package_opencr_index.json`
4. Confirmer les changements en pressant *OK* dans le bas à droite de l'écran.
5. Enfin, installer les librairies Motorcontrole dans la section *Outils* puis *Type de carte* et *Gestionnaire de carte*. Taper OpenCR dans la barre de recherche et installer les librairies.

### Installation sur Pi

Le Pi agit comme le cerveau de la cage. En effet, le Pi analyse la caméra et l'interface utilisateur.

#### Installation de Qt designer

Si vous voulez modifier l'interface utilisateur (modifier les fichiers .ui), vous devez télécharger Qtdesigner (fait parti de Qtcreator)

  $ sudo apt-get install qttools5-dev-tools
  $ sudo apt-get install qttools5-dev

#### Installation de PyQt

Pour concevoir le HMI nous avons utilisé PyQt qui est un module libre qui permet de lier le langage Python avec la bibliothèque Qt. 
L'installation se fait sur le Raspberry Pi et consiste à faire rouler la ligne de commande suivante :

	$ sudo apt-get install python3-pyqt5

Si votre Pi n'est pas à jour, rouler ces lignes de commande au préalable :

	$ sudo apt-get update
	$ sudo apt-get upgrade

À partir de là, pour coder l'interphase graphique on utilise Qt 5 Designer avec le PyQt intégré.

#### Installation des librairies Open CV
Afin d'installer OpenCV sur votre RaspberryPi, 
il suffit de suivre le guide **Setting Up Open-CV for Object Detection** sur ce site:
[Guide d'installation OpenCV](https://core-electronics.com.au/tutorials/object-identify-raspberry-pi.html)

## Initialisation de la cage


## Autres informations


## License
