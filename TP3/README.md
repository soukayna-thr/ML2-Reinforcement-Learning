# TP3 – Optimisation des Feux de Circulation avec Apprentissage par Renforcement

## Objectif

L’objectif de ce TP est d’explorer l’optimisation des feux de circulation à l’aide de l’apprentissage par renforcement. À travers ce TP, nous allons :

- Découvrir un environnement simulé pour la gestion du trafic.
- Implémenter deux algorithmes d’apprentissage par renforcement : Q-Learning et SARSA.
- Comparer les résultats obtenus par ces deux algorithmes à l’aide de graphiques et d’évaluations quantitatives.

---

## Prérequis

- **Python** 
- **Bibliothèques :**
  - [NumPy](https://numpy.org)
  - [Matplotlib](https://matplotlib.org)
  - (Assurez-vous également que le module personnalisé pour l’environnement de trafic, par exemple `env_traffic`, est accessible.)

Ce TP se décompose en 4 parties :
Exercice 1 : Découverte de l'Environnement Traffic Tester et explorer l'environnement simulé de gestion du trafic.

Exercice 2 : Implémentation de Q-Learning Créer et entraîner une Q-Table afin d’apprendre une politique optimale via Q-Learning.

Exercice 3 : Implémentation de SARSA Implémenter l’algorithme SARSA, qui met à jour la Q-Table à partir de l’action effectivement choisie, afin de pouvoir comparer avec Q-Learning.

Exercice 4 : Analyse et Visualisation des Résultats Comparer graphiquement l’évolution des récompenses cumulées et la convergence des valeurs pour Q-Learning et SARSA.

## Exercice 1 : Découverte de l'Environnement
Objectif : Découvrir et teste d’environnement simulé de gestion du trafic.

Instructions :

- Importation d'environnement Traffic depuis le module. (Ficher env_traffic.py)

- Exécutionl'environnement sur quelques itérations.

## Exercice 2 : Implémentation de Q-Learning
Objectif : Implémentation d'algorithme Q-Learning pour entraîner l'agent à optimiser les actions afin d'obtenir une politique optimale.

Instructions :

- Initialisation d'une Q-Table adaptée à la dimension de l'environnement. 

- Utilisation une stratégie epsilon-greedy pour gérer l'exploration et l'exploitation.

- Mise à jour la Q-Table selon la règle suivante : Q(s,a) = Q(s,a) + alpha * [R + gamma * max(Q(s',a')) - Q(s,a)]

- Entraînement sur plusieurs épisodes.

## Exercice 3 : Implémentation de SARSA
Objectif : Implémentation d'algorithme SARSA pour comparer la mise à jour basée sur l'action réellement choisie avec Q-Learning.

Instructions :

- Créeation et initialisation d'une nouvelle Q-Table pour SARSA.

- Utilisation d'une stratégie epsilon-greedy.

- Mise à jour la Q-Table avec la règle SARSA : Q(s,a) = Q(s,a) + alpha * [R + gamma * Q(s',a') - Q(s,a)]

- Entraînement d'agent sur plusieurs épisodes.

## Exercice 4 : Analyse et Visualisation des Résultats
Objectif : Analyse de la performance de l’agent en comparant la convergence et la vitesse d’apprentissage de Q-Learning et SARSA à l’aide de graphiques.

Instructions :

Utilisation de  Matplotlib pour tracafe des courbes et comparaison :

- L’évolution des récompenses cumulées.

- La rapidité avec laquelle l’agent converge vers une politique optimale.

## Interprétation Finale des Résultats

![Image3](https://0.academia-photos.com/330955293/180743098/170847113/original_image3.png)

Le graphique comparatif des récompenses cumulées entre Q-Learning et SARSA met en évidence plusieurs points clés concernant l'évolution de l'apprentissage dans l'optimisation des feux de circulation :

1. Convergence des Algorithmes
- Les deux algorithmes atteignent, après un certain nombre d'épisodes, une stabilisation des récompenses cumulées.
- Cette convergence indique que l'agent adopte une politique efficace pour optimiser ses actions.
- Q-Learning et SARSA semblent ainsi apprendre de manière relativement similaire dans cet environnement.

2. Rapidité d'Apprentissage
- Bien que les courbes de récompenses se rapprochent vers la fin de l'entraînement, de légères différences persistent dans la vitesse de convergence.
- Ces variations suggèrent qu'un algorithme (par exemple, Q-Learning) peut converger plus rapidement ou de façon plus stable que SARSA dans ce contexte spécifique.

3. Stabilité et Variabilité
- Les fluctuations observées au début des épisodes traduisent une phase d'exploration intense, où l'agent teste diverses politiques.
- Au fur et à mesure, la réduction des variations indique que l'agent affine ses décisions et la politique apprise devient plus robuste et homogène.

4.  Choix de l'Algorithme en Fonction du Contexte
- Malgré des performances finales comparables, le choix entre Q-Learning et SARSA peut être orienté en fonction de critères complémentaires tels que la rapidité de convergence ou la stabilité désirée.
- Ce choix dépendra des exigences spécifiques de l'application, ici, l'optimisation de la gestion des feux de circulation.

## Conclusion
En résumé, l'analyse comparative suggère que, malgré de légères différences dans le processus d'apprentissage, les deux algorithmes sont capables d'apprendre une politique efficace pour optimiser les feux de circulation dans l'environnement simulé. Cette étude ouvre la voie à des expérimentations supplémentaires en ajustant les hyperparamètres afin de maximiser les performances dans des scénarios plus variés.



Pour plus d'informations, vous pouvez consulter ce document  : [Analyse Comparative de SARSA et Q-Learning pour l'Optimisation des Feux de Circulation](https://www.academia.edu/128465535/Analyse_Comparative_de_SARSA_et_Q_Learning_pour_lOptimisation_des_Feux_de_Circulation)

