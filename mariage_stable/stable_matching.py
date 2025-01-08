import json
import random


def charger_donnees(fichier_entree="preferences.json"):
    """Charge les données depuis un fichier JSON."""
    with open(fichier_entree, "r", encoding="utf-8") as fichier:
        donnees = json.load(fichier)
    return donnees["familles"], donnees["animaux"]


def mariage_stable(familles, animaux):
    """Implémente l'algorithme de Gale et Shapley pour appariement stable."""
    # Dictionnaires de préférences
    preferences_familles = {f["nom"]: f["preferences"] for f in familles}
    preferences_animaux = {a["nom"]: a["preferences"] for a in animaux}

    # Dictionnaires pour suivre les appariements
    appariements = {}  # Clé : famille, Valeur : animal
    animal_apparie = {}  # Clé : animal, Valeur : famille
    familles_libres = [f["nom"] for f in familles]

    # Tant qu'il y a des familles non appariées
    while familles_libres:
        famille = familles_libres.pop(0)  # Prendre une famille libre
        pref_famille = preferences_familles[famille]

        for animal in pref_famille:
            if animal not in animal_apparie:
                # Si l'animal est libre, apparier avec la famille
                appariements[famille] = animal
                animal_apparie[animal] = famille
                break
            else:
                # Si l'animal est déjà apparié, vérifier les préférences
                famille_actuelle = animal_apparie[animal]
                pref_animal = preferences_animaux[animal]

                if pref_animal.index(famille) < pref_animal.index(famille_actuelle):
                    # L'animal préfère la nouvelle famille, on change l'appariement
                    appariements[famille] = animal
                    animal_apparie[animal] = famille
                    del appariements[famille_actuelle]  # Supprimer l'ancien appariement
                    familles_libres.append(famille_actuelle)  # Rendre l'ancienne famille libre
                    break
                # Sinon, continuer avec le prochain animal dans la liste

    # Ajouter les familles restantes sans appariement
    for famille in familles:
        if famille["nom"] not in appariements:
            appariements[famille["nom"]] = None

    return appariements


def enregistrer_appariements(appariements, fichier_sortie="appariements.json"):
    """Enregistre les appariements dans un fichier JSON, triés numériquement par famille."""
    # Trier les appariements par numéro de famille
    appariements_triees = {famille: appariements[famille]
                           for famille in sorted(appariements.keys(), key=lambda x: int(x.split()[1]))}

    with open(fichier_sortie, "w", encoding="utf-8") as fichier:
        json.dump(appariements_triees, fichier, indent=4, ensure_ascii=False)

    print(f"Appariements enregistrés dans '{fichier_sortie}'")


def generer_donnees(nombre_familles, nombre_animaux, fichier_sortie="preferences.json"):
    """Génère des données de familles et d'animaux avec des préférences aléatoires et les enregistre dans un fichier JSON."""
    tailles_animaux = ["petit", "moyen", "grand"]
    activites_physiques = ["faible", "modéré", "intense"]
    experiences_animaux = ["aucune", "peu", "modéré", "beaucoup"]
    niveau_energie = ["faible", "modéré", "élevé"]
    budgets = ["faible", "modéré", "élevé"]
    espaces_disponibles = ["petit", "moyen", "grand"]

    familles = []
    animaux = []

    # Génération des familles
    for i in range(1, nombre_familles + 1):
        famille = {
            "nom": f"Famille {i}",
            "taille_animal": random.choice(tailles_animaux),
            "activite_physique": random.choice(activites_physiques),
            "allergies": random.choice([True, False]),
            "enfants_en_bas_age": random.choice([True, False]),
            "experience_avec_animaux": random.choice(experiences_animaux),
            "temps_disponible": random.choice(activites_physiques),
            "budget": random.choice(budgets),
            "espace_disponible": random.choice(espaces_disponibles),
            "preferences": random.sample([f"Animal {j}" for j in range(1, nombre_animaux + 1)], nombre_animaux)
        }
        familles.append(famille)

    # Génération des animaux
    for i in range(1, nombre_animaux + 1):
        animal = {
            "nom": f"Animal {i}",
            "type": random.choice(["chien", "chat", "lapin", "oiseau"]),
            "comportement": random.choice(["calme", "joueur", "protecteur", "indépendant"]),
            "besoins_en_exercice": random.choice(activites_physiques),
            "compatibilite_avec_enfants": random.choice(["bonne", "moyenne", "mauvaise"]),
            "niveau_energie": random.choice(niveau_energie),
            "problemes_de_sante": random.choice(["aucun", "mineurs", "sérieux"]),
            "proprete_et_hygiene": random.choice(["propre", "moyen", "peu propre"]),
            "côut_entretien": random.choice(budgets),
            "espace_minimal": random.choice(espaces_disponibles),
            "preferences": random.sample([f"Famille {j}" for j in range(1, nombre_familles + 1)], nombre_familles)
        }
        animaux.append(animal)

    # Enregistrement dans un fichier JSON
    donnees = {
        "familles": familles,
        "animaux": animaux
    }

    with open(fichier_sortie, "w", encoding="utf-8") as fichier:
        json.dump(donnees, fichier, indent=4, ensure_ascii=False)

    print(f"Données générées et enregistrées dans '{fichier_sortie}'")


if __name__ == "__main__":
    choix = input("Choisissez une option : \n (1) Générer des données \n (2) Apparier les familles et les animaux \n ")
    if choix == "1":
        nombre_familles = int(input("Entrez le nombre de familles :"))
        nombre_animaux = int(input("Entrez le nombre d'animaux : "))
        generer_donnees(nombre_familles, nombre_animaux)
    elif choix == "2":
        familles, animaux = charger_donnees()
        appariements = mariage_stable(familles, animaux)
        enregistrer_appariements(appariements)
    else:
        print("Option invalide.")