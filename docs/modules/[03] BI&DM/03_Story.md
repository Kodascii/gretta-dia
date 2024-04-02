<link rel="stylesheet" href="../../stylesheet.css">

# Story_03 — CRUD + Jointure

## Contexte
> Se familiariser avec les opérations dans une base de donnée CRUD.
> Savoir réaliser des requêtes sur plusieurs tables avec des différents types de jointures.

## Mots clefs
- <def-of>Jointure</def-of> : *Opération permettant de combiner les lignes de deux ou plusieurs tables en fonction d'une condition de relation entre les colonnes de ces tables.*
    - <def-of>`LEFT JOIN`</def-of> : *Retourne toutes les lignes de la table de gauche (première table spécifiée) et les lignes correspondantes de la table de droite. Si aucune correspondance n'est trouvée dans la table de droite, les colonnes de cette table contiennent des valeurs `NULL`.*
    - <def-of>`RIGHT JOIN`</def-of> : *L'inverse du Left Join. Retourne toutes les lignes de la table de droite avec les lignes correspondantes de la table de gauche. Si aucune correspondance n'est trouvée dans la table de gauche, les colonnes de cette table contiennent des valeurs `NULL`.*
    - <def-of>`INNER JOIN`</def-of> : *Retourne uniquement les lignes où il y a une correspondance entre les colonnes spécifiées dans les deux tables. Les lignes pour lesquelles aucune correspondance n'est trouvée sont exclues du résultat.*
    - <def-of>`FULL OUTER JOIN`</def-of> : *Retourne toutes les lignes lorsque des correspondances sont trouvées dans l'une ou l'autre des tables. Les colonnes sans correspondance contiennent des valeurs NULL*
- <def-of>CRUD (Create Read Update Delete)</def-of> : *L'ensemble de ces quatre opérations couvre l'ensemble des actions de manipulation de données dans un système informatique.*
- <def-of>Fonction d'agrégation</def-of> : *Fonction qui effectue un calcul sur un ensemble de valeurs et retourne une seule valeur résumée. (`SUM`, `AVG`, `MIN`, `MAX`, etc.)*
- <def-of>Clause</def-of> : *Partie spécifique d'une instruction SQL qui précise des conditions, des filtres ou des actions particulières à appliquer.*
- <def-of>SQLAlchemy</def-of> : *Bibliothèque Python qui fournit un ensemble d'outils et de fonctionnalités pour faciliter l'interaction avec les bases de données relationnelles.*

## Problématiques
1. Comment utiliser les différents types de jointures.
1. Comment utiliser les différentes opérations CRUD.
1. Comment faire des requêtes SQL avancée.

## Hypothèses
- <u>Les jointures fonctionne de manière similaire aux opérations ensemblistes</u> <h-t/>
    - *Voir algèbre relationnelle.*
- <u>On peut faire une requête SQL dans une requête SQL</u> <h-t/>
- <u>Une jointure peut se faire que entre deux tables</u> <h-t/>
- <u>On peux renvoyer une jointure sql ou une requéte au format JSON</u> <h-t/>
- <u>Le caractère `%` permet de représenter n'importe quel caractère</u> <h-t/>
- <u>La fonction d'agrégation est une simple opération de concatenation de deux tables</u> <h-t/>


## Plan d'action
1. Investigation des ressources
6. Définitions des mots clefs;
7. Vérifier les hypothèses;
8. Répondre aux questions.

# RER