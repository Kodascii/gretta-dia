<link rel="stylesheet" href="../../stylesheet.css">

# Story_01 — Merise & MCD/MPD

## Contexte
> Concevoir et réaliser une base de données, ainsi que comprendre les modèles MCD, MLD et MPD.

## Mots clefs
- <def-of>Attribut</def-of> : *Les entités sont caractérisées par des attributs qui décrivent différentes propriétés ou caractéristiques de l'entité. (Par exemple, un client pourrait avoir des attributs tels que "Nom", "Adresse", et "Numéro de téléphone".)*
- <def-of>Cardinalité</def-of> : *Couples de valeur qui apportent des contraintes sur le MCD. Elles traduisent des règles de gestion — Dans le modèle UML on parle alors de multiplicité : c’est le nombre de relations possibles entre types. Si une classe « ville » peut avoir 10 « structures », il y a multiplicité 0..10.*
- <def-of>CIF (Contraintes d'Intégrité Fonctionnelle)</def-of> : *Dépendance fonctionnelle entre plusieurs entités. Il garantit la cohérence fonctionnelle des données.*
- <def-of>Dépendance Fonctionnelle</def-of> : *Formellement, dans une table relationnelle, une dépendance fonctionnelle est notée comme A → B, où A et B sont des ensembles d'attributs (colonnes). Cela signifie que, pour chaque combinaison unique de valeurs dans les colonnes A, il existe une seule valeur correspondante dans la colonne B.*
    - <def-of>— Complète</def-of> : *A → B, où B dépend entièrement de A, et si nous retirons n'importe quel attribut de A, la dépendance fonctionnelle ne tiendra plus.*
    - <def-of>— Transitive</def-of> : *Si A → B et B → C, alors A → C. Cela signifie que la dépendance fonctionnelle se propage à travers une autre colonne.*
    - <def-of>— Partielle</def-of> : *Si A → B, mais B dépend également d'un autre attribut C, alors il y a une dépendance fonctionnelle partielle.*
- <def-of>Dictionnaire de données</def-of> : *Ensemble organisé d'informations détaillées sur les données utilisées dans un système d'information ou une base de données. Il s'agit d'une documentation qui fournit une description détaillée de chaque élément de données, y compris sa signification, sa source, son format, sa relation avec d'autres données, etc. Ce dictionnaire joue un rôle essentiel dans la gestion des données et la communication entre les équipes techniques et non techniques au sein d'une organisation.*
- <def-of>Entité</def-of> : *Unité symbolique ou concrète, équivalente à un objet (classe ou occurrence) dans un MCD.*
- <def-of>Formalisme</def-of> : *Ensemble de règles utilisées pour représenter les modèles de données.*
- <def-of>Héritage</def-of> : *Partage d'attributs commun entre différentes entités.*
- <def-of>Looping</def-of> : *Lociel de modélisation conceptuelle de données (*entièrement gratuit et libre d'utilisation*).*
- <def-of>Merise</def-of> : *Méthode pour rassembler les idées sans effort, ou encore, vient du merisier qui est un porte-greffe.*
- <def-of>[1] MCD (Modèle Conceptuel des Données)</def-of> : *Représentation graphique de haut niveau qui permet facilement et simplement de comprendre comment les différents éléments sont liés entre eux.*
- <def-of>[2] MLD (Modèle Logique des Données)</def-of> : *Transformation du MCD en ensembles de tables avec des champs et des clefs.*
- <def-of>[3] MPD (Modèle Physique des Données)</def-of> : *Étape permettant de construire la structure finale de la base de données avec les différents liens entre les éléments qui la composent (*usage de SQL*).*
- <def-of>MER (Modèle Entité-Relation)</def-of> : *Modèle conceptuel qui utilise des entités, des relations et des attributs pour représenter graphiquement la structure d'une base de données.*
- <def-of>Normalisation</def-of> : *Processus de conception qui vise à organiser les données de manière efficace pour réduire la redondance et améliorer l'intégrité des données.*
    - <def-of>— Première Forme Normale (1NF)</def-of> : *Une table est en 1NF si elle ne contient pas de valeurs répétées ou de groupes de valeurs atomiques. Chaque colonne de la table doit contenir une seule valeur et ne doit pas être une liste ou un ensemble de valeurs.*
    - <def-of>— Deuxième Forme Normale (2NF)</def-of> : *Une table est en 2NF si elle est en 1NF et si toutes ses dépendances fonctionnelles dépendent de la totalité de la clé primaire. Cela signifie qu'il ne doit pas y avoir de dépendance partielle de la clé primaire.*
    - <def-of>— Troisième Forme Normale (3NF)</def-of> : *Une table est en 3NF si elle est en 2NF et si elle ne contient pas de dépendances transitives entre les colonnes non clés. En d'autres termes, toutes les colonnes non clés doivent dépendre uniquement de la clé primaire.*
- <def-of>Règle de gestion</def-of> : *Besoin et exigence organisationnelle. Contraintes légale fournis par le client.*
- <def-of>Relation</def-of> : *Liens entre 2 entités dans un MCD qui décrit comment ces entités partagent des informations dans la base de données.*
- <def-of>PowerAMC</def-of> : *Outil, utilisé pour concevoir et modéliser des bases de données, ainsi que d'autres éléments tels que des architectures d'entreprise, des modèles UML, etc.*
- <def-of>Sémantique</def-of> : *Etude du sens et des références selon le contexte.*
- <def-of>UML (Unified Modeling Language)</def-of> : *Langage de modélisation visuelle utilisé pour concevoir, spécifier et documenter les systèmes logiciels. Modèle graphique adapter au langage orienté objet.*

## Problématiques
1. Comment concevoir une base de donnés avec la méthode Merise ?
1. Comment stucturé les données et construire le MCD ?

## Hypothèses
- <u>Une base de données contient forcément plusieurs fichiers</u> <h-f/>
    - **Bases de données monolithiques** : *Dans ce cas, toute la base de données est stockée dans un seul fichier ou un ensemble de fichiers très étroitement liés.*
    - **Bases de données distribuées** : *Ces bases de données sont réparties sur plusieurs fichiers ou serveurs, ce qui permet de gérer de grandes quantités de données de manière plus efficace.*
- <u>On peut se passer de la méthode Merise pour créer une base de données</u> <h-t/>
- <u>Une table peut avoir plusieurs clefs étrangères</u> <h-t/>
- <u>On peut créer un MPD avant un MCD</u> <h-f/>
- <u>Le MPD est identique au MCD </u> <h-f/>
    - *Ce sont deux étapes distinctes dans le processus de conception d'une base de données. Ils représentent différents niveaux d'abstraction et servent des objectifs différents.*
- <u>La méthode Merise est la meilleure méthode pour concevoir une base de données</u> <h-f/>
    - *Il est important de noter que l'adéquation d'une méthodologie dépend des besoins spécifiques du projet, de la complexité de l'application, des compétences de l'équipe de développement et d'autres facteurs.*
- <u>Il est possible de relier une entité a elle-même</u> <h-t/>
    - *Cela s'appelle une "relation réflexive" ou "auto-association".*
- <u>La phase de modélisation d’une BDD est facultative</u> <h-t/>
- <u>Modifier le schéma d’une BDD peut permettre d’ajouter une couche de sécurité</u> <h-t/>
    - **Normalisation et Restructuration** : *Une bonne conception de base de données, y compris la normalisation, peut contribuer à améliorer la sécurité en réduisant les risques liés à la redondance des données. La normalisation peut également faciliter la gestion des autorisations d'accès en permettant des contrôles plus granulaires sur les tables.*
    - **Ajout de Contraintes d'Intégrité** : *L'ajout de contraintes d'intégrité, telles que les clés étrangères, peut garantir la cohérence des données et prévenir les manipulations indésirables. Cela peut être particulièrement important pour éviter les attaques telles que l'injection de données.*
    - **Contrôles d'Accès Renforcés** : *La modification du schéma pour mettre en place des contrôles d'accès basés sur les rôles, les utilisateurs et les privilèges peut améliorer la sécurité en garantissant que seules les personnes autorisées ont accès aux données.*
- <u>Pour faire une relation entre 2 tableaux il n’est pas nécessaire d’avoir une clef étrangère</u> <h-t/>
    - *(à éviter)*

## Plan d'action
1. Investigation des ressources;
1. Définitions des mots clefs;
1. Vérifier les hypothèses;
1. Faire le workshop;
1. Répondre aux questions.

# RER

## Lecture MLD
- Chaque ligne représente une table;
- C’est toujours le nom de la table qui est écrit en premier;
- Les champs sont listés entre parenthèses et séparés par des virgules;
- Les clés primaires sont soulignées et placées au début de la liste des champs;
- Les clés étrangères sont préfixées par un dièse.

## Changement de vocabulaire entre MCD et MPD
- Une entité du MCD devient une table;
- L'identifiant de l'entité devient la clé primaire de la table;
- Les autres propriètes de l'entité se transforme en champs (ou attributs) de la table;
- Les identifiants se transforment en clés et se retrouvent soulignés. Chaque table dispose d’au minimum 1 clé dite primaire;
- Les relations et les cardinalités se transforment en champs anoté d'un `#` : il s’agit de créer des « clés étrangères » reliées à une « clé primaire » dans une autre table.

## Règles pour les relations du MCD
### Relation type Père-Fils
- (**cardinalité entité « père » : `0/1, N`**) et (**cardinalité entité « fils » : `0/1, 1`**)
- L'identifiant de l'entité « père » devient attribut de la table « fils » (*clé étrangère*).

### Relation type Père-Père
- (**cardinalité entité « père(s) » : `0/1, N`**)
- La relation devient une table
    - les champs de cette table sont la concatenation des clés primaires des tables correspondantes.