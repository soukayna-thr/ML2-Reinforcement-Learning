# Machine Learning II - TP5 : Reinforcement Learning avec TF-Agents

Ce projet est un TP pratique qui explore les bases du reinforcement learning en utilisant la bibliothèque [TF-Agents](https://www.tensorflow.org/agents) de TensorFlow. L'objectif principal est de développer un agent DQN pour apprendre à équilibrer un pendule inversé sur le chariot (l'environnement CartPole) à l'aide d'un réseau de neurones et d'un replay buffer.


## Introduction

Dans ce TP, nous aborderons les étapes suivantes :

1. **Préparation de l'environnement :**  
   - Installation des bibliothèques nécessaires (TensorFlow, TF-Agents, TensorFlow Probability, etc.).  
   - Chargement et configuration de l'environnement CartPole à partir de Gym via TF-Agents.

2. **Création du réseau et de l'agent :**  
   - Conception d'un QNetwork simple pour approximer les Q-valeurs.  
   - Mise en place d'un agent DQN.

3. **Entraînement et Évaluation :**  
   - Utilisation d'un replay buffer pour stocker les transitions.  
   - Boucle d'entraînement et évaluation de la performance de l'agent.

## Objectifs

- **Comprendre** comment interagir avec un environnement de Gym via TF-Agents.
- **Implémenter** une architecture standard de DQN pour des tâches de contrôle.

## Prérequis

- Python 3.7+ (Python 3.8 ou supérieur recommandé)
- TensorFlow 2.11 (ou une version compatible)
- TensorFlow Probability (ex. : version 0.19)
- TF-Agents 
- Gym (pour l'environnement CartPole)

## Installation

1. **Installation via pip :**

   Si tu souhaites utiliser la version stable, exécute :

   ```bash
    !pip install --upgrade --force-reinstall tensorflow==2.15.0
    !pip install --upgrade --force-reinstall tf-agents[reverb]==0.16.0
    !pip install --upgrade --force-reinstall numpy==1.23.5
    !pip install gym

Pour plus d'informations, consulter :
* [TensorFlow](https://www.tensorflow.org/agents/tutorials/0_intro_rl?hl=fr)
* [Train a Deep Q Network with TF-Agents](https://github.com/tensorflow/agents/blob/master/docs/tutorials/1_dqn_tutorial.ipynb)
