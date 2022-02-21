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


## Composantes informatiques


## Assemblage

Pour ce qui est de l'assemblage de la structure de base, il suffit de respecter l'assemblage de la pièce PoubelleV3.sldprt. En fait, un mélange de colle et de clou à finition ont été utilisé pour avoir un structure solide. De plus, le prototype actuelle est fait avec des planche de bois 1/4" découpé au laser et assembler par la suite. Ensuite, la pièce rail.sldprt et trape_horizontal.sldprt sont collé ensemble et forme la trappe en avant de la poubelle au niveau du plancher médian.

Pour ce qui est de l'assemblage du convoyeur, ...

## Installation logiciel

La section suivante couvre l'installation des logiciels et des librairies necessaires a la compilation du code.

### Installation sur Ordinateur

Il est necessaire de compiler et d'envoyer le code de la carte OpenCR a partir d'un ordinateur, car le Pi ne prend pas en charge les librairies de la carte OpenCR et des moteurs Dynamixel.

#### Installation de Arduino IDE

### Installation sur Pi

Le Pi agit comme le cerveau de la cage. En effet, le pi analyse la caméra et l'interface utilisateur.

#### Installation de PyQt

Pour concevoir le HMI nous avons utilisé PyQt qui est un module libre qui permet de lier le langage Python avec la bibliothèque Qt. L'installation se fait sur le Raspberry Pi et consiste à faire rouler la ligne de commande suivante :



#### Installation des librairies Open CV


## Initialisation de la cage


## Autres informations


## License
