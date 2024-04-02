<link rel="stylesheet" href="../../../stylesheet.css">

# Story_00 — Arbre de décision

## Contexte
> .

## Mots clefs
- <def-of>Arbre de décision</def-of> : *Outil d'aide à la décision représentant un ensemble de choix sous la forme graphique d'un arbre.*
- <def-of>Decision Tree Classifier</def-of> : *Classe capable d'effectuer une classification multi-classes sur un ensemble de données.*
- <def-of>Pruning</def-of> : *Algorithme utilisé pour élaguer un arbre afin d'éviter le surajustement*
- <def-of>Hyperparamètre</def-of> : *Paramètre externe au modèle qui ne peut pas être appris à partir des données d'entraînement.*
- <def-of>Métriques</def-of> : *Mesure quantitative qui permet d'évaluer la performance d'un modèle ou d'une solution par rapport à certains critères.*
    - **Precision** : *Mesure la proportion de vrais positifs parmi toutes les prédictions positives.*
    - **Recall** : *Mesure la proportion de vrais positifs parmi tous les exemples réels positifs.*
    - **F1-Score** : *Une métrique qui combine précision et rappel.*
    - **ROC (Receiver Operating Characteristic)** : *Courbe graphique utilisée pour évaluer la performance d'un modèle de classification, en particulier dans le contexte de la classification binaire*
    - **AUC-ROC** : *L'aire sous la courbe ROC, qui évalue la performance d'un modèle de classification binaire sur différents seuils.*
- <def-of>ID3</def-of> : *(DecisionTreeClassifier) Un algorithme spécifique utilisé pour construire des arbres de décision en choisissant les meilleures caractéristiques pour diviser les données à chaque nœud.*
- <def-of>Matice de confusion</def-of> : *Table qui est utilisée pour évaluer les performances d'un modèle de classification sur un ensemble de données, en comparant les prédictions du modèle aux vraies valeurs (étiquettes) des observations.*
- <def-of>Overfitting</def-of> : *Il se produit lorsqu'un modèle est trop complexe par rapport à la complexité sous-jacente réelle des données.*
- <def-of>Cross validation</def-of> : *Technique d'évaluation des performances d'un modèle d'apprentissage automatique. Son objectif principal est de maximiser l'utilisation des données d'entraînement tout en permettant une estimation fiable de la performance du modèle sur des données non vues.*
- <def-of>Entropie</def-of> : *Mesure du désordre (impureté, chaos ou encore le hasard)*
- <def-of>CART (Classification and Regression Trees)</def-of> : *Technique utilisée pour la construction d'arbres de décision, tant pour les problèmes de classification que pour les problèmes de régression.*
- <def-of>Gini</def-of> : *Mesure de l'impureté ou du désordre dans un ensemble d'éléments. L'impureté Gini est couramment utilisée comme critère pour diviser les nœuds dans un arbre de décision pendant le processus de construction.*

## Problématiques
1. Comment fonctionne le ID3 ?
1. Comment utiliser le classifieur ID3 ?
1. Comment choisir les hyper-paramètres pour que l'algo soit le mieux adaptés ?

## Hypothèses
- <u>Les arbres D sont adaptés pour le clustering</u> <h-t/> : *!;*
- <u>Les arbres de decision évite l’overfitting</u> <h-t/> : *!;*
- <u>Les arbres de décision </u> <h-t/> : *!;*
- <u>L’entropie est un hyperparamètre de ID3</u> <h-f/> : *C'est-un paramètre*
- <u></u> <h-t/> : *!;*
- <u>?</u> <h-t/> : *!;*
- <u>?</u> <h-t/> : *!;*
- <u>?</u> <h-t/> : *!;*

## Plan d'action
1. Investigation des ressources
6. Définitions des mots clefs;
7. Vérifier les hypothèses;
8. Répondre aux questions.

# RER

## Sklearn Hypèresparamètres

### Arbres de Décision et Forêts Aléatoires

**Arbres de Décision :**
- `criterion` : Critère de fractionnement ('gini' ou 'entropy').
- `max_depth` : Profondeur maximale de l'arbre.
- `min_samples_split` : Nombre minimum d'échantillons requis pour fractionner un nœud interne.
- `min_samples_leaf` : Nombre minimum d'échantillons requis dans une feuille.

**Random Forest** :
- Tous les hyperparamètres des arbres de décision.
- `n_estimators` : Nombre d'arbres dans la forêt.

### Machines à Vecteurs de Support (SVM)
- `C` : Coefficient de régularisation.
- `kernel` : Type de noyau ('linear', 'poly', 'rbf', etc.).
- `gamma` : Coefficient du noyau pour 'rbf', 'poly' et 'sigmoid'.

### Régression Linéaire
- `alpha` : Terme de régularisation pour Ridge et Lasso.
- `l1_ratio` : Ratio de mélange pour Elastic Net (utilisé avec penalty='elasticnet').

### Réseaux de Neurones (MLP)
- `hidden_layer_sizes` : Taille des couches cachées.
- `activation` : Fonction d'activation ('identity', 'logistic', 'tanh', 'relu').
- `learning_rate` : Taux d'apprentissage ('constant', 'invscaling', 'adaptive').

### k-Moyennes (Clustering)
- `n_clusters` : Nombre de clusters à former.
- `init` : Méthode d'initialisation des centroïdes ('k-means++', 'random').

### Réduction de Dimension (PCA)
- `n_components` : Nombre de composantes principales à extraire.

### Gradient Boosting
- `n_estimators` : Nombre d'itérations.
- `learning_rate` : Taux d'apprentissage.
- `max_depth` : Profondeur maximale des arbres.

### Méthodes d'Ensemble
- `n_estimators` : Nombre d'estimateurs dans l'ensemble (pour AdaBoost, Gradient Boosting, etc.).

### Validation Croisée
- `cv` : Nombre de plis dans la validation croisée.


## Matrice de Confusion

La matrice de confusion a quatre entrées principales :
1. **Vrais Positif** $T_+$ : Le nombre d'observations réelles de la classe positive correctement prédites comme positives par le modèle.
1. **Vrais Négatifs** $T_-$ : Le nombre d'observations réelles de la classe négative correctement prédites comme négatives par le modèle.
1. **Faux Positif** $F_+$ : Le nombre d'observations réelles de la classe négative incorrectement prédites comme positives par le modèle (erreur de type I).
1. **Faux Négatifs** $F_-$ : Le nombre d'observations réelles de la classe positive incorrectement prédites comme négatives par le modèle (erreur de type II).

À partir de ces valeurs, plusieurs métriques de performance peuvent être calculées, notamment :
- **Précision (Precision) :** *La proportion d'observations prédites comme positives parmi celles qui le sont réellement* $$\frac{T_+}{T_+ + F_-}$$
- **Rappel (Recall) :** *La proportion d'observations positives réellement prédites comme positives par le modèle.* $$\frac{T_+}{T_+ + F_-}$$
- **Exactitude (Accuracy) :** *La proportion totale d'observations correctement classées par le modèle.* $$\frac{T_+ + T_-}{T_+ + T_- + F_+ + F_-}$$

## Arbre de decisions
> Plus l’arbre est profond, plus les règles de décision sont complexes et plus le modèle est adapté.

### Les 4 d'apprentissage supérvisé
- 1. **Dataset** (`X`: features, `y`: target)
- 2. **Modèle** : *Spécifier le modèle et les hyperparamètres du modèle*
- 3. **Fonction Coût** : Ensemble des erreurs entre les prédictions du modèle et les vraies valeurs du dataset
- 4. **Algorithme de minimisation** : Cherche à minimiser la fonction coût en cherchant les meilleurs paramètres.
https://profs.info.uaic.ro/~ciortuz/SLIDES/ml3.pdf