import json

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
    familles_libres = [f["nom"] for f in familles]
    animaux_disponibles = [a["nom"] for a in animaux]

    # Tant qu'il y a des familles non appariées et des animaux disponibles
    while familles_libres and animaux_disponibles:
        famille = familles_libres.pop(0)  # Prendre une famille libre
        pref_famille = preferences_familles[famille]

        for animal in pref_famille:
            if animal in animaux_disponibles:
                # Si l'animal est libre, apparier avec la famille
                appariements[famille] = animal
                animaux_disponibles.remove(animal)
                break
            else:
                # Si l'animal est déjà apparié, vérifier les préférences
                famille_actuelle = [f for f, a in appariements.items() if a == animal][0]
                pref_animal = preferences_animaux[animal]

                if pref_animal.index(famille) < pref_animal.index(famille_actuelle):
                    # L'animal préfère la nouvelle famille, on change l'appariement
                    appariements[famille] = animal
                    familles_libres.append(famille_actuelle)
                    break
                # Sinon, continuer avec le prochain animal dans la liste

    # Ajouter les familles restantes sans appariement
    for famille in familles_libres:
        appariements[famille] = None

    return appariements

def enregistrer_appariements(appariements, fichier_sortie="appariements.json"):
    """Enregistre les appariements dans un fichier JSON."""
    with open(fichier_sortie, "w", encoding="utf-8") as fichier:
        json.dump(appariements, fichier, indent=4, ensure_ascii=False)

    print(f"Appariements enregistrés dans '{fichier_sortie}'")


# Exemple d'utilisation
if __name__ == "__main__":
    familles, animaux = charger_donnees()
    appariements = mariage_stable(familles, animaux)
    enregistrer_appariements(appariements)
