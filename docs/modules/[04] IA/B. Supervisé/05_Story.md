<link rel="stylesheet" href="../../../stylesheet.css">

# Story_05 — Flask

## Contexte
> Introduction au développement web avec le Framework Flask, comprendre et apprendre 2 langages : HTML et CSS.

## Mots clefs
- <def-of>HTML (HyperText Markup Language)</def-of> : *Language de balisage front-end, pour la création des pages web.*
- <def-of>CSS (Cascading StyleSheet)</def-of> : *Feuille de style.*
- <def-of>Flask</def-of> : *Flask est un micro framework d'application Web WSGI léger.*
- <def-of>Django</def-of> : *Framework Web Python qui permet le développement rapide de sites Web sécurisés et maintenables.*
- <def-of>GET</def-of> : *Méthode HTTP utilisée par les navigaterus pour ajouter les champs du formulaire à l'URL, encombrant la barre d'adresse du navigateur.*
- <def-of>POST</def-of> : *Méthode HTTP utilisée par les navigateurs pour soumettre les données du formulaire dans le corps de la demande.*
- <def-of>Postman</def-of> : *Application qui permet de créer et tester des API's web. Postman simplifie chaque étape du cycle de vie de l'API et rationalise la collaboration.*
- <def-of>ORM (Object Relational Mapping)</def-of> : *Technique de programmation pour convertir des données entre une base de données relationnelle et le tas d'un langage de programmation orienté objet.*
- <def-of>Environnement virtuel</def-of> : *Isole les dépendances d'un projet Python, y compris les bibliothèques et les interpréteurs de version.*
- <def-of>Microblog/Blog</def-of> : **
- <def-of>Werkzeug</def-of> : *Bibliothèque complète d'applications Web WSGI.*
- <def-of>WSGI (Web Server Gateway Interface)</def-of> : *Standard spécifiant comment un serveur Web peut interagir avec une application Python.*

## Problématiques
1. Comment utiliser Flask  et les langages HTML et CSS ? 
1. Comment bien développer un site web en utilisant Python ? 

## Hypothèses
- <u>On peut utiliser des templates en format HTML, pour l'injecter dans flask.</u> <h-t/> : *!;*

## Plan d'action
1. Investigation des ressources
6. Définitions des mots clefs;
7. Vérifier les hypothèses;
8. Répondre aux questions.

# RER

### Django vs. Flask

| Caractéristique                | Django                                 | Flask                                  |
|------------------------------- |----------------------------------------|----------------------------------------|
| **Architecture**               | Basé sur le modèle MTV (Model-Template-View) | Basé sur un modèle simple, flexible et extensible |
| **Abstraction de la base de données** | Fournit une ORM intégrée pour la gestion des bases de données | Peut utiliser des extensions pour l'ORM, telles que SQLAlchemy |
| **Conventions**                | Suit des conventions strictes par défaut | Suit le principe "micro" et encourage la flexibilité et la liberté |
| **Évolutivité**                | Convient bien aux applications de taille moyenne à grande | Convient bien aux petites et moyennes applications, mais peut être étendu avec des extensions |
| **Inclus**                     | Fournit un ensemble complet de fonctionnalités intégrées (administration, authentification, etc.) | Offre des fonctionnalités de base, mais encourage l'utilisation d'extensions pour des besoins spécifiques |
| **Flexibilité**                | Moins flexible en termes de structure du projet | Offre une grande flexibilité, laissant au développeur la liberté de structurer le projet comme il le souhaite |
| **Complexité**                 | Peut être perçu comme plus complexe en raison de sa richesse en fonctionnalités | Plus simple et peut être plus facile à apprendre pour les débutants |
| **Courbe d'apprentissage**     | Peut nécessiter plus de temps pour maîtriser en raison de sa richesse en fonctionnalités | Plus rapide à apprendre en raison de sa simplicité |
| **Communauté**                 | Grande communauté active et documentée | Communauté active, mais généralement plus petite que celle de Django |
| **Utilisation**                | Idéal pour les projets complexes, robustes et riches en fonctionnalités | Convient aux petites et moyennes applications, idéal pour les projets plus simples et rapides |
| **Intégration avec d'autres outils** | Intégré avec d'autres outils Django, comme Django REST framework | Plus modulaire, peut être intégré avec divers outils selon les besoins |
| **Idéal pour**                 | Applications web complexes, sites avec des exigences de sécurité élevées | Projets plus simples, prototypage rapide, API RESTful, microservices |
