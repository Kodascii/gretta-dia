<link rel="stylesheet" href="../../stylesheet.css">

# Story_04 — Mise en place du poste

## Contexte
> Pour coder l'IA il faut des outils informatiques adaptés à son développement:
> - Anaconda
> - Jupyter
> - Python

## Mots clefs
- <def-of>Anaconda</def-of> : *Anaconda is a Python distribution (prebuilt and preconfigured collection of packages) that is commonly used for data science.*
- <def-of>Compilateur</def-of> : *Outil logiciel qui traduit le code source de haut niveau écrit dans un langage de programmation en code machine ou en code intermédiaire.*
- <def-of>Environement (Développement)</def-of> : *Ensemble d'outils, de bibliothèques et de ressources pour créer, tester et déboguer des logiciels. Cela inclut les éditeurs de code, les compilateurs/interprètes, les systèmes de contrôle de version et d'autres outils qui facilitent le processus de développement.*
- <def-of>Github</def-of> : *Plateforme Web pour le contrôle de versions et le développement collaboratif de logiciels.*
- <def-of>IDE (Integrated Development Environment)</def-of> : *Il s'agit d'une application logicielle qui fournit des outils et des fonctionnalités complets pour faciliter le développement de logiciels.*
- <def-of>Interpréteur</def-of> : *Logiciel qui exécute directement le code source écrit dans un langage de programmation de haut niveau, traduisant et exécutant chaque ligne de code une par une.*
- <def-of>Jupyter</def-of> : *Jupyter est un projet open source qui développe des blocs-notes interactifs basés sur le Web pour la programmation, l'analyse de données et l'apprentissage automatique.*
- <def-of>[Mathplotlib](https://matplotlib.org/stable/tutorials/pyplot.html)</def-of> : *Bibliothèque complète de visualisation de données pour le langage de programmation Python.*
- <def-of>[Numpy (Numerical Python)](https://www.w3schools.com/python/numpy/default.asp)</def-of> : *Bibliothèque Python utilisée pour travailler avec des tableaux et des matrices.*
- <def-of>[Pandas](https://www.w3schools.com/python/pandas/default.asp)</def-of> : *Bibliothèque open source de manipulation et d'analyse de données pour le langage de programmation Python. Il fournit des structures de données faciles à utiliser.*
- <def-of>Python</def-of> : *Langage de programmation interprété de haut niveau,largement utilisé dans divers domaines, notamment le développement Web, la science des données, l'apprentissage automatique, l'automatisation et les scripts.*
- <def-of>[Scipy (Scientific Python)](https://www.w3schools.com/python/scipy/index.php)</def-of> : *Bibliothèque de calcul scientifique open source pour Python. Il s'appuie sur les fonctionnalités fournies par NumPy et fournit des modules supplémentaires pour le calcul scientifique et technique. SciPy comprend une large gamme d'outils pour l'optimisation, l'intégration, l'interpolation, le traitement du signal et des images, l'algèbre linéaire, l'analyse statistique, etc. Il est conçu pour fonctionner de manière transparente avec les baies NumPy.*

## Problématiques
> Comment choisir les outils de travail et les installer ? Nous devons choisir les outils de travaille en fonction de ce qu’on a besoin et regarder sur internet et chercher pour le moment d’installation

## Hypothèses
- <u>Anaconda est un géstionnaire de librairies</u> <h-t/>
- <u>Les compilateurs prennents plus de temps que les interpréteurs</u> <h-f/>
- <u>Les librairies python sont payantes</u> <h-f/>
- <u>Les outils proposé sont suffisant pour développer une IA</u> <h-t/>
- <u>Les librairies ne sont pas essentiel au développement d'une IA</u> <h-t/>
- <u>Github est essentiel pour développer une IA</u> <h-f/>

## Plan d'action
1. Investigation des ressources;
2. Définitions des mots clefs;
3. Vérifier les hypothèses;
4. Faire 3 tableaux avantages inconvenants : anaconda, jupyter notebook et python 

# RER

## Pros & Cons

### Anaconda

| Pros                                       | Cons                                         |
|--------------------------------------------|----------------------------------------------|
| Gestion facile des environnements virtuels | Interfaces graphiques parfois lourdes        |
| Prêt à l'emploi pour l'analyse de données  | Espace disque utilisé significatif           |
| Installation simple et rapide              | Inclusion de librairies peu utilisées        |
| Gestion automatisée des dépendances        |                                              |

### Jupyter Notebook

| Pros                                           | Cons                                                     |
|------------------------------------------------|----------------------------------------------------------|
| Interactivité et exploration de données        | Possibilité d'exécution non séquentielle                 |
| Support multi-langages (via kernels)           | Difficulté à gérer les versions des dépendances          |
| Intégration de visualisations interactives     | Peut générer des fichiers volumineux                     |
| Documentation interactive et narrative         | Moins adapté pour les projets de grande envergure        |
| Large adoption dans la communauté scientifique | Environnement basé sur le navigateur peut être lent      |
| Facilité de partage et de collaboration        | Environnement non idéal pour des tâches non interactives |

### Python

| Pros                                             | Cons                                                                  |
| -------------------------------------------------| ----------------------------------------------------------------------|
| **Lisibilité et simplicité**                     | **Vitesse d'exécution**                                               |
| Clarté et syntaxe lisible                        | Interprétation peut entraîner une exécution plus lente                |
|                                                  |                                                                       |
| **Bibliothèques étendues**                       | **Verrouillage interpréteur global (GIL)**                            |
| Grande bibliothèque standard                     | Le GIL peut limiter le traitement parallèle dans le multi-threading   |
| Large éventail de bibliothèques                  |                                                                       |
|                                                  |                                                                       |
| **Communauté et Documentation**                  | **Consommation de mémoire**                                           |
| Grande communauté active                         | Consommation de mémoire plus élevée par rapport à certaines langues   |
| Documentation extensive                          |                                                                       |
|                                                  |                                                                       |
| **Polyvalence et Compatibilité multiplateforme** | **Capacités limitées dans les applications intensives en ressources** |
| Plusieurs paradigmes de programmation            | Peut ne pas être idéal pour les applications intensives en ressources |
| Compatibilité multiplateforme                    |                                                                       |
|                                                  |                                                                       |
| **Productivité et développement rapide**         |                                                                       |
| Syntaxe concise                                  |                                                                       |
| Capacités d'intégration avec d'autres langages   |                                                                       |
