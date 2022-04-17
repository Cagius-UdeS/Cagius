# Dossier *Main*

Les fichiers de ce dossier assurent la communication entre le Raspberry Pi, la carte OpenCR et la caméra Pi et contiennent la machine à état général du code, en d'autres termes la séquence d'éxécution.

## Fichiers

- **functions_Comm** : Fichier contenant les différentes fonctions pour envoyer, recevoir et attendre des messages de la carte OpenCR.
- **init_stop_Sequences** : Fichier contenant les différentes fonctions d'initialisation de composantes ou de séquences, de lancements d'états.

## Structure du programme

<img src="../../Documentation/Images/HierarchieMain.png">

### Communication Pi et OpenCR

<img src="../../Documentation/Images/flowchart.png">

### Algorithme d'utilisation de la caméra dans la séquence

<img src="../../Documentation/Images/Algo_PI_Camera.png">
