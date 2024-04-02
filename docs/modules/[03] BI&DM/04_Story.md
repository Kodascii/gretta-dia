<link rel="stylesheet" href="../../stylesheet.css">

# Story_04 — Data Warehouse, ETL & OLAP

## Contexte
> .

## Mots clefs
- <def-of>OLAP (On-Line Analytical Processing)</def-of> : *Catégorie de technologies informatiques qui permettent aux utilisateurs d'interagir dynamiquement avec des données multidimensionnelles. Les systèmes OLAP sont conçus pour effectuer des analyses complexes et fournir une vue rapide et interactive des données à des fins d'exploration, de reporting et de prise de décision.*
- <def-of>OLTP (On-Line Transactional Processing)</def-of> : *Type de système de base de données utilisé dans les applications orientées transactions, telles que de nombreux systèmes opérationnels. « En ligne » signifie que ces systèmes sont censés répondre aux demandes des utilisateurs et les traiter en temps réel (traiter les transactions).*
- <def-of>ETL (Extract Transform Load)</def-of> : *Processus informatique utilisé pour déplacer et transformer des données d'un système source vers un système cible.*
    - **Extract** : *Pendant cette étape, les données sont extraites de différentes sources, telles que des bases de données, des fichiers plats, des API, etc. Cela peut impliquer l'extraction de données complètes ou seulement d'une partie des données, en fonction des besoins du process.*
    - **Transform** : *Une fois les données extraites, elles subissent une phase de transformation. Cela peut inclure le nettoyage des données, la normalisation, la conversion de formats, la suppression des doublons, etc. L'objectif est d'assurer que les données sont conformes aux besoins et aux standards du système cible.*
    - **Load** : *Dans cette étape, les données transformées sont chargées dans le système cible, tel qu'un entrepôt de données, une base de données relationnelle ou tout autre système de stockage approprié. Le chargement peut être effectué de manière incrémentielle ou en bloc, selon les exigences du processus.*
- <def-of>BI (Business Intelligence)</def-of> : *Ensemble de technologies, de processus et d'outils qui aident les entreprises à collecter, analyser et présenter des informations commerciales. L'objectif principal de la BI est de prendre des décisions éclairées pour améliorer les performances et la compétitivité d'une organisation.*
- <def-of>Granularité des données</def-of> : *Niveau de détail ou à la finesse avec laquelle les données sont représentées ou enregistrées. (Une granularité plus fine signifie que les données sont enregistrées avec plus de détails et de spécificités, tandis qu'une granularité plus grossière implique des données plus agrégées ou généralisées.)*
- <def-of>Dataware House</def-of> : *Base de données centralisée conçue pour stocker et gérer de grandes quantités de données provenant de différentes sources au sein d'une organisation. L'objectif principal d'une Data Warehouse est de fournir un environnement unique et intégré où les données peuvent être analysées et utilisées à des fins de prise de décision stratégique.*
- <def-of>Datamart</def-of> : *Sous-section spécialisée d'un entrepôt de données (Data Warehouse) qui est conçue pour répondre aux besoins spécifiques d'un groupe ou d'un département particulier au sein d'une organisation. Contrairement à un entrepôt de données, qui stocke des données à l'échelle de l'ensemble de l'entreprise, un Datamart est plus ciblé et orienté vers un domaine particulier ou une fonction spécifique.*
- <def-of>Dataverse</def-of> : *Application Web open source pour partager, préserver, citer, explorer et analyser des données de recherche.*
- <def-of>Donnée agrégé</def-of> : *Données qui ont été regroupées, combinées ou transformées d'une manière qui résume ou représente une vision plus globale ou synthétique des données sous-jacentes. L'agrégation de données est souvent utilisée dans le contexte de l'analyse de données, de la Business Intelligence et des rapports pour fournir une vue plus concise et informative des informations.*
- <def-of>Raw Data</def-of> : *Informations non traitées, non structurées ou non transformées qui ont été collectées directement à partir de sources d'origine.*
- <def-of>Meta Data</def-of> : *Données qui fournissent des informations sur d'autres données. En d'autres termes, ce sont des informations qui décrivent les caractéristiques, les propriétés, le contexte ou la structure des données.*
- <def-of>ERP (Enterprise Resource Planning)</def-of> : [**Système d'Entreprise**] *Système logiciel complet conçu pour aider les entreprises à intégrer et à gérer l'ensemble de leurs processus et flux de travail internes de manière centralisée. L'objectif principal d'un ERP est d'améliorer l'efficacité opérationnelle, d'optimiser l'utilisation des ressources et de faciliter la prise de décision en fournissant une vue consolidée et en temps réel de l'ensemble de l'entreprise.*
- <def-of>CRM (Customer RelationShip Management)</def-of> : *Stratégie d'entreprise axée sur la gestion des relations avec les clients et les prospects, ainsi qu'un ensemble de technologies informatiques et de logiciels conçus pour faciliter la mise en œuvre de cette stratégie.*
- <def-of>Modèle dimensionnel</def-of> : *L'objectif principal du modèle dimensionnel est de fournir une représentation des données qui soit intuitive et permette une récupération rapide et flexible des informations pour l'analyse.*
- <def-of>Reporting</def-of> : *Processus d'extraction, de présentation et d'analyse d'informations stockées dans une base de données afin de générer des rapports significatifs pour les utilisateurs finaux.*
- <def-of>MDX (Multidimensional Expressions)</def-of> : *Langage de requête utilisé principalement pour interagir avec des bases de données multidimensionnelles, telles que celles utilisées dans les systèmes de gestion de cubes OLAP.*
- <def-of>Power BI</def-of> : *Logiciel interactif de visualisation de données développé par Microsoft avec un accent principal sur la business intelligence.*
- <def-of>Mesure</def-of> : *Valeur quantitative qui représente une caractéristique spécifique des données stockées dans un cube OLAP.*
- <def-of>Dimension</def-of> : *Catégorie ou à un aspect particulier selon lequel les données peuvent être organisées et analysées dans un cube multidimensionnel.*

## Problématiques
1. 

## Hypothèses
- <u>Plus les transformations ETL sont complexes, plus la flexibilité des analyses OLAP est grande</u> <h-t/> : *!;*
- <u>ETL est le processus le plus complexe à mettre en place</u> <h-f/> : *L'installation des dépendences logiciels sur linux est plus complexe / Cela dépend du logiciel utilisé.*
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

| Caractéristique                   | OLTP                                                               | OLAP                                           |
|-----------------------------------|--------------------------------------------------------------------|------------------------------------------------|
| **Forme complète**                | Traitement en ligne des transactions                               | Traitement analytique en ligne                 |
| **Objectif principal**            | Soutenir les opérations transactionnelles quotidiennes             | Faciliter l'analyse complexe et les rapports   |
| **Type de données**               | Données actuelles, opérationnelles                                 | Données historiques, données agrégées          |
| **Structure des données**         | Bases de données relationnelles                                    | Cubes multidimensionnels ou bases de données relationnelles |
| **Conception de schéma**          | Conception de schéma normalisée                                    | Conception de schéma dénormalisée ou en étoile/flocon |
| **Type de requête**               | Transactions simples, fréquentes, courtes                          | Requêtes complexes, moins fréquentes, ad-hoc   |
| **Volume de transactions**        | Volume élevé de transactions courtes                               | Volume plus faible, requêtes analytiques complexes |
| **Temps de réponse**              | Faible latence, temps de réponse rapide                            | Tolérant aux temps de réponse plus longs       |
| **Normalisation**                 | Généralement fortement normalisé                                   | La dénormalisation est courante pour les performances |
| **Exemples de cas d'utilisation** | Traitement des commandes, gestion des stocks                       | Intelligence d'affaires, exploration de données |
| **Taille de la base de données**  | Généralement plus petite                                           | Peut être plus grande en raison du stockage des données historiques |
| **Sauvegarde et récupération**    | Sauvegardes fréquentes, récupération rapide                        | Sauvegardes moins fréquentes, accent sur l'analyse |
| **Index**                         | Ont tendance à avoir plus d'index pour la vitesse des transactions | Moins d'index pour optimiser les requêtes analytiques |
| **Granularité des données**       | Fines, enregistrements individuels                                 | Grossières, données agrégées                  |
| **Technologies exemples**         | MySQL, PostgreSQL, Oracle                                          | Microsoft SQL Server Analysis Services, SAP BW|
