<link rel="stylesheet" href="../../stylesheet.css">

# Story_03 — Introduction à l'IA

## Contexte
> Avec la quantité croissante de données, les entreprises ont un besoin de nouvelles et différentes applications de l'IA. IA imite la pensé de l'être humain, et le replacera dans différentes tâches.

> Raisonner/Planifer/Optimiser/Apprendre/Comprendre sont les 5 tâches dans lesquelles l'IA perform.

## Mots clefs
- <def-of>Data mining</def-of> : *Procès d'extraction et de découverte de modèles dans un large ensemble de données.*
- <def-of>Deep learning</def-of> : *Sous-ensembles des méthodes d'apprentissage automatique qui sont basés sur des réseaux neuronales.*
- <def-of>IA</def-of> : *Ensembles de théories et de techniques capables de simuler l'intelligence humaine.*
- <def-of>IoT (Interner of Things)</def-of> : *Ensembles des outils numérique qui se connecte entre eux, et échange des données.*
- <def-of>Modèle</def-of> : *Construction mathématique générant une déduction ou une prédiction à partir de données d’entrée.*
- <def-of>Neural Networks</def-of> : *Réseau de neuronnes numerique construits et organisé à partir des réseaux neuronaux biologiques constituant le cerveau des animaux.*
- <def-of>Pattern</def-of> : *Modèle simplifié.*
- <def-of>Stupidité artificielle</def-of> : *IA avec un modèle à support aléatoire.*

## Problématiques
1. Comment une entreprise peut transformer un océan de données en flux régulier ?

## Hypothèses
- <u>L'application de l'IA est strictement sur Big Data</u> <h-f/> :
   *Les deux entretiennent une relation interdépendante et chacun ne peut fonctionner sans l’autre.*
- <u>L'IA est capable de résoudre des problèmes algébriques non solubles par l'humain</u> <h-f/>
- <u>L'IA permet de faire une même application avec différents langages</u> <h-f/>
- <u>L'IA peut-être indépendant de l'Homme, s'auto-générer (après création)</u> <h-f/>
- <u>L'IA est limité par la quantité de données dont t'on dispose</u> <h-f/> :
   *L'IA peut produire des connaissances à partir des informations.*
- <u>Une IA est forcément éthique</u> <h-f/> :
   *Il y n'existe pas de bonne IA, c'est un outil, et comme tout outil, il est utilisé pour le meilleur ou pour le pire.*

## Plan d'action
1. Investigation des ressources;
2. Definir les 5 phases historiques de l'IA;
3. Construire un tableau avantages/inconvenients de l'IA;
4. Citer les application de l'IA;
5. Différence entre Machine Learning et Deep Learning;
6. Définitions des mots clefs (*bref*);
7. Vérifier les hypothèses;
8. Répondre aux questions.

# RER

## Pros & Cons
| Pros                          | Cons                        |
|-------------------------------|-----------------------------|
| Créatrice de nouveaux métiers | Perte d'emplois             |
| Efficacité                    | Impact environnemental      |
| Précision                     | Menace la cybersecurité     |
| Productivité                  | Problème de confidentialité |
| Reduit les erreurs/risk/coûts | Pas d'éthique               |


## Applications de l'IA
- <p-x c="blue">Médicine</p-x> : Détecter les maladies et d’identifier les cellules cancéreuses. L’IA utilise la combinaison de données historiques et de l’intelligence médicale pour la découverte de nouveaux médicaments.
- <p-x c="blue">Education</p-x> : L’IA a contribué à accroître la productivité parmi les enseignants et les a aidés à se concentrer davantage sur les élèves plutôt que sur le travail administratif.
- <p-x c="blue">Recherche et développement</p-x> : *Les algorithmes d'IA sont capables d'analyser des quantités massives de données, de trouver des modèles et de générer de nouvelles hypothèses. Les chercheurs utilisent l'IA pour accélérer la découverte de nouveaux matériaux*.
- <p-x c="blue">Reconnaissance d'image et vision par ordinateur</p-x> : *La reconnaissance d'image et la vision par ordinateur sont des domaines de l'IA qui permettent aux machines d'analyser et d'interpréter des images et des vidéos.*

## Deep Learning ≠ Machine Learning
- <p-x c="blue">Principes de fonctionnement</p-x>
   - **ML** : *Utilisation d'algorithmes qui apprennent des modèles et font des prédictions basées sur des caractéristiques dérivées des données d'entrée.*
   - **DL** : *Utilise un réseau neuronal avec des couches multiples.*
- <p-x c="blue">Exigences en matière de données</p-x>
   - **ML** : *Implique l’existence de données organisées.*
   - **DL** : *N’a pas besoin de données structurées.*
- <p-x c="blue">Complexité du modèle</p-x>
   - **ML** : *Utilise des modèles simples, comme la [régression linéaire](https://fr.wikipedia.org/wiki/R%C3%A9gression_lin%C3%A9aire), [arbres de décision](https://fr.wikipedia.org/wiki/Arbre_de_d%C3%A9cision) ou [machines à vecteurs de support](https://fr.wikipedia.org/wiki/Machine_%C3%A0_vecteurs_de_support).*
   - **DL** : *Utilise des architectures de réseaux neuronaux complexes, souvent comportant de nombreuses couches, ce qui permet de modéliser des relations complexes dans les données.*
- <p-x c="blue">Temps d'entrainement</p-x>
   - **ML** : *Plus court que le deep learning, en particulier pour les modèles volumineux et complexes.*
   - **DL** : *Peut nécessiter beaucoup de temps et de calculs, en particulier avec de grands ensembles de données et des architectures complexes.*

## IA symbolique & connexionniste

|                                       | Symbolique                              | Connexionniste                 |
|---------------------------------------|-----------------------------------------|--------------------------------|
| **Représentation de la connaissance** | Utilise des symboles et règles logiques | Réseaux de neurones            |
| **Apprentissage**                     | Manipulation des symboles et de règles  | Apprend à partir de données    |
| **Interprétabilité**                  | Facilement interprétable                | Plus difficile à comprendre    |
| **Cas d'usage**                       | Efficace pour tâches spécifiques        | Efficace pour tâches complexes |

## IA forte & faible

|                 | Forte                                    | Faible                  |
|-----------------|------------------------------------------|-------------------------|
| **Cas d'usage** | Toutes sorte de tâche                    | Tâche précises          |
| **Capacité**    | Raisone avec l'entrainement + sentiments | Raisone comme entrainé  |
| **Test Turing** | Réussite du test Turing à 100%           | En fonction de la tâche |