# TP4 – Apprentissage Profond pour les Jeux : Entraînement d'un Agent avec PPO sur Taxi-v3

## Objectif du TP

Ce TP a pour objectif de familiariser avec l'implémentation de l'algorithme **Proximal Policy Optimization (PPO)**.

![Image4](https://www.gymlibrary.dev/_images/taxi.gif)
## Prérequis

- **Python**
- **Bibliothèques requises :**
  - [Gymnasium](https://www.gymlibrary.dev)
  - [NumPy](https://numpy.org)
  - (Dépendance pour l'environnement Taxi-v3, disponible via Gymnasium)

Le TP se divise en 4 exercices :

## Exercice 1 : Initialisation de l'Environnement et des Structures de Données
Instructions :

- Initialisation l'environnement Taxi-v3.

- Affichage du nombre d'états et d'actions.

- Création d'une table de politique où chaque état dispose d'une probabilité égale pour chaque action.

- Création d'une table de valeurs initialisée à zéro.

- Affichage des premières lignes de policy_table et value_table.

## Exercice 2 : Expiration et Collecte d'Épisodes
Instructions :

- Exécution d'un agent aléatoire dans l'environnement pendant 20 épisodes.

- Affichage des actions exécutées et les récompenses obtenues pour chaque épisode.

## Exercice 3 : Mise à Jour de la Politique avec PPO
Instructions :

- Implémentation de l'algorithme PPO qui optimise la politique en utilisant une fonction objectif avec clipping pour éviter des mises à jour trop brutales.

- Calcule des récompenses cumulées (discounted rewards) et l’avantage.
- Mise à jour la table de politique et la fonction de valeur.

## Exercice 4 : Évaluation de l'Agent Après Entraînement
Instructions :

- Teste de l'agent entraîné pendant 20 épisodes.

- Comparaison des performances (récompense cumulative) avant et après l'entraînement.

  
Voir Notebook : [Notebook du TP4](TP4.ipynb)

En cas de problème d'ouverture ou pour un accès simplifié, vous pouvez consulter et exécuter le notebook directement sur Google Colab en suivant ce lien : [Accéder au notebook sur Colab](https://colab.research.google.com/drive/1-ImQ4deX4MMHV9byt6KsTa5sg16FFh8Y?usp=sharing)

Pour plus d'informations, consulter : 📚[Documentation Taxi-v3](https://www.gymlibrary.dev/environments/toy_text/taxi/) 
