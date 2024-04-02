<link rel="stylesheet" href="../../../stylesheet.css">

# Story_08 — API Restful

## Contexte
> Se familiariser avec la construction et la conceptualisation des API’s Restful.

## Mots clefs
- <def-of>API (Application Programming Interface)</def-of> : *Interface permettant l’interaction entre différentes applications.*
- <def-of>FastAPI</def-of> : *FastAPI est un framework web Python*
- <def-of>REST (REpresentational State Transfer)</def-of> : *Ensemble de principes utilisant les méthodes HTTP pour concevoir des APIs web.*
- <def-of>Restful</def-of> : *Services web conformes au style d'achitecture REST.*
- <def-of>Marshmallow</def-of> : **
- <def-of>Swagger</def-of> : **
- <def-of>Postman</def-of> : **
- <def-of>URI (Uniform Resource Identifier)</def-of> : **
- <def-of>URL</def-of> : **
- <def-of>Endpoint</def-of> : **
- <def-of>Rootage</def-of> : **
- <def-of>HTTP (HyperTexte Transfer Protocol)</def-of> : **
- <def-of>HTTPS</def-of> : **
- <def-of>SQLAlchemy</def-of> : **
- <def-of>OWASP</def-of> : **
- <def-of>GET</def-of> : **
- <def-of>POST</def-of> : **
- <def-of>PUT</def-of> : **
- <def-of>PATCH</def-of> : **
- <def-of>DELETE</def-of> : **
- <def-of>SOAP (Simple Object Access Protocol)</def-of> : **
- <def-of>Dash</def-of> : **
- <def-of>WSGI (Web Server Gateway Interface)</def-of> : *Spécification pour une interface universelle entre les serveurs Web et les applications ou frameworks Web Python. WSGI définit une interface standard qui permet aux serveurs Web de communiquer avec les applications Python, permettant ainsi à différents serveurs Web et cadres d'application de fonctionner ensemble de manière transparente.*
- <def-of>ASGI (Asynchronous Server Gateway Interface)</def-of> : *Évolution de WSGI et est conçu pour répondre aux limitations des modèles de requête-réponse synchrones dans les applications Web traditionnelles.*

## Problématiques
1. Comment construire une API Rest avec Python ? 
1. Comment sécuriser une API ? 
1. Comment créer une documentation avec Swagger ? 
1. Comment fonctionne Postman ?
1. Comment utiliser les méthodes GET, POST, PUT, PATCH, DELETE ? 
1. Comment mettre en place une application Restful avec Flask ? 

## Hypothèses
- <u>On doit utiliser les méthodes GET et POST pour faire des requêtes. </u> <h-t/> : *!;*
- <u>Une API prend en compte les connexions sécuriser HTTPS.</u> <h-t/> : *!;*
- <u>Les réponses d'une API RESTful peuvent être mises en cache.</u> <h-t/> : *!;*
- <u>On garde le même jeton d'authentification lorsque l'on fait plusieurs requêtes.</u> <h-t/> : *!;*
- <u>Il faut toujours une clef d’accès pour une API.</u> <h-t/> : *!;*
- <u>?</u> <h-t/> : *!;*
- <u>?</u> <h-t/> : *!;*
- <u>?</u> <h-t/> : *!;*

## Plan d'action
1. Investigation des ressources
1. Définitions des mots clefs;
1. Vérifier les hypothèses;
1. Répondre aux questions.
1. Comparaison entre API Rest, et API SOAP. 
1. Comparaison entre HTTP et HTTPS. 

# RER

### [Codes d'états retour HTTP](https://fr.wikipedia.org/wiki/Liste_des_codes_HTTP)

