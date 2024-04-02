<link rel="stylesheet" href="../../stylesheet.css">

# Story_04 — Structures de données

## Contexte
> Ce familiariser avec les différents structures de données.

## Mots clefs
- <def-of>Collection (Python):</def-of> *La plus part des structures de données en python sont considérées comme des collections. Cependant, il existe d'autres types de données qui ne sont pas strictement considérés comme des collections, comme les types numériques, les booléens, les ensembles immuables (`frozenset`), etc - ces types représentent des valeurs individuelles plutôt que des collections d'éléments.*
- <def-of>Dictionnaire</def-of> : *Structure de données permetant de stocker des paires clé-valeur, où chaque clé doit être unique.*
- <def-of>Liste</def-of> : *Structure de données qui permet de stocker un ensemble ordonnée d'éléments..*
- <def-of>Liste imbriquée</def-of> : *Tableau multi-dimensionnel.*
- <def-of>Tuple</def-of> : *Structure de données similaire à une liste, mais avec une différence principale : les tuples sont immuables.*
- <def-of>Indice</def-of> : *Position d'un élément dans une collection.*
- <def-of>Mutable</def-of> : *Terme d'écrivant un object dont l'état peut-être modifié après sa création.*
- <def-of>Object ordonné</def-of> : *Structure de données où l'ordre des éléments est significatif.*
- <def-of>Object non ordonné</def-of> : *tructure de données où l'ordre des éléments est insignifiant..*
- <def-of>Séquence</def-of> : *Collection ordonnée d'éléments.*
- <def-of>Méthode</def-of> : *Fonction associé à un object.*
- <def-of>`len()`</def-of> : *Renvoie la longueur (le nombre d'éléments) d'un objet. L'argument peut être une séquence (telle qu'une chaîne, des octets, un tuple, une liste ou une plage) ou une collection (telle qu'un dictionnaire, un ensemble ou un ensemble figé).*
- <def-of>`.keys()`</def-of> : *Renvoie une nouvelle vue des clés du dictionnaire..*
- <def-of>`.values()`</def-of> : *Renvoie une nouvelle vue des valeurs du dictionnaire.*
- <def-of>`.items()`</def-of> : *Renvoie une nouvelle vue des éléments du dictionnaire (paires (`key`, `value`)).*
- <def-of>`.append(x)`</def-of> : *Ajoute x à la fin de la séquence*

## Problématiques
1. Quels structures de données adaptés aux différents cas?
1. Quels sont les avantages et les inconvenients de chaque structure de données?

## Hypothèses
- <u>On peut sélectionner plusieurs valeurs dans une liste</u> <h-t/>
- <u>On peut sélectionner plusieurs valeurs dans une liste</u> <h-t/>
- <u>On peut mettre un tuple en clé de dictionnaire</u> <h-t/>
- <u>On peut représenter un tableau comme une liste</u> <h-t/>
- <u>Les dictionnaires permettent d’accéder aux valeurs grâce aux clés</u> <h-t/>
- <u>Il est possible d’imbriquer un dictionnaire dans un autre</u> <h-t/>
- <u>On peut cibler une donnée précise dans un dictionnaire</u> <h-t/>
- <u>On peut utiliser une liste pour tous les types de données</u> <h-t/>
- <u>On peut agrandir une liste à l’infini</u> <h-t/>
- <u>Une liste peut être non modifiable</u> <h-t/>
- <u>Toutes les collections python sont mutables</u> <h-t/>
- <u>Il est plus efficace de chercher dans un dictionnaire que dans une liste</u> <h-t/>
- <u>On ne peut pas utiliser un dictionnaire sans accolade</u> <h-t/>
- <u>Pour des opérations de lecture fréquentes, il est préférable d’utiliser les tuples, que les dictionnaires ou les listes</u> <h-t/>


## Plan d'action
1. Investigation des ressources;
1. Définitions des mots clefs;
1. Vérifier les hypothèses;
1. Répondre aux questions;
1. Faire le tableau avatages/inconvénients;
1. Faire le workshop;

# RER

## Différences entre structures de données

| Collection                 | Ordre | Modifiable | Indexé | Doublons autorisés |
|----------------------------|-------|------------|--------|--------------------|
| **Liste (`list`)**         | Oui   | Oui        | Oui    | Oui                |
| **Tuple (`tuple`)**        | Oui   | Non        | Oui    | Oui                |
| **Ensemble (`set`)**       | Non   | Oui        | Non    | Non                |
| **Dictionnaire (`dict`)**  | Non   | Oui        | Oui    | Clés uniques       |

# Extras
- **`len(s)` :** *Return the length (the number of items) of an object. The argument may be a sequence (such as a `str`, `bytes`, `tuple`, `list`, or `range()`) or a collection (`dict`, `set`, or `frozenset`).*