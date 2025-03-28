 # TP1 – Initiation au Reinforcement Learning avec OpenAI Gym 🤖

## 📌 Contexte et Objectif

Ce TP fait partie du module "Machine Learning II". L'objectif est de se familiariser avec les outils essentiels du Reinforcement Learning (RL) en utilisant principalement la bibliothèque OpenAI Gym. Nous avons apprendre à interagir avec un environnement RL, à exécuter des actions et à comprendre les notions de base comme l'espace d'actions, les observations, les récompenses et le critère de fin d'épisode.

## 🚀 Partie 1 : Présentation des Bibliothèques Clés

### OpenAI Gym
![img](https://gymnasium.farama.org/_images/gymnasium-text.png)

- **Description :**
  - OpenAI Gym fournit un ensemble d'environnements interactifs qui permettent de tester et de comparer différents algorithmes d'apprentissage par renforcement.
  - Un environnement Gym est défini par un ensemble **d'états**, **d'actions**, **de récompenses**, et **un critère de fin**.

- **Installation :**

  Pour installer Gym ainsi que quelques bibliothèques associées (pygame, numpy, etc.), exécutez la commande suivante :
  
  ```bash
  pip install --upgrade gymnasium pygame numpy
  
## 🛠️ Partie 2 : Exercices Pratiques avec OpenAI Gym

### Exercice 1 : Découverte et Exploration d'un Environnement
**Objectif :**  
Comprendre la structure d'un environnement Gym en examinant ses espaces d'actions et d'observations.

---

### Exercice 2 : Manipulation des Observations et Récompenses
**Objectif :**  
Analyser comment récupérer l'observation, la récompense et l'état de fin (`done`) après l'exécution d'une action.

---

### Exercice 3 : Contrôle Manuel de l'Agent
**Objectif :**  
Permettre à l'utilisateur de contrôler manuellement l'agent pour observer directement l'effet de ses actions.

---

### Exercice 4 : Évaluation des Performances d'une Politique Aléatoire
**Objectif :**  
Mesurer la durée moyenne d'un épisode lorsque l'agent prend des actions aléatoires.


## 🎯  Informations : CartPole - OpenAI Gym


### Objectif
L'agent doit apprendre à garder l'équilibre du poteau aussi longtemps que possible en sélectionnant les bonnes actions.
![Image1](https://www.gymlibrary.dev/_images/cart_pole.gif)

### Environnement

#### 1. **Espace d'état (Observation Space)**
L'état est représenté par un vecteur de 4 valeurs continues :
- **Position du chariot** (x)
- **Vitesse du chariot** (\(\dot{x}\))
- **Angle du poteau** (\(\theta\))
- **Vitesse angulaire du poteau** (\(\dot{\theta}\))

#### 2. **Espace d'actions (Action Space)**
L'agent peut prendre deux actions discrètes :
- `0` : Appliquer une force vers la gauche
- `1` : Appliquer une force vers la droite

#### 3. **Récompense (Reward)**
L'agent reçoit une **récompense de +1** pour chaque étape où le poteau reste en équilibre.

#### 4. **Conditions de fin**
L'épisode se termine si :
- L'angle du poteau dépasse **±12°**
- La position du chariot dépasse **±2.4 unités**
- L'épisode atteint **500 étapes**

Pour plus d'informations, consulter : 📚[Documentation CartPole](https://www.gymlibrary.dev/environments/classic_control/cart_pole/) 
