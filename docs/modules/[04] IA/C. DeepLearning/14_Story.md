# Story_14 — RegEx & Scraping

## Contexte
> Apprendre le code de RegEx et le manipuler via le Scraping.

## Mots clefs
- <def-of>RegEx</def-of> : *Chaîne de caractères qui décrit, selon une syntaxe précise, un ensemble de chaînes de caractères possibles.*
- <def-of>Web scraping</def-of> : *Technique d'extraction des données de sites web par l'utilisation d'un script ou d'un programme.*
- <def-of>Parsing (Analyse Syntaxique)</def-of> : *Consiste à mettre en évidence la structure d'un texte. Cette structure est souvent mise en évidence par un arbre de syntaxe.*
- <def-of>BeautifulSoup</def-of> : *Bibliothèque Python d'analyse syntaxique de documents HTML et XML. Elle produit un arbre syntaxique qui peut être utilisé pour chercher des éléments ou les modifier.*
- <def-of>Scrapy</def-of> : *Scrapy est un framework d'exploration Web gratuit et open source écrit en Python. Conçu à l'origine pour le web scraping, il peut également être utilisé pour extraire des données à l'aide d'API ou en tant que robot d'exploration Web à usage général.*
- <def-of>Crawler</def-of> : *Terme générique désignant tout programme utilisé pour découvrir et analyser automatiquement des sites Web en suivant des liens d'une page Web à une autre.*
- <def-of>Twisted</def-of> : *Framework de programmation réseau événementiel écrit en Python. On l'utilise pour créer facilement des applications réseau comme des serveurs web, des serveurs de messagerie et plus encore.*
- <def-of>Selenium</def-of> : *Suite d'outils open-source utilisée pour l'automatisation des tests d'applications web.  Il permet d'écrire des scripts dans divers langages de programmation pour simuler les interactions d'un utilisateur avec un navigateur web.*
- <def-of>Splash</def-of> : *Service de rendu JavaScript open source spécialement conçu pour le web scraping. Il permet d'exécuter du code JavaScript dans un environnement sans interface graphique, afin de rendre des pages web dynamiques et d'extraire des données inaccessibles aux outils de scraping traditionnels.*
- <def-of>PySpider</def-of> : **
- <def-of>`requests`</def-of> : *Bibliothèque populaire pour effectuer des requêtes HTTP. Il simplifie le processus d'envoi de requêtes aux serveurs Web et de récupération de leurs réponses.*
- <def-of>Robots.txt</def-of> : *Convention visant à empêcher les robots d'exploration (web crawlers) d'accéder à tout ou une partie d'un site web. (Il ne sert pas à empêcher une page ou un répertoire dans les résultats de recherche, il ne contrôle pas l'indexation de vos contenus.)*
## Problématiques
1. ?

## Hypothèses
- <u>On peut utiliser RegEx pour bloquer une injection SQL</u> <h-f/> : *Utiliser des expressions régulières (RegEx) pour bloquer les injections SQL peut être bénéfique, mais ce n'est pas une solution suffisante et doit être combiné avec d'autres approches pour une protection complète.*
- <u>On ne peut pas faire du web scraping sans respecter les conditions d'utilisation des sites web et les lois sur la protection des données.</u> <h-t/> : *!;*
- <u>Le web scraping est la seule méthode pour extraire des informations à partir de pages web  </u> <h-t/> : *!;*


## Plan d'action
1. Investigation des ressources 
1. Définitions des mots clefs 
1. Vérifier les hypothèses 
1. Répondre aux questions 
1. Tableau de comparaison entre NLTK et SpaCy 
1. Faire Workshop NLKT puis SpaCy 

# RER

### Twisted
Twisted est un framework de programmation réseau événementiel écrit en Python. On l'utilise pour créer facilement des applications réseau comme des serveurs web, des serveurs de messagerie et plus encore.

Voici quelques fonctionnalités clés de Twisted :

- **Evenement-driven:** Contrairement à la programmation multi-thread traditionnelle, Twisted utilise un modèle basé sur les événements. Cela signifie que vous définissez des callbacks qui seront appelés en réponse à des événements spécifiques, comme la réception de données sur une connexion réseau.
- **Support de nombreux protocoles:** Twisted prend en charge une large gamme de protocoles réseau courants, notamment TCP, UDP, HTTP, SSH, SMTP, POP3 et IRC. Cela vous évite de réinventer la roue pour chaque type d'application réseau que vous souhaitez créer.
- **Extensible:** Twisted est conçu pour être extensible. Il dispose d'un large éventail de modules intégrés, et vous pouvez également créer vos propres extensions pour répondre à vos besoins spécifiques.

En résumé, Twisted est un outil puissant et polyvalent pour le développement d'applications réseau Python. Si vous envisagez de créer un serveur web, un chat en ligne, un client de messagerie ou toute autre application nécessitant une communication réseau, Twisted mérite d'être considéré.

## Tableau comparatif entre Scrapy, BeautifulSoup et Selenium

| Fonctionnalité | Scrapy | BeautifulSoup | Selenium |
|---|---|---|---|
| **Objectif principal** | Web scraping structuré | Analyse et manipulation de HTML | Automatisation d'interactions web |
| **Méthode de fonctionnement** | Basé sur des requêtes HTTP et des sélecteurs CSS/XPath | Analyse du code HTML brut | Contrôle du navigateur web via WebDriver |
| **Avantages** | Rapide, efficace pour le scraping structuré, prend en charge les sites web complexes | Facile à utiliser, idéal pour l'analyse et la manipulation de données HTML | Permet d'automatiser des actions JavaScript, de gérer des formulaires et de simuler des interactions utilisateur |
| **Inconvénients** | Ne gère pas le JavaScript dynamique, nécessite une configuration plus complexe | Limité à l'analyse et la manipulation de HTML, ne permet pas d'automatiser des interactions web | Plus lent que Scrapy et BeautifulSoup, nécessite l'installation d'un pilote web |
| **Cas d'utilisation** | Extraction de données structurées à partir de sites web, scraping de contenu web à grande échelle | Analyse de données HTML, nettoyage et transformation de données web, création de rapports à partir de données web | Automatisation de tâches web complexes, tests d'interface utilisateur, simulations de navigation web |
| **Langage de programmation** | Python | Python | Python, Java, C#, JavaScript |
| **Bibliothèques associées** | Extensions Scrapy, parsers HTML | Lxml, html5lib | WebDriver (Chrome, Firefox, Edge, etc.) |

**Remarques:**

* Ce tableau présente une comparaison simplifiée des fonctionnalités de base. Chaque outil offre des fonctionnalités plus avancées et des options de personnalisation.
* Le choix de l'outil dépend des besoins spécifiques du projet et des compétences du développeur.
* Il est possible de combiner l'utilisation de ces outils pour obtenir un scraping web plus complet et flexible.
