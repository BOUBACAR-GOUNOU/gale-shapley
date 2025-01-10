# R & D : Problème de mariage stable  
*[Poster de présentation](docs/poster_G1_probleme_mariage_stable.pdf)*.

Étant donné n hommes et n femmes, chacun ayant établi une liste de préférence ordonnée des
individus du sexe opposé, l’objectif est de former des couples de manière à ce qu’il n’existe aucune paire (h, f ) d’hommes et de femmes qui préféreraient être ensemble plutôt que de rester avec leurs partenaires respectifs. Lorsque cette condition est remplie, on considère que l’ensemble des mariages est stable.

## Simulation : Refuge Animal

L'objectif est de créer un ensemble de données comprenant des familles et des animaux avec des attributs spécifiques, ainsi que des préférences mutuelles entre eux. Ces données sont ensuite utilisées pour simuler un appariement stable entre les familles et les animaux à l'aide de l'algorithme de Gale et Shapley dans notre projet de recherche : **Problème de mariage stable.**

## 1. Génération des Familles

Les familles sont générées en prenant en compte plusieurs critères aléatoires. Chaque famille dispose de certaines caractéristiques et de préférences pour les animaux. Voici les étapes de la génération des familles :

### Attributs des familles :

- **Nom** : Chaque famille reçoit un nom unique sous la forme "Famille X", où X est un numéro.
- **Taille de l'animal souhaité** : Chaque famille choisit une taille d'animal (petit, moyen ou grand).
- **Activité physique** : Un choix est effectué pour le niveau d'activité physique souhaité (faible, modéré ou intense).
- **Allergies** : La famille peut avoir des allergies (booléen : vrai ou faux).
- **Enfants en bas âge** : La famille peut avoir ou non des enfants en bas âge.
- **Expérience avec les animaux** : La famille a une certaine expérience avec les animaux (aucune, peu, modéré, beaucoup).
- **Temps disponible** : Le temps disponible pour prendre soin de l'animal (faible, modéré, élevé).
- **Budget** : Le budget de la famille pour l'entretien de l'animal (faible, modéré, élevé).
- **Espace disponible** : L'espace que la famille peut offrir (petit, moyen, grand).

### Préférences des familles :

Chaque famille établit une liste de préférences parmi tous les animaux disponibles. Les préférences sont générées de manière aléatoire en ordonnant les animaux, de sorte qu'une famille puisse avoir une préférence pour un animal spécifique en fonction des critères ci-dessus.

## 2. Génération des Animaux

Les animaux sont également générés de manière aléatoire, avec des caractéristiques qui correspondent aux critères requis par les familles. Chaque animal a également ses propres préférences pour les familles. Voici les étapes de génération des animaux :

### Attributs des animaux :

- **Nom** : Chaque animal reçoit un nom unique sous la forme "Animal X", où X est un numéro.
- **Type** : L'animal peut être un chien, un chat, un lapin, ou un oiseau.
- **Comportement** : L'animal a un comportement qui peut être calme, joueur, protecteur, ou indépendant.
- **Besoins en exercice** : Le niveau d'exercice nécessaire (faible, modéré, élevé).
- **Compatibilité avec les enfants** : L'animal peut être compatible avec les enfants (bonne, moyenne, mauvaise).
- **Niveau d'énergie** : Le niveau d'énergie de l'animal (faible, modéré, élevé).
- **Problèmes de santé** : L'animal peut avoir des problèmes de santé (aucun, mineurs, sérieux).
- **Propreté et hygiène** : Le niveau de propreté de l'animal (propre, moyen, peu propre).
- **Coût d'entretien** : Le coût d'entretien de l'animal (faible, modéré, élevé).
- **Espace minimal** : L'animal a besoin d'un certain espace (petit, moyen, grand).

### Préférences des animaux :

Pour chaque animal, une liste de préférences est générée en choisissant un certain nombre de familles parmi celles disponibles, triées en fonction des critères spécifiques à chaque animal (par exemple, un animal pourrait préférer une famille avec un espace plus grand ou avec un budget plus élevé).

## 3. Liens entre Familles et Animaux

Après avoir généré les familles et les animaux, les préférences de chaque famille et de chaque animal sont stockées dans des listes.

### Pour chaque famille :
Une liste de préférences est générée en choisissant un certain nombre d'animaux parmi ceux disponibles, triés en fonction des critères de la famille (par exemple, le type d'animal, les besoins en exercice, le budget).

### Pour chaque animal :
Une liste de préférences est générée en choisissant un certain nombre de familles parmi celles disponibles, triées en fonction des critères de l'animal (par exemple, la compatibilité avec les enfants, l'espace disponible, les problèmes de santé).

## 4. Programme

### `make_preference.py`
Ce programme génère les familles et les animaux avec leurs attributs respectifs ainsi que leurs préférences. Les données générées sont ensuite enregistrées sous forme de fichier JSON.

### `make_appariement.py`
Ce programme utilise l'algorithme de Gale et Shapley pour effectuer l'appariement entre les familles et les animaux, en fonction des préférences mutuelles. Le résultat de l'appariement est également enregistré dans un fichier JSON.

### `make_graphe.py`
Ce programme permet de créer un graphe visuel représentant l'appariement entre les familles et les animaux. Chaque famille et chaque animal sont représentés par un nœud, et les arêtes entre eux montrent l'appariement stable obtenu par l'algorithme de Gale et Shapley.

### `stable_matching.py` 
Ce programme combine **make_preference.py** et **make_appariement.py**

### `taux_satisfaction.py`
Ce programme charge des données de préférences et d'appariements depuis des fichiers JSON, puis calcule la satisfaction moyenne des familles et des animaux en fonction de leurs positions dans les préférences. Ensuite, il génère un graphique à barres montrant ces taux de satisfaction.
**Le calcule de taux de satisfaction (voir le point 5).**

## 5. Algorithme de Gale et Shapley
L'algorithme de Gale et Shapley est un algorithme permettant de trouver un appariement stable entre deux ensembles de participants. Dans le cadre de ce projet, il permet d'apparier des familles et des animaux en fonction de leurs préférences respectives.

Une **paire instable** se produit lorsqu'il existe deux participants, un de chaque côté, qui préfèrent être appariés entre eux plutôt que d'être appariés avec leurs partenaires actuels. L'algorithme cherche à éliminer ces instabilités.

##### Exemple de paire instable :
- Famille A préfère Animal X à son partenaire actuel Animal Y.
- Animal X préfère la Famille A à sa partenaire actuelle Famille B.

Dans ce cas, la paire (Famille A, Animal X) constitue une paire instable.
### Pseudo-Code de l'Algorithme de Gale et Shapley

**Entrée** : `n` hommes et `n` femmes, chacun avec une liste de préférences.  
**Sortie** : Un ensemble de mariages stables.

1. Initialiser chaque homme et chaque femme comme étant célibataire.
2. Tant qu’il existe un homme célibataire qui n’a pas encore proposé à toutes les femmes :
   1. Sélectionner un tel homme `h`.
   2. `f` ← la femme préférée de `h` parmi celles à qui il n’a pas encore proposé.
   3. Si `f` est célibataire :
      - `h` et `f` se fiancent.
   4. Sinon :
      - Comparer `h` avec le fiancé actuel `h'` de `f`.
      - Si `f` préfère `h` à `h'` :
        - `h` et `f` se fiancent, et `h'` redevient célibataire.
      - Sinon :
        - `h` reste célibataire.
3. Retourner l’ensemble des couples formés.

**Complexité** : polynomiale `O(n^2)`

## 5. Taux de Satisfaction

L'algorithme de Gale-Shapley, utilisé pour résoudre le problème des mariages stables, peut être analysé sous l'angle du taux de satisfaction des participants. Le taux de satisfaction de chaque participant peut être exprimé par la formule suivante :

**Satisfactionᵢ = (N - positionᵢ + 1) / N × 100%**

où :
- **N** est le nombre total de choix possibles,
- **positionᵢ** est le rang du partenaire dans la liste de préférences de i.

Cette mesure reflète le niveau de satisfaction de chaque participant en fonction de sa position dans la liste de préférences de son partenaire. Plus un participant est assigné à un partenaire plus haut dans sa liste, plus sa satisfaction est élevée.

L'algorithme de Gale-Shapley a une tendance à favoriser légèrement les "proposants" (c'est-à-dire, ceux qui initient la proposition), car en moyenne, les "proposants" finissent par obtenir un partenaire plus proche du sommet de leur liste de préférences que les "répondants". Cela est dû au fait que les "proposants" ont plus d'opportunités de se réajuster tout au long de l'exécution de l'algorithme, tandis que les "répondants" doivent accepter ou rejeter les propositions selon un ordre plus rigide.

En conséquence, le taux de satisfaction moyen des "proposants" est souvent plus élevé que celui des "répondants", ce qui témoigne de cette légère préférence dans l'algorithme de Gale-Shapley.


## 6.  Document de Recherche

Vous pouvez consulter le [Poster de présentation](docs/poster_G1_probleme_mariage_stable.pdf).
