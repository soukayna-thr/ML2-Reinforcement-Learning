# Devoir : Implémentation d'un Agent d'Apprentissage par Renforcement

## Contexte et Objectif

Dans ce devoir, nous avons concevoir et programmer un agent intelligent capable de trouver un trésor dans une grille. 
L'objectif principal est de mettre en œuvre une méthode permettant à l'agent d'explorer l'environnement, d'apprendre de ses expériences et de trouver le chemin optimal pour atteindre le trésor tout en évitant les pièges avec la programmation classique.

## Règles du Jeu

L'agent évolue dans une grille et doit respecter les règles suivantes :

- **Point de Départ :**  
  L’agent commence toujours dans le coin supérieur gauche de la grille, à la case (0, 0).

- **Actions Disponibles :**  
  Il peut se déplacer dans quatre directions : **HAUT**, **BAS**, **GAUCHE** et **DROITE**.

- **Coût des Déplacements :**  
  Chaque déplacement coûte **-1 point** afin d’encourager la recherche du chemin le plus court.

- **Pièges :**  
  Si l’agent entre dans une case contenant un piège, il subit une pénalité de **-10 points** et la partie est terminée immédiatement.

- **Trésor :**  
  Trouver le trésor rapporte **+10 points** et met fin au jeu.
## Les fichiers joints
- [Fichier DevoirSolution](DevoirSolution.ipynb) : contient un code simple de jeu
- [Fichier Simulation](Simulation.py) : aajout des améliorations, notamment une interface pour la simulation du jeu avec un historique des déplacements.
pour l'exécuter:
```bash
   python Simulation.py
