<link rel="stylesheet" href="../../stylesheet.css">

# Story_02 — MySQL

## Contexte
> Créer ou administrer une base de donnée, pour une organisation. Avec ou sans GUI.

## Mots clefs
- <def-of>Administrer</def-of> : *Ensemble des activités liées à la gestion, à la configuration, à la surveillance et à la maintenance de la base de données.*
- <def-of>GUI (Graphical User Interface)</def-of> : *Permet de naviger avec des composant graphiques pluôt qu'en ligne de commande.*
- <def-of>PhpMyAdmin</def-of> : *GUI pour gérer une base de données MySQL sur un serveur PHP.*  
- <def-of>Requête</def-of> : *Instruction qui permet de faire une opération sur des données dans un SGBD.*
- <def-of>IDE (Integrated Development Environment)</def-of> : *Application logicielle qui aide les programmeurs à développer efficacement du code logiciel.*
- <def-of>Principe Server-Client</def-of> : *Modèle de communication dans lequel un programme (le serveur) fournit des services ou des ressources à d'autres programmes (les clients). *
- <def-of>Script d'import</def-of> : *Ensemble d'instruction pour importer des données de fichiers externes dans une BDD.*
- <def-of>`cursor()`</def-of> : *Crée un objet lié à la classe `connect`, qui permet de passer des requêtes MySQL, et de récuperer le résultat.*
- <def-of>`execute()`</def-of> : *Execute une requête sur la BDD sur laquelle le `cursor` est ouvert.*
- <def-of>`fetchone()`</def-of> : *Retourne un tuple or `None`: Une ligne du jeu de résultats de la requête.*
- <def-of>`fetchmany()`</def-of> : *Renvoye une liste d'enregistements d'une table (ou une liste vide si aucun enregistrement).*
- <def-of>`fetchall()`</def-of> : *Récupère toutes les lignes du résultat d'une requête. (Retourne une liste de tuples)*
- <def-of>`commit()`</def-of> : *Valide la transaction en cours.*
- <def-of>`rollback()`</def-of> : *Annule la transaction en cours.*
- <def-of>`WHERE`</def-of> : *Clause SQL pour spécifier les conditions de filtrages dans une requête.*


## Problématiques
1. Comment choisir son SGDB
1. Comment gérer un SGBD
1. Comment connecter une BDD à un programme python ?

## Hypothèses
- <u>On peut accéder à une base de donnée en python sans usage d'un serveur pour un SGBD.</u> <h-t/>
    - *Il est possible d'accéder aux données sans serveur, mais, cela risque de compromettre la sécurité, les performances et l’intégrité des données.*
- <u>On peut exporte une base de donne en ligne de commande.</u> <h-t/>

## Plan d'action
1. Investigation des ressources
1. Définitions des mots clefs;
1. Vérifier les hypothèses;
1. Répondre aux questions.
1. Install MySQL et phpMyAdmin
1. Comparer MySQL Workbench avec PHPMyAdmin
1. Faire le workshop
1. Rendres livrables (en JNB)