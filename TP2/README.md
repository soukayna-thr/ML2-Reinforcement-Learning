# TP2 – Implémentation du Q-Learning sur FrozenLake

## Objectif

L'objectif de ce TP est de mettre en pratique les concepts fondamentaux de l'apprentissage par renforcement en explorant l'algorithme Q-Learning. À travers une série d'exercices progressifs, nous avons :

- Implémenter l'algorithme Q-Learning.
- Comprendre l'impact des stratégies d'exploration et d'exploitation.
- Observer la convergence de la Q-Table.
  
L'environnement **FrozenLake** de OpenAI Gym servira de terrain d'expérimentation pour illustrer comment un agent apprend à optimiser ses décisions grâce aux mises à jour successives de sa Q-Table.

![Image2](https://www.gymlibrary.dev/_images/frozen_lake.gif)

## Prérequis

- **Python** 
- **Bibliothèques :**
  - [gymnasium](https://www.gymlibrary.dev)  
  - [numpy](https://numpy.org)

## Exercice 1 : Exploration de l'Environnement FrozenLake
Objectif : Comprendre la structure de l'environnement FrozenLake en affichant ses espaces d'états et d'actions, puis en exécutant plusieurs épisodes avec des actions aléatoires.

Instructions :

- Chargement l'environnement FrozenLake-v1 avec l'option.

- Affichage des informations relatives aux espaces d'états et d'actions.

- Exécution une boucle pour simuler plusieurs épisodes avec des actions aléatoires.

- Observation des observations et récompenses obtenues.

## Exercice 2 : Implémentation et Initialisation de la Q-Table
Objectif : Création et initialisation une Q-Table de dimension (nombre d'états x nombre d'actions) avec des valeurs initiales à zéro, puis l'affichage.

Instructions :

- Détermination du nombre d'états (n_states) et d'actions (n_actions).

- Création d'une Q-Table initialisée à zéro avec numpy.zeros.

- Affichage la Q-Table et vérifier que chaque état possède une liste de valeurs associées aux actions possibles.

## Exercice 3 : Implémentation du Q-Learning et Mise à Jour de la Q-Table
Objectif : Appliqueation de la mise à jour de la Q-Table selon l'algorithme Q-Learning et observation l’évolution de celle-ci au fil des épisodes.

Instructions :

- Définition des hyperparamètres :alpha (taux d'apprentissage), gamma (facteur de discount), epsilon (taux d'exploration initial), epsilon_decay (taux de décroissance d'epsilon)

- Implémentation de la règle de mise à jour : Q(s, a) = Q(s, a) + alpha * [R + gamma * max(Q(s',a')) - Q(s, a)]
- Exécution plusieurs épisodes pour faire évoluer la Q-Table.

## Exercice 4 : Évaluation des Performances de l'Agent
Objectif : Évaluation de la performance de l'agent après apprentissage en exécutant des épisodes avec uniquement l'action optimale.

Instructions :

- Effectuation de  100 épisodes en utilisant l'action optimale.

- Mesure du taux de réussite.

