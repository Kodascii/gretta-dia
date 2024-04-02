<link rel="stylesheet" href="../../../stylesheet.css">

# Story_01 — Naïve Bayes

## Contexte
> Découvrir naïve Bayes et se familiariser avec son fonctionnement.

## Mots clefs
- <def-of>Théorème de Bayes</def-of> : *permet de déterminer la probabilité qu'un événement arrive à partir d'un autre évènement qui s'est réalisé, notamment quand ces deux évènements sont interdépendants.*
    $$ P(A\,|\,B) = \frac{P(B\,|\,A)\,\cdot\,P(A)}{P(B)} $$
- <def-of>Classifieur linéaire</def-of> : *Modèle de machine learning qui tente de séparer des données en classes en utilisant une frontière de décision linéaire. L'idée principale est de trouver un hyperplan (une dimension de moins que l'espace de caractéristiques) qui divise l'espace des caractéristiques en deux régions, chaque région étant associée à une classe différente.*
- <def-of>KDD (Knowledge Discovery in Databases)</def-of> : **
- <def-of>Apprentissage supervisé</def-of> : *L'objectif de l'apprentissage supervisé est d'apprendre une fonction qui mappe les entrées aux sorties, en se basant sur les exemples fournis dans l'ensemble d'entraînement.*
- <def-of>Apprentissage non supervisé</def-of> : *Contrairement à l'apprentissage supervisé, où le modèle apprend à partir d'exemples étiquetés, l'apprentissage non supervisé cherche à extraire des modèles ou des structures intrinsèques à partir des données sans avoir d'informations sur les résultats attendus.*
- <def-of>Apprentissage par renforcement</def-of> : *Branche de l'apprentissage machine où un agent interagit avec un environnement dynamique et apprend à prendre des décisions pour maximiser une récompense cumulée.*
- <def-of>CRISP-DM</def-of> : *Modèle de processus standard ouvert qui décrit les approches courantes utilisées par les experts en exploration de données. Il s’agit de l’un des modèles d’analyse les plus utilisés.*
- <def-of>Evènement</def-of> : *C’est une observation (enregistrement), élément d'information qui est utilisé pour entraîner ou évaluer un modèle de prédiction.*
- <def-of>OneR (One-Rule)</def-of> : *Un algorithme simple de classification basé sur une seule règle, qui choisit la variable la plus prédictive (le champ dominant) pour faire des prédictions.*

## Problématiques
1. Comment fonctionne un classifieur Naïve Bayes ? 
1. Comment utiliser Naïve Bayes ?  
1. Quelles sont les avantages et les limites de Naïve Bayes ?  

## Hypothèses
- <u>Naîve Bayes est sous-optimales pour des données ou il existe une forte dépendence entre les variables</u> <h-t/>
    - *Plus la dépendance est grande, moins la précision est grande*
- <u>?</u> <h-t/> : *!;*
- <u>?</u> <h-t/> : *!;*
- <u>?</u> <h-t/> : *!;*
- <u>?</u> <h-t/> : *!;*
- <u>?</u> <h-t/> : *!;*
- <u>?</u> <h-t/> : *!;*
- <u>?</u> <h-t/> : *!;*

## Plan d'action
1. Investigation des ressources
6. Définitions des mots clefs;
7. Vérifier les hypothèses;
8. Répondre aux questions.

# RER

## Validation Croisée en ML
> En divisant  l'ensemble de données nous pouvons:
> - Evaluer les performances du modèle
> - Déterminer le pouvoir prédictif du modèle

## Principales différences des apprentissages
| Critère                         | Apprentissage Supervisé        | Apprentissage Non Supervisé    | Apprentissage par Renforcement  |
| --------------------------------| ----------------------------- | ----------------------------- | ------------------------------- |
| **Données d'entraînement**      | Données étiquetées            | Données non étiquetées        | Interaction avec l'environnement |
| **Objectif principal**          | Prédire les sorties           | Identifier des structures     | Maximiser la récompense cumulée |
| **Exemples d'applications**     | Classification, régression    | Clustering, réduction de dimension | Jeux, robotique, gestion de ressources |
| **Évaluation du modèle**        | Comparaison avec les étiquettes | Évaluation de la structure des données | Maximisation de la récompense    |
| **Supervision des données**     | Étiquettes nécessaires        | Aucune étiquette requise      | Récompenses du système          |
| **Exemples d'algorithmes**      | SVM, réseaux de neurones      | K-moyennes, PCA              | Q-learning, méthodes de politique gradient |
| **Utilisation des prédictions** | Généralisation à de nouvelles données | Identification de modèles, recommandation | Séquence de décisions optimales  |

![](../../res/ML_Learning.webp)

> L’apprentissage profond automatise une grande partie de l’extraction des fonctionnalités du processus, éliminant ainsi une partie de l’intervention humaine manuelle requise. Il permet également d’utiliser de grands ensembles de données, ce qui lui vaut le titre d’apprentissage automatique évolutif. Cette capacité est passionnante à l’heure où nous explorons plus en profondeur l’utilisation de données non structurées, d’autant plus que l’on estime que plus de 80 % des données d’une organisation sont non structurées.