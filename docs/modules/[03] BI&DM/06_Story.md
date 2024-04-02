<link rel="stylesheet" href="../../stylesheet.css">

# Story_06 — Systèmes Décisionnels & Data Mining

## Contexte
> Se familiariser avec l'extraction de règles d'associations et les systèmes experts (aussi appelées systèmes décisionnels).

## Mots clefs
- <def-of>Système expert / système décisionnel</def-of> : *Processus d'exploration et d'analyse de grandes quantités de données pour extraire des modèles significatifs, des tendances ou des relations cachées donc des connaissances.*
- <def-of>Règle d’association</def-of> : *Relations logiques qui mettent en évidence des corrélations fréquentes entre les variables d'un ensemble de données.*
- <def-of>Market Basket Analysis</def-of> : *Méthode d'apprentissage automatique basée sur des règles pour découvrir des relations entre les variables.*
- <def-of>Apriori</def-of> : *Algorithme de data mining utilisé pour extraire des règles d'association à partir d'ensembles de données.*
- <def-of>SID (Système d'Information Décisionnel)</def-of> : *Outil de Business Intelligence (BI) visant à aider les entreprises à prendre des décisions commerciales éclairées sur la base de grandes quantités de données analysées.*
- <def-of>Support</def-of> : *Fréquence d'apparition d'un ensemble d'items dans un ensemble de données.*
    $s(X) = \sigma(X) / |\Omega|$
- <def-of>Confidence</def-of> : *Probabilité qu'une règle d'association spécifique soit vraie.*
    $c(X \rightarrow Y) = s(X \cup Y) / s(X)$
- <def-of>Lift</def-of> : *Force de l'association entre deux ensembles d'items (antécédent et conséquent) dans une règle d'association en comparaison avec ce à quoi on pourrait s'attendre au hasard.*
    $\ell(X \rightarrow Y) = c(X \rightarrow Y) / s(Y)$
- <def-of>FP-Tree</def-of> : *Structure de données compacte utilisée pour représenter les ensembles d'articles fréquents dans le processus d'extraction de règles d'association.*
- <def-of>Méthode d'inférence</def-of> : *Composant d'un système expert conçu pour appliquer des règles logiques aux bases de connaissances et afin d'en déduire de nouvelles informations (faits) ou prendre des décisions.*

## Problématiques
1. Comment choisir le bon outil d'analyse de donnée ?
1. Comment impémenter l'algorithme apriori en python ?
1. Comment trouver des modèles communs d'éléments (des règles d'associations) ?

## Hypothèses
- <u>LIFT est un ratio de probabilité</u> <h-t/> : *!;*
- <u>L’incorporation des techniques de Data Mining dans les systèmes décisionnels optimisent la précision des prédictions</u> <h-t/> : *!;*
- <u>Le SID et le BI sont la même chose</u> <h-t/> : *!;*
- <u>Extend est une libraire utilisé pour les systèmes décisionnels</u> <h-t/> : *!;
- <u>Les systèmes décisionnels sont réservés aux grosses entreprises</u> <h-t/> : *!;*
- <u>Mlxtend est une librairie utile pour les systèmes décisionnels</u> <h-t/> : *!;*
- <u>?</u> <h-t/> : *!;*
- <u>?</u> <h-t/> : *!;*

## Plan d'action
1. Investigation des ressources
6. Définitions des mots clefs;
7. Vérifier les hypothèses;
8. Répondre aux questions.

# RER

> Any rule consists of two parts: the `if` part, called the **antecedent** (***premise*** or ***condition***) and the `then` part called the **consequent** (***conculsion*** or ***action***).
```
if   <premise>
then <action>
```

## Questions
