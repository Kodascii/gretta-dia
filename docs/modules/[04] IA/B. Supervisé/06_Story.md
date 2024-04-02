<link rel="stylesheet" href="../../../stylesheet.css">

# Story_00 — Support Vector Machines (SVC & SVR)

## Contexte
> .

## Mots clefs
- <def-of>SVM</def-of> : *Ensemble de méthodes d’apprentissage supervisé utilisées pour la classification, la régression et la détection des valeurs aberrantes.*
- <def-of>SVC (Support Vector Classification)</def-of> : *Visent à trouver un hyperplan optimal pour séparer les différentes classes dans l'espace des caractéristiques.*
- <def-of>SVR (Support Vector Regression)</def-of> : *Vise à trouver un hyperplan optimal qui maximise la marge tout en minimisant l'erreur de prédiction.*
- <def-of>Vecteur Support</def-of> : *Point de données d'entraînement qui se trouve le plus près de l'hyperplan de décision.*
- <def-of>[RBF](https://fr.wikipedia.org/wiki/Fonction_de_base_radiale) (Radial Basis Function)</def-of> : **
    $$K(x, y) = \exp(-\gamma||x - y||^2$$
- <def-of>Hyperplan</def-of> : *Objet mathématique qui définit une séparation dans un espace de dimension supérieure. Dans le contexte des SVM, il est utilisé pour délimiter les classes et maximiser la marge entre elles.*
- <def-of>[MAE](https://en.wikipedia.org/wiki/Mean_absolute_error) (Mean Absolute Error)</def-of> : *Evalue la performance d'un modèle de régression, en quantifiant la différence moyenne entre les valeurs prédites par le modèle et les valeurs réelles de la variable cible.*
    $$MAE = \frac{1}{n}\sum_{i=1}^n |y_i - \hat{y}_i|$$
- <def-of>MSE (Mean Squared Error)</def-of> : *Quantifie la moyenne des carrés des différences entre les valeurs prédites par le modèle et les valeurs réelles de la variable cible. Cette métrique permet de mettre un 'poids' plus important pour les valeurs qui sont éloignées de la fonction hypothèse.*
    $$MSE = \frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2$$
- <def-of>RMSE (Root Mean Squared Error)</def-of> : **
    $$RMSE = \sqrt{MSE}$$
- <def-of>R²</def-of> : *Le coefficient de détermination, mesure la qualité de la prédiction d'une régression.*
    $$R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y}_i)^2}$$
- <def-of>Adjusted R²</def-of> : *R2 tend à surévaluer la qualité de la régression linéaire. Sa valeur augmente toujours car le nombre d'effets est inclus dans le modèle. La mesure R2 ajusté tente de corriger cette surévaluation. Le R2 ajusté peut diminuer si un effet spécifique n'améliore pas le modèle.*
    $$\bar{R}^2 = 1 - \frac{(1 - R^2) \times (n - 1)}{n - p - 1}$$
- <def-of>Marge Maximale</def-of> : *Désigne la distance entre les vecteurs de supports.*
- <def-of>`C`</def-of> : *Paramètre de régularisation; Compromis entre les violations de marges et l'augmentation de la marge.*
- <def-of>`epsilon`</def-of> : *Hyperparamètre d'un modèle SVR, c'est l'erreur tolérée entre les prédictions et les valeurs cibles.*
- <def-of>`kernel`</def-of> : *Le noyau est une fonction mathématique qui transforme les données d'un espace de dimension initiale en un espace de dimension supérieure. Les noyaux permettent de résoudre des problèmes de séparation non linéaires en les transformant en problèmes de séparation linéaires dans un espace de dimension supérieure.*
- <def-of>`gamma`</def-of> : *Hyperparamètre qui influence la forme du noyau, il va chercher chercher à garder une marge aussi grande que possible tout en évitant qu'un datapoint se retrouve au milieu de la route. (Contrôle la bande passante de la guassienne)*

## Problématiques
1. Comment mettre en place une SVM ?

## Hypothèses
- <u>Le choix du kernel est le plus important pour avoir un bon critère de performance</u> <h-t/> :
    *il influence directement la capacité du modèle à représenter la relation entre les données d'entrée et la variable cible.*
- <u>SVR est robuste aux valeurs aberrantes</u> <h-t/> : *!;*
- <u>Pour définir un noyaux personalisé il faut une excellente connaissance à la fois du domaine d'application et à la fois du problème.</u> <h-t/> : *!;*
- <u>Dans la SVM, tous les points de données ne sont pas traités de manière égale</u> <h-t/> : *!;*
- <u>SVM n'est efficace que dans le cas des données linéairement séparables</u> <h-f/> : *!;*

## Plan d'action
1. Explorer les ressources
1. Définir et comprendre les mots clefs
1. Faire les Workshops
1. Utilisation du gridsearch et validation croisée pour trouver les hyperparamètres optimaux
1. Finaliser le RER


# RER

### Correlation
> Correlation measures the strength and direction of a linear relationship between two variables. It quantifies how changes in one variable correspond to changes in another. The correlation coefficient, typically denoted as “r” ranges from -1 to 1, where -1 indicates a perfect negative correlation, 1 signifies a perfect positive correlation, and 0 implies no correlation.

### Regression
> Regression, on the other hand, aims to predict the value of one variable based on the values of one or more other variables. It establishes an equation that describes the relationship between the variables. In simple linear regression, there is one predictor variable, while multiple linear regression involves more than one predictor.