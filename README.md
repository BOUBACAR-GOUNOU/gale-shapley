# Simulation : Refuge Animal

L'objectif de ce projet est de créer un ensemble de données comprenant des familles et des animaux avec des attributs spécifiques, ainsi que des préférences mutuelles entre eux. Ces données sont ensuite utilisées pour simuler un appariement stable entre les familles et les animaux à l'aide de l'algorithme de Gale et Shapley.

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

#### Algorithme de Gale et Shapley
L'algorithme de Gale et Shapley est un algorithme permettant de trouver un appariement stable entre deux ensembles de participants. Dans le cadre de ce projet, il permet d'apparier des familles et des animaux en fonction de leurs préférences respectives.

Une **paire instable** se produit lorsqu'il existe deux participants, un de chaque côté, qui préfèrent être appariés entre eux plutôt que d'être appariés avec leurs partenaires actuels. L'algorithme cherche à éliminer ces instabilités.

##### Exemple de paire instable :
- Famille A préfère Animal X à son partenaire actuel Animal Y.
- Animal X préfère la Famille A à sa partenaire actuelle Famille B.

Dans ce cas, la paire (Famille A, Animal X) constitue une paire instable.

### `make_graphe.py`
Ce programme permet de créer un graphe visuel représentant l'appariement entre les familles et les animaux. Chaque famille et chaque animal sont représentés par un nœud, et les arêtes entre eux montrent l'appariement stable obtenu par l'algorithme de Gale et Shapley.

## 5. Pseudo-Code de l'Algorithme de Gale et Shapley

```text
1. Initialiser tous les participants (familles et animaux) comme non appariés.
2. Tant qu'il existe des familles non appariées :
   a. Une famille non appariée propose à son premier choix d'animal.
   b. Si l'animal n'est pas apparié, il accepte la proposition.
   c. Si l'animal est déjà apparié, il compare son partenaire actuel avec la famille qui lui a proposé.
      i. Si l'animal préfère le nouveau prétendant, il rejette son partenaire actuel et accepte la nouvelle proposition.
      ii. Si l'animal préfère son partenaire actuel, il rejette la nouvelle proposition.
3. Répéter l'étape 2 jusqu'à ce que tous les participants soient appariés.
4. Retourner l'appariement stable.
```

## 9. Document de Recherche

Vous pouvez consulter le [Poster de recherche](docs/poster_probleme_mariage_stable.pdf).
