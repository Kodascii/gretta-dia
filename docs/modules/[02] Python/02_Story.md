<link rel="stylesheet" href="../../stylesheet.css">

# Story_02 — Conditions & Booléens

## Contexte
> Se familiariser avec les conditions et les booléens.

## Mots clefs
- <def-of>Bloc de code</def-of> : *Section de code source dans un programme informatique qui est regroupée ensemble et exécutée comme une unité.* 
- <def-of>Condition</def-of> : *Expression qui peut-être évalué vraie ou fausse.* 
- <def-of>Alternative</def-of> : *Bifurcation dans l'exécution d'un programme en fonction d'une condition.* 
- <def-of>Structure de contrôle</def-of> : *Ensemble d'instructions qui détermine l'ordre d'exécution des instructions dans un programme.*
- <def-of>Structure conditionnelle</def-of> : *Construction qui permet d'exécuter des blocs de code en fonction de conditions spécifiques.* 
- <def-of>Structure de boucle</def-of> : *Construction de programmation qui permet d'exécuter un bloc de code de manière répétée tant qu'une certaine condition est vraie (boucle `while`) ou pour un nombre prédéterminé d'itérations (boucle `for`).* 
- <def-of>Variable booléen</def-of> : *Type de variable en programmation informatique qui peut avoir deux valeurs distinctes : `true` ou `false`.* 
- <def-of>Opérateurs booléens</def-of> : *Symbole ou mot-clef utilisé pour effectuer des opérations logiques entre des expressions booléennes* 
- <def-of>Opérateurs de comparaison</def-of> : *Symboles ou mot-clef, utilisés en programmation pour comparer deux valeurs et produire un résultat booléen (vrai ou faux) en fonction de la relation entre ces valeurs.* 
- <def-of>Test</def-of> : *Fait généralement référence à l'évaluation d'une condition ou d'un ensemble de conditions pour déterminer si une certaine partie du code doit être exécutée.* 
- <def-of>Tests imbriqués</def-of> : *Référence à l'utilisation de tests à l'intérieur d'autres tests, créant ainsi une structure hiérarchique de tests. Cette approche est souvent utilisée dans le contexte des tests unitaires.* 
- <def-of>Tests multiples</def-of> : *Référence à l'exécution de plusieurs cas de test dans le cadre d'une suite de tests. Dans le contexte des tests logiciels, une suite de tests est un ensemble organisé de cas de test qui vise à vérifier le bon fonctionnement d'un logiciel dans différentes situations.* 

## Problématiques
1. Dans quel contexte utiliser les booléens? 
1. Comment construire une structure conditionnelle? 
1. Comment modéliser les problèmes en termes de tests et d’alternatives?

## Hypothèses
- <u>`match` est une structure condtionnelle</u> <h-f/> : *Correspondance des modèles structurels.*
- <u>Il est possible d’avoir une condition sans les booléens</u> <h-t/>
- <u>Le nombre d’imbrications dans les conditions est infinie</u> <h-f/>
- <u>On ne peut avoir d’opérateurs de comparaison dans une condition</u> <h-t/>
- <u>Le ternaire existe en python.</u> <h-t/>
- <u>Il existe d’autres structures conditionnelles autres que if, elif and else</u> <h-t/>
- <u>Une condition ne peut avoir qu’une instruction (`if`)</u> <h-f/>
- <u>Une condition est une variable</u> <h-f/>
- <u>L’évaluation d’une condition ne peut avoir qu’une seule valeur</u> <h-t/>
- <u>On peut mettre deux conditions dans une même ligne</u> <h-t/>
- <u>`False == 0`</u> <h-t/>
- <u>Une condition peut être assigné avec une variable</u> <h-t/>


## Plan d'action
1. Explorer les ressources.
1. Définir les mots clés.
1. Vérifier les hypothèses.
1. Utiliser Jupyter Notebook pour tester toutes les notions abordées.
1. Faire les exercices dans le fichier : Booléens et les [conditions.ipynb](02_Conditions.ipynb).
1. Finaliser le RER.