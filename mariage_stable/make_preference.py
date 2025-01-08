import random
import json

def generer_donnees(nombre_familles, nombre_animaux, fichier_sortie="preferences.json"):
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


# Exemple d'utilisation
if __name__ == "__main__":
    nombre_familles = int(input("Entrez le nombre de familles : "))
    nombre_animaux = int(input("Entrez le nombre d'animaux : "))
    fichier_sortie = "preferences.json"
    generer_donnees(nombre_familles, nombre_animaux, fichier_sortie)
