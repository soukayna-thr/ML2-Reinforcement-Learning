# 🚀 Machine Learning II - Travaux Pratiques en Reinforcement Learning  

Ce repository contient les travaux pratiques réalisés dans le cadre du module **Machine Learning II**, axé sur l'apprentissage par renforcement (*Reinforcement Learning*). L'objectif est d'explorer les concepts fondamentaux, d'expérimenter avec des algorithmes classiques et d'appliquer ces techniques à des problématiques concrètes.

## 📌 Contenu du repository  

Ce projet est organisé en quatre travaux pratiques (TP), chacun traitant un aspect clé de l'apprentissage par renforcement :  

| TP  | Sujet  | Objectif  |
|------|--------|-----------|
| TP1  | Introduction à OpenAI Gym  | Se familiariser avec les outils essentiels du Reinforcement Learning |
| TP2  | Implémentation de Q-Learning | Mettre en pratique les concepts fondamentaux de l'apprentissage par renforcement |
| TP3  | Optimisation des feux de circulation | Appliquer l'apprentissage par renforcement à un problème du monde réel, et comparer Q-Learning avec SARSA|
| TP4  | Apprentissage profond pour les  jeux | Comprendre et expérimenter avec l’algorithme **Proximal Policy Optimization (PPO)** |

## 🛠 Technologies utilisées  

- **Python 3.x**
- **Environnement de développement** - Recommandé : Jupyter / Colab / Vs Code
- **OpenAI Gym** – Environnement de simulation pour le RL  
- **NumPy & Matplotlib** – Manipulation des données et visualisation   

## 📚 About OpenAI Gym
OpenAI Gym est une bibliothèque Python open-source développée par OpenAI pour faciliter la création et l’évaluation des algorithmes d’apprentissage par renforcement (RL).

### - Comment fonctionne?
OpenAI Gym repose sur une approche intuitive : il met à disposition des environnements où un agent peut interagir en prenant des actions, recevant des récompenses ou des pénalités, et observant les conséquences de ses décisions.

Grâce à une interface homogène pour tous les environnements, il simplifie le développement et l'évaluation d'algorithmes d'apprentissage par renforcement, en éliminant le besoin de personnaliser le code pour des spécifications environnementales variées.

### - Les 4 principales caractéristiques d’OpenAI Gym
OpenAI Gym offre plusieurs fonctionnalités clés qui le rendent précieux pour l’apprentissage par renforcement :

<div align="center">
  <img src="https://www.allaboutai.com/wp-content/uploads/2024/09/Environment-Agent.gif" width="500">
</div>

- *Environnements* : Configurez et entraînez des agents dans une variété d'environnements à l'aide de la fonction make, avec la possibilité de gérer des scénarios multi-agents.

- *Wrappers* : Personnalisez les environnements existants en modifiant des paramètres tels que les actions ou les récompenses, afin d'adapter le processus d'entraînement à vos besoins spécifiques.

- *Actions* : Déterminez la manière dont l’agent réagit aux observations. Chaque action déclenche une étape dans l’environnement, générant de nouvelles observations, des récompenses et des retours d’état.

- *Observations* : Collectez les données relatives à l’interaction de l’agent avec l’environnement, incluant des détails pour faciliter le débogage et suivre l’évolution des performances étape par étape.

### - Les avantages d’OpenAI Gym
OpenAI Gym est essentiel pour toute personne travaillant avec l’apprentissage par renforcement, offrant une manière contrôlée et flexible de développer et tester des modèles d’IA. Voici pourquoi il est indispensable :

<div align="center">
  <img src="https://www.allaboutai.com/wp-content/uploads/2025/01/Interaction-Protocols-in-Object-Interaction-768x576.png.webp" width="500">
</div>

## 🚀 Instructions d'installation  

1. **Cloner le repository**  
   ```bash
   git clone https://github.com/soukayna-thr/ML2-Reinforcement-Learning.git
   
2. **Accéder au projet**  
   ```bash
   cd ML2-Reinforcement-Learning

## 📊 Résultats et observations
Les résultats détaillés de chaque TP (apprentissage des agents, graphiques, scores obtenus) sont disponibles dans les notebooks et les fichiers de rapport correspondants.

📜 Licence
---
Ce projet est distribué sous la licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus d'informations.
