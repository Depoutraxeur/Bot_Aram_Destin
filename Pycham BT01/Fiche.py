import time
import random


def afficher_inventaire(perso):
    print("Inventaire :")
    if len(perso["inventaire"]) == 0:
        print("Ton inventaire est vide")
        return
    for item in perso["inventaire"]:
        print("-", item)


def ajouter_objet(perso):
    objet = input("Quel objet veux-tu rajouter ? ")
    perso["inventaire"].append(objet)
    print("Tu as ajouté :", objet)


def supprimer_objet(perso):
    objet = input("Quel objet veux-tu supprimer ? ")
    if objet in perso["inventaire"]:
        perso["inventaire"].remove(objet)
        print("Objet supprimé :", objet)
    else:
        print("Objet introuvable")


def afficher_fiche(perso):
    print("\n=== FICHE PERSONNAGE ===")
    print("Nom :", perso["nom"])
    print("Classe :", perso["classe"])
    print("Niveau :", perso["niveau"])
    print("PV :", perso["PV"], "/", perso["PV_max"])

    print("\n-- Caractéristiques --")
    for carac, valeur in perso["caracs"].items():
        print(carac, ":", valeur)

    print("\n-- Inventaire --")
    afficher_inventaire(perso)


def changer_pv(perso, delta):
    perso["PV"] += delta
    if perso["PV"] < 0:
        perso["PV"] = 0
    if perso["PV"] > perso["PV_max"]:
        perso["PV"] = perso["PV_max"]
    print("PV actuels :", perso["PV"], "/", perso["PV_max"])


def boire_potion(perso):
    potion = "Potion de soin"
    soin = 10
    if potion in perso["inventaire"]:
        perso["inventaire"].remove(potion)
        changer_pv(perso, soin)
        print("Tu récupères", soin, "PV en buvant une potion.")
    else:
        print("Tu n'as pas de potion !")


def lancer_d20():
    resultat = random.randint(1, 20)
    print("Un D20 est lancé...")
    time.sleep(1)
    print("Résultat :", resultat)
    return resultat


def modificateur(score):
    return (score - 10) // 2


def attaquer(attacker, cible):
    print("\n--- TOUR D'ATTAQUE ---")
    if cible["PV"] <= 0:
        print(cible["nom"], "est déjà K.O !")
        return

    jet = lancer_d20()

    # base dégâts
    if jet == 20:
        print("Coup critique !")
        degat = random.randint(15, 20)
    elif jet == 1:
        print("Échec critique !")
        degat = random.randint(0, 5)
    else:
        degat = random.randint(5, 15)

    # bonus FOR si dispo
    bonus = 0
    if "caracs" in attacker:
        bonus = modificateur(attacker["caracs"]["FOR"])

    # crit double toujours (même pour mannequin)
    if jet == 20:
        degat *= 2

    degat += bonus
    if degat < 0:
        degat = 0

    print(attacker["nom"], "fait", degat, "dégâts à", cible["nom"])
    changer_pv(cible, -degat)
    print("----------------------")


mannequin = {"nom": "Bob le Mannequin", "PV_max": 40, "PV": 40}

nom = input("Nom de ton personnage ? ")
classe = input("Classe ? ")

perso = {
    "nom": nom,
    "classe": classe,
    "niveau": 1,
    "PV_max": 50,
    "PV": 10,
    "inventaire": ["Épée en bois", "Potion de soin"],
    "caracs": {"FOR": 10, "DEX": 10, "CON": 10, "INT": 10, "CHA": 10},
}

print("Très bien,", perso["nom"], "tu es un/une", perso["classe"])
time.sleep(1)

while True:
    print("\n--- MENU ---")
    print("1) Afficher inventaire")
    print("2) Ajouter un objet")
    print("3) Supprimer un objet")
    print("4) Afficher fiche personnage")
    print("5) Attaquer le mannequin")
    print("6) Boire une potion")
    print("7) Quitter")

    choix = input("Ton choix : ")

    if choix == "1":
        afficher_inventaire(perso)
    elif choix == "2":
        ajouter_objet(perso)
    elif choix == "3":
        supprimer_objet(perso)
    elif choix == "4":
        afficher_fiche(perso)
    elif choix == "5":
        attaquer(perso, mannequin)
        if mannequin["PV"] > 0:
            print("Le mannequin riposte !")
            attaquer(mannequin, perso)
    elif choix == "6":
        boire_potion(perso)
    elif choix == "7":
        break
    else:
        print("Choix invalide, réessaie.")