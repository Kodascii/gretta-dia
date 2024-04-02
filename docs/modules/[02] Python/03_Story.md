<link rel="stylesheet" href="../../stylesheet.css">

# Story_03 — [Les Boucles](https://courspython.com/boucles.html)

## Contexte
> Se familiariser avec les différents types de boucles.

## Mots clefs
- <def-of>Boucle</def-of> : *Structure de contrôle permettant d'itérer l'exécution d'un bloc tant qu'une condition est respecté. (Boucle bornée, ou non bornée.)*
- <def-of>Boucle bornée</def-of> : *Boucle permettant d'itérer sur une séquence prédéfinie d'éléments.*
- <def-of>Boucle non bornée</def-of> : *Boucle permettant de répéter l'exécution d'un bloc, tant qu'un condition est vraie.*
- <def-of>Boucle imbriqué</def-of> : *Boucle à l'intérieur d'une autre boucle.*
- <def-of>Liste en compréhension</def-of> : *Manière concise de créer des listes. Elle permet de générer des listes en une seule ligne de code en utilisant une syntaxe compacte et expressive.*
- <def-of>Itération</def-of> : *Répétition d'un bloc d'instructions ou d'une séquence de code plusieurs fois.*
- <def-of>Pas</def-of> : *Quantité d'incrémentation.*
- <def-of>Récursivité</def-of> : *Capacité d'une fonction ou d'un algorithme à s'appeler elle-même.*
- <def-of>`def `</def-of> : *Mot-clef python, désignant le début de la déclaration d'une fonction.*
- <def-of>`range()`</def-of> : *Fonction pré-définie générant une séquence de nombres contenue dans l'interval donné.*
- <def-of>`None`</def-of> : *Type d'objet spécial qui représente l'abscence de valeur dans la variable. C'est un singleton, il n'existe qu'une seule instance dans un programme python.*
- <def-of>`for`</def-of> : *Mot-clef python, désignant le début d'une boucle bornée.*
- <def-of>`while`</def-of> : *Mot-clef python, désignant le début d'une boucle non bornée.*
- <def-of>`pass`</def-of> : *Insstruction python, ne faisant rien.*
- <def-of>`return`</def-of> : *Utilisé dans une fonction pour renvoyer une valeur spécifique.*
- <def-of>`break`</def-of> : *Instruction python, permettant de sortir d'une boucle.*
- <def-of>`continue`</def-of> : *Instruction python, permettant de passer à l'itération suivante de la boucle.*

## Problématiques
1. Comment utiliser les boucles pour résoudre un problème ? 
1. Comment choisir la boucle adéquate ? 
1. Comment faire pour qu’une boucle ne tourne pas à l’infini ? 
1. Comment connaitre le nombre d’itération pour une boucle ? 

## Hypothèses
- <u>Il n’y a que 2 types de boucles</u> <h-t/> : *`while` et `for`.*
- <u>Il faut indenter les structures de boucle</u> <h-t/>
- <u>On peut faire une boucle qui se décrémente</u> <h-t/>
- <u>On peut mettre un `for` dans un `while` et inversement</u> <h-t/>
- <u>`match` est un type de boucle</u> <h-f/>
- <u>Une boucle bornée peut s’écrire comme une boucle non bornée</u> <h-t/>
- <u>Toutes les boucles sont infinies </u> <h-f/>
- <u>On peut sortir d’une boucle quand l’on veut </u> <h-t/> : 
    *En utilistant `break`.*
- <u>La fonction `range()` est importante pour la boucle `for`</u> <h-t/>
- <u>Imbriqué des boucles n’a pas d’impact sur la lourdeur du programme</u> <h-t/>
- <u>Il n'existe pas de `do-while` en python</u> <h-t/>
- <u>On peut annoter les boucles en python</u> <h-f/>
- <u>On peut utiliser des opérateurs de comparaisons dans les boucles</u> <h-t/>

## Plan d'action
1. Investigation des ressources
1. Définitions des mots clefs;
1. Vérifier les hypothèses;
1. Répondre aux questions.