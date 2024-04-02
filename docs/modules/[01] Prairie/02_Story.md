<link rel="stylesheet" href="../../stylesheet.css">

# Story_02 — Introduction aux bases des données

## Contexte
> Comprendre les bases de données et leur diversité.

## Mots clefs
- <def-of>Type de donnée</def-of> : *String/Numeric/Date&Time.*
- <def-of>SQL (Structured Query Language)</def-of> : *Language informatique destiné à exploiter des bases de données relationnelle.*
- <def-of>Big Data</def-of> : *Large données, qui peut être analyser pour révéler des modèles.*
- <def-of>NoSQL (Not Only SQL)</def-of> : *Famille de SGBD non relationnel (structuré, semi-structuré & non-structuré).*
- <def-of>SGBD (System de Gestion de Bases de Données)</def-of> : *Logicle destiné au stockage et la manipulation des bases de données relationnelle.*
- <def-of>Client</def-of> : *Logiciel qui envoie des demandes à un serveur.*
- <def-of>Serveur</def-of> : *Logiciel qui offre des services à un ou plusieurs clients.*
- <def-of>BDD</def-of> : *Ensemble de données stocké sur un support informatique.*
  - <def-of>(relationnelle)</def-of> : *Ensembles d'informations qui organise les données dans des relations prédéfinies et les stockent dans les tableaux.*
  - <def-of>(no relationnelle)</def-of> : *Stockage de donnée indexée. Format clef-valeur.*
- <def-of>Enregistrement</def-of> : *Donnée composite qui comporte plusieurs champs dans chacun desquels est enregistrée une donnée.*
- <def-of>Donnée</def-of>
  - <def-of>(structurée)</def-of> : *Donnée formaté selon une organisation adapté.*
  - <def-of>(semi-structurée)</def-of> : *Donnée dont certaines des informations leurs sont associé via des meta-données.*
  - <def-of>(non-structurée)</def-of> : *Données non-structurés décrite par des métadonnées structurés.*
- <def-of>Information</def-of> : *Ensemble des données traités et organiser d'une manière compréhensible dans un context spécifique.*
- <def-of>Big Data</def-of> : *Ressources d'informations dont les caractéristiques en termes de volume, de velocité, et de variaté imposent l'utilisation de technologies et des méthodes analytiques particulières pour créer de la valeur, et qui dépassent en général les capacités d'une seule et unique machine et nécessitent des traitements parallélisés.*
- <def-of>Champs</def-of> : *Un attribut, une caractéristique décrivant les valeurs de la colonne d'une table.*

## Problématiques
1. *Comment organiser une base de données ?*

## Hypothèses
- <u>Peux-t'on mettre toutes les données en une seul table ?</u> <h-t/>
- <u>NoSQL n'utilise pas SQL</u> <h-f/> :
  *Les systèmes NoSQL peuvent prendre en charge des langages de requête de type SQL ou s'associer à des bases de données SQL dans des architectures polyglottes persistantes.*
- <u>Les BDD ont un language universel</u> <h-f/>
- <u>Toutes les BDD ont le même système de sécurité</u> <h-f/>
- <u>Le language SQL est le plus utilisé concernant les BDD</u> <h-t/>
- <u>Toutes les données sont importantes</u> <h-f/>
- <u>Pour construire une BDD il faut avoir la connaissance des différents types de données</u> <h-t/>

## Plan d'action
1. Investigation des ressources;
2. Chercher l'histoire des bases de données;
3. Observer les differences entre les BDD's, en comparant dans un tableau;
4. Définitions des mots clefs (*bref*);
5. Vérifier les hypothèses;
6. Répondre aux questions.

# RER

## Histoire
> Le concept de base de donnée fût possible grâce à l'émergence des supports de stockages avec un accès direct à la mémoire comme les disques magnétiques au milieu des années <u>1960</u>.

Au début, les deux principaux models utilisé fûrent:
- **Modèle hiérarchique :** *les données sont organisées en structure arborescente*.
- **Modèle réseau :** *extension du modèle hiérarchique* 

> Dans les années <u>1970</u> le modèle relationnelle fût proposé en partant de l'idée que les applications devraient chercher la donnée par le contenue, et non par liens.

> Dans les années <u>1980</u>, les bases de données d'objets sont apparue.

> À la fin des années <u>2000</u>, la prochaine génération de bases de données post-relationnelles est devenue connue sous le nom de bases de données NoSQL.

## Différences entre les BDD's

|                 | SQL           | MySQL         | PostgreSQL       | NoSQL             |
|-----------------|---------------|---------------|------------------|-------------------|
| **Paradigm**    | Relationnelle | Relationnelle | Relationnelle    | Non-Relationnelle |
| **Donnée**      | Structuré     | Structuré     | Structuré & Semi | *                 |
| **Rapidité**    | Lente         | Lente         | Lente            | Rapide            |
| **Flexibilité** | Moindre       | Moindre       | Moindre          | Supérieur         |

# Extras
- **NoSQL:** *NoSQL systems may support SQL-like query languages or sit alongside SQL databases in polyglot-persistent architectures.*
- **[Polyglot persistence](https://en.wikipedia.org/wiki/Polyglot_persistence):** *is a term that refers to using multiple data storage technologies within a single system, in order to meet varying data storage needs. Such a system may consist of multiple applications, or it may be a single application with smaller components.*