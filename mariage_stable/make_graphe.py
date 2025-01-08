import json
import matplotlib.pyplot as plt
import math


def charger_appariements(fichier="appariements.json"):
    """Charge les appariements depuis un fichier JSON."""
    with open(fichier, "r", encoding="utf-8") as fichier_json:
        return json.load(fichier_json)


def afficher_appariements_graphique(appariements, graphique_num):
    """Affiche un graphique bipartite des appariements avec des noms d'animaux et des numéros."""

    # Extraire les familles et les animaux
    familles = list(appariements.keys())
    animaux = list(appariements.values())

    # Définir les positions sur l'axe X pour les familles et les animaux
    x_familles = [1] * len(familles)
    x_animaux = [2] * len(animaux)
    y_positions = range(len(familles))

    fig, ax = plt.subplots(figsize=(10, 6))

    # Différencier familles appariées et non appariées
    familles_appariees = [familles[i] for i, a in enumerate(animaux) if a != "Non apparié"]
    y_appariees = [y_positions[i] for i, a in enumerate(animaux) if a != "Non apparié"]
    familles_non_appariees = [familles[i] for i, a in enumerate(animaux) if a == "Non apparié"]
    y_non_appariees = [y_positions[i] for i, a in enumerate(animaux) if a == "Non apparié"]

    # Placer les points sur le graphique
    ax.scatter([1] * len(y_appariees), y_appariees, color='blue', label='Familles appariées', s=100)
    ax.scatter([1] * len(y_non_appariees), y_non_appariees, color='red', label='Familles non appariées', s=100)
    ax.scatter(x_animaux, y_positions, color='green', label='Animaux appariés', s=100)

    # Annoter les points avec les numéros et les noms des animaux
    for i in range(len(familles)):
        ax.text(0.9, y_positions[i], str(i + 1), ha='right', va='center', fontsize=10, color='blue' if familles[i] in familles_appariees else 'red')
        if animaux[i] != "Non apparié":
            ax.text(2.1, y_positions[i], str(animaux[i]), ha='left', va='center', fontsize=10, color='green')

    # Tracer les flèches entre familles et animaux appariés
    for i, famille in enumerate(familles):
        if appariements[famille]:
            animal = appariements[famille]
            animal_index = animaux.index(animal)
            ax.annotate("",
                        xy=(x_animaux[animal_index], y_positions[animal_index]), xycoords='data',
                        xytext=(x_familles[i], y_positions[i]), textcoords='data',
                        arrowprops=dict(arrowstyle="->", lw=1.5, color='gray'))

    # Configuration des axes et de la légende
    ax.set_xticks([1, 2])
    ax.set_xticklabels(["Familles", "Animaux"], fontsize=12)
    ax.set_yticks([])
    ax.legend()
    plt.title(f"Graphique des appariements Familles ↔ Animaux")
    plt.grid(False)
    plt.tight_layout()
    plt.show()


def afficher_appariements_multiples(appariements, elements_par_graphe=10):
    """Affiche plusieurs graphiques si le nombre d'éléments dépasse une certaine limite."""

    # Diviser les appariements en plusieurs groupes de taille "elements_par_graphe"
    familles = list(appariements.keys())
    total_familles = len(familles)
    nombre_graphe = math.ceil(total_familles / elements_par_graphe)

    for i in range(nombre_graphe):
        # Déterminer le sous-ensemble des appariements pour ce graphique
        start_index = i * elements_par_graphe
        end_index = min((i + 1) * elements_par_graphe, total_familles)
        appariements_subset = {famille: appariements[famille] for famille in familles[start_index:end_index]}

        # Afficher le graphique pour ce sous-ensemble
        afficher_appariements_graphique(appariements_subset, graphique_num=i + 1)


# Charger les appariements depuis un fichier JSON
appariements = charger_appariements("appariements.json")

# Afficher plusieurs graphiques
afficher_appariements_multiples(appariements, elements_par_graphe=10)
