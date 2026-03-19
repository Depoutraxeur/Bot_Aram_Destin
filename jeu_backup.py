# ------------------ OUTILS ------------------
import os
import time

ASCII_BANNER = r"""
  _   _    ____    __  __     _____    _    _     _____     ____    _   _        _    ____    _   _     _____    _____   _____     _ 
 | \ | |  / __ \  |  \/  |   |  __ \  | |  | |   |  __ \   / __ \  | \ | |      | |  / __ \  | \ | |   |_   _|  / ____| |_   _|   | |
 |  \| | | |  | | | \  / |   | |  | | | |  | |   | |  | | | |  | | |  \| |      | | | |  | | |  \| |     | |   | |        | |     | |
 | . ` | | |  | | | |\/| |   | |  | | | |  | |   | |  | | | |  | | | . ` |  _   | | | |  | | | . ` |     | |   | |        | |     | |
 | |\  | | |__| | | |  | |   | |__| | | |__| |   | |__| | | |__| | | |\  | | |__| | | |__| | | |\  |    _| |_  | |____   _| |_    |_|
 |_| \_|  \____/  |_|  |_|   |_____/   \____/    |_____/   \____/  |_| \_|  \____/   \____/  |_| \_|   |_____|  \_____| |_____|   (_)

"""

VERSION = "0.1"


def slow_print(texte, vitesse=0.03):
    for caractere in texte:
        print(caractere, end="", flush=True)
        time.sleep(vitesse)
    print()


def clear():
    os.system("cls" if os.name == "nt" else "clear")


# ------------------ PERSONNAGE ------------------

def creer_perso(nom):
    return {
        "nom": nom,
        "habilete": 0,
        "endurance": 0,
        "chance": 0,
        "inventaire": [],
        "or": 0,
        "pv": 10,
        "talents": [],
        "cles": [],
        "flags": [],
        "chapitre": 0
    }


def afficher_perso(perso):
    clear()
    print("=== FICHE PERSONNAGE ===")
    print("Nom :", perso["nom"])
    print("PV :", perso["pv"])
    print("Or :", perso["or"])
    print("Chapitre :", perso["chapitre"])

    print("\nInventaire :")
    if perso["inventaire"]:
        for o in perso["inventaire"]:
            print("-", o)
    else:
        print("(Vide)")

    print("\nTalents :")
    if perso["talents"]:
        for t in perso["talents"]:
            print("-", t)
    else:
        print("(Aucun)")

    input("\n[Entrée pour revenir]")


def ajouter_objet(perso, objet):
    perso["inventaire"].append(objet)


# ------------------ ATTRIBUTS ------------------

def repartir_points(perso, points):
    clear()
    print("=== ATTRIBUTION DES POINTS ===")
    print("1 = Habileté | 2 = Endurance | 3 = Chance")
    print("Tape 1, 2 ou 3\n")

    while points > 0:
        print(f"Points restants : {points}")
        print(f"H:{perso['habilete']}  E:{perso['endurance']}  C:{perso['chance']}")
        choix = input("> ").strip()

        if choix == "1":
            perso["habilete"] += 1
            points -= 1
        elif choix == "2":
            perso["endurance"] += 1
            points -= 1
        elif choix == "3":
            perso["chance"] += 1
            points -= 1
        else:
            print("Choix invalide.")
            continue

        clear()


def demarrer_jeu(perso):
    choix = input(
        "Tout est prêt. Es-tu sûr de vouloir commencer ?\n"
        "(répond simplement par oui ou non)\n> "
    ).strip().lower()

    if choix == "oui":
        slow_print("Très bien. Voyons donc jusqu'où tu iras…")
        chapitre_0(perso)

    elif choix == "non":
        slow_print(
            "En fait… tu n'as pas vraiment le choix.\n"
            "Je voulais simplement voir ce que tu allais répondre."
        )
        chapitre_0(perso)

    else:
        slow_print("Ne joue pas au plus malin...")
        chapitre_0(perso)


# ------------------ TALENTS ------------------

talents = [
    (
        "Pas sans trace",
        "Vous savez disparaître quand il le faut.\n"
        "Se déplacer sans bruit, éviter les regards, contourner un affrontement :\n"
        "là où d’autres seraient repérés, vous glissez hors de portée."
    ),
    (
        "Mauvais pressentiment",
        "Quelque chose cloche… et vous le sentez avant qu’il ne soit trop tard.\n"
        "Vous repérez les pièges, les embuscades et les dangers imminents\n"
        "avant de tomber dedans."
    ),
    (
        "Voix persuasive",
        "Vos mots pèsent plus lourd qu’une lame.\n"
        "Négocier, apaiser, convaincre ou obtenir un avantage\n"
        "sans recourir à la violence fait partie de vos talents."
    ),
    (
        "Clés interdites",
        "Aucune serrure n’est vraiment inviolable.\n"
        "Portes closes, coffres scellés, passages verrouillés\n"
        "cèdent sous vos mains patientes et expertes."
    ),
    (
        "Lecteur de signes",
        "Symboles, runes, codes ou langues oubliées vous parlent encore.\n"
        "Vous comprenez ce qui est caché dans les textes anciens,\n"
        "les inscriptions et les messages cryptés."
    ),
    (
        "Marqué par la route",
        "La faim, la fatigue et les terres hostiles ne vous arrêtent pas facilement.\n"
        "Vous savez survivre là où d’autres s’effondrent,\n"
        "et poursuivre votre route malgré l’usure."
    ),
    (
        "La Mort détourne les yeux",
        "Quand tout devrait s’achever, il vous reste parfois une chance.\n"
        "Par un sursis, un coup de chance ou un destin capricieux,\n"
        "vous échappez à une issue fatale."
    )
]


def choisir_talents(perso, max_talents=2):
    def afficher_liste():
        clear()
        print("=== TALENTS DISPONIBLES ===\n")
        for i, (nom, desc) in enumerate(talents, start=1):
            print(f"{i} - {nom}")
            slow_print("    " + desc, 0.01)
            time.sleep(0.2)
            print()

    afficher_liste()

    while len(perso["talents"]) < max_talents:
        restants = max_talents - len(perso["talents"])
        choix = input(f"Choisis un talent ({restants} restant) > ").strip()

        if not choix.isdigit():
            print("Entre un numéro valide.")
            continue

        index = int(choix) - 1
        if not 0 <= index < len(talents):
            print("Numéro hors limite.")
            continue

        talent = talents[index][0]
        if talent in perso["talents"]:
            print("Déjà choisi.")
            continue

        perso["talents"].append(talent)
        print(f"✅ Talent ajouté : {talent}")


# ------------------ CHAPITRES ------------------
def jouer_chapitre(perso):
    if perso["chapitre"] == 0:
        chapitre_0(perso)
    elif perso["chapitre"] == 1:
        chapitre_1(perso)
    else:
        print("Chapitre inconnu :", perso["chapitre"])
        input("[Entrée]")


def chapitre_0(perso):
    clear()
    print("\n=== INTRODUCTION : LE RÉVEIL ===\n")

    slow_print("Le froid te réveille avant la douleur.")
    slow_print("Un froid lourd, poisseux, qui s'infiltre dans tes os.\n")

    slow_print("Tu ouvres les yeux avec difficulté.")
    slow_print("La lumière est grise, étouffée par un ciel sans visage.")
    slow_print("Tu es étendu dans la boue, au milieu de corps brisés et de carcasses déchirées.\n")

    slow_print("Des membres tordus émergent de la terre comme des racines mortes.")
    slow_print("Le métal éventré et la chair ouverte se confondent.")
    slow_print("Impossible de dire où s'arrête l'homme et où commence la machine.\n")

    slow_print("L'odeur du sang et de la terre humide colle à ta gorge.")
    slow_print("Chaque respiration est un combat.")
    slow_print("Ton estomac se noue, mais rien ne vient.\n")

    slow_print("Tu essaies de bouger.")
    slow_print("La douleur répond immédiatement, brutale, sans pitié.")
    slow_print("Ton corps est là… mais il ne t'obéit qu'à moitié.\n")

    slow_print("Tes souvenirs se dérobent quand tu essaies de les saisir.")
    slow_print("Des images surgissent, puis disparaissent aussitôt.")
    slow_print("Des cris. Des ordres. Une lumière aveuglante.")
    slow_print("Puis plus rien.\n")

    slow_print("Tu connais ton nom…")
    slow_print("Il résonne encore quelque part dans ton esprit.")
    slow_print("Mais tu ignores ce qui t'a conduit ici.\n")

    slow_print("Tes vêtements sont lacérés, imbibés de boue et de sang séché.")
    slow_print("Ton corps est meurtri, couvert de plaies mal refermées.")
    slow_print("Tes mains tremblent quand tu les lèves devant ton visage.\n")

    slow_print("Elles ne semblent pas tout à fait… normales.")
    slow_print("Sous la crasse, quelque chose brille faiblement.")
    slow_print("Du métal. Des implants. Ou pire.\n")

    slow_print("Autour de toi, le champ de bataille est silencieux.")
    slow_print("Un silence anormal, presque respectueux.")
    slow_print("Comme si le monde retenait son souffle.\n")

    slow_print("Tu es vivant.")
    slow_print("Pour l'instant.\n")

    slow_print("Et tu sens, au plus profond de toi,")
    slow_print("que ton réveil n'est pas un hasard.")

    # Boucle de choix : 1 entrer, 2 rester (et le narrateur 'rewind')
    while True:
        print("Tu comprends deux choses :")
        print("- rester ici, blessé et désarmé, c'est accepter une mort certaine ;")
        print("- l'intérieur de cette structure est peut-être pire… mais c'est un abri.")
        try:
            choix = int(input(
                "\nQue fais-tu ?\n1 - Te diriger vers l'entrée sombre\n2 - Rester ici et affronter ce qui arrive\n> "))
        except ValueError:
            print("Entre 1 ou 2, s'il te plaît.")
            continue

        if choix == 1:
            print("\nChaque pas arrache une plainte à ton corps.")
            print("Les grognements derrière toi se rapprochent, mais tu ne te retournes pas.")
            print("Tu atteins l'entrée, une arche de pierre fendue, avalée par l'obscurité.")
            print("Tu franchis le seuil. Le monde extérieur se tait derrière toi.\n")
            break

        elif choix == 2:
            print("\nTu restes là, vacillant au milieu des cadavres.")
            print("Les silhouettes sortent enfin de la brume : des bêtes maigres, des formes tordues,")
            print("des yeux affamés qui brillent dans le gris du matin.")
            print("Elles t'encerclent sans hâte. Tu le sais : tu n'as aucune chance.\n")

            if "La Mort détourne les yeux" in perso["talents"]:
                print("Une des créatures bondit, puis hésite, comme retenue par une répugnance invisible.")
                print("Mais les autres n'ont pas ces scrupules.\n")

            print("Tu te débats. Tu cries. Tu griffes la boue pour t'accrocher à la vie quelques secondes de plus.")
            print("Ce n'est pas un combat. C'est une exécution lente.\n")

            print("“Non…”")
            print("“Ce n'est pas ainsi que ton histoire doit s'achever.”")
            print("“Mourir ici, dans la boue, avant même d'avoir franchi le seuil…”")
            print("“Ce serait d'un ennui affligeant.”")
            print("“Reprenons.”\n")

            print("Tu inspires brutalement. Tu es de nouveau au sol, dans la boue, là où tout a commencé.")
            print("Cette fois, tu sais au moins une chose : rester ici n'est pas une option.\n")
            # On ne casse rien, on laisse juste la boucle recommencer

        else:
            print("Choix invalide, réponds par 1 ou 2.")

    # A la fin de l'intro, tu es DANS le donjon, prêt pour le chapitre 1
    perso["chapitre"] = 1


def chapitre_1(perso):
    clear()
    print("\n=== CHAPITRE 1 : LE SEUIL DES PROFONDEURS ===")

    if "ch1_scene1_faite" in perso["flags"]:
        input("\n(Tu as déjà passé cette partie. [Entrée])")
        return

    print("L'air est lourd et immobile. La lumière du dehors ne te suit pas ici.")
    print("Seuls quelques rais blanchâtres filtrent par des fissures haut placées.\n")

    print("Un couloir s'étend devant toi, la pierre usée par le temps et par le passage de choses")
    print("que tu préfères ne pas imaginer. Bientôt, le chemin se divise :\n")
    print("1 - Longer le mur gauche, là où le sol paraît plus stable.")
    print("2 - Couper tout droit, pour gagner du temps.")

    # Choix sécurisé
    while True:
        try:
            choix = int(input("Que fais-tu ? (1 ou 2) : "))
        except ValueError:
            print("Entre 1 ou 2, s'il te plaît.")
            continue
        if choix not in (1, 2):
            print("Choix invalide, réponds par 1 ou 2.")
            continue
        break

    if choix == 1:
        print("\nTu avances lentement le long du mur, une main appuyée contre la pierre froide.")
        print("Chaque pas est pesé, mesuré, douloureux mais prudent.")
        print("Tu as, pour l'instant, évité le pire.")
    else:
        print("\nTu accélères, pressé de quitter ce couloir oppressant.")
        print("Un craquement sec retentit sous ton pied.")

        # Talent 1 : Mauvais pressentiment
        if "Mauvais pressentiment" in perso["talents"]:
            print("\nUne alerte explose dans ton esprit : DANGER.")
            print("Tu te jettes en arrière alors qu'une dalle s'effondre devant toi.")
            print("Le vide te frôle sans t'avaler.")
        # Talent 2 : Pas sans trace
        elif "Pas sans trace" in perso["talents"]:
            print("\nTon pas est plus léger que ta douleur ne le laisserait croire.")
            print("La dalle se fissure, mais ne cède pas complètement.")
            print("Tu recules juste à temps, le coeur battant.")
        # Talent 3 : La Mort détourne les yeux
        elif "La Mort détourne les yeux" in perso["talents"]:
            print("\nLe sol s'ouvre et tu tombes lourdement dans un trou étroit.")
            perso["pv"] -= 1
            print("Le choc t'arrache un cri, mais quelque chose t'épargne une chute plus profonde.")
            print("La Mort détourne les yeux, une fois encore. Tu ne perds qu'1 point de vie.")
        # Aucun talent utile
        else:
            print("\nLa dalle s'effondre sous toi et tu bascules dans le vide.")
            perso["pv"] -= 2
            print("Tu t'écrases sur des pierres brisées. La douleur t'arrache le souffle.")
            print("Tu perds 2 points de vie.")

        # Sécurité PV
        if perso["pv"] < 0:
            perso["pv"] = 0

    perso["chapitre"] = 1
    perso["flags"].append("ch1_scene1_faite")
    print("\n=== Fin du chapitre 1 ===")


# ------------------ MENU ------------------

def menu_principal(perso):
    while True:
        clear()
        print("=== MENU ===")
        print("1 - Continuer")
        print("2 - Fiche personnage")
        print("3 - Quitter menu")

        choix = input("> ")

        if choix == "1":
            jouer_chapitre(perso)
        elif choix == "2":
            afficher_perso(perso)
        elif choix == "3":
            break


# ------------------ JEU ------------------

def nouvelle_partie():
    # AVERTISSEMENT - le méssage a placer !
    slow_print("AVERTISSEMENT")
    slow_print("Ce jeu contient des thèmes sombres...ceci est un teste de longueur de texte \n"
               "pour voir si le texte va s'alligner comme je le veut au cas ou jecris bocoup\n"
               "pour voir ce que ca donne ici")
    slow_print("La mort peut survenir sans prévenir.")
    input("\n(Appuie sur Entrée pour continuer)")

    # Création
    nom = input("Nom du personnage : ")
    perso = creer_perso(nom)

    objet = input("Objet de départ : ")
    ajouter_objet(perso, objet)

    slow_print(f"\nAvant d'aller plus loin… Comment {nom} est constitué ?")
    slow_print("Habileté :")

    print(" Représente ta maîtrise du combat, ta précision et tes réflexes.")
    print(" Influence ta capacité à toucher et à éviter les coups.\n")

    slow_print("Endurance :")

    print(" Détermine ta résistance physique et ta capacité à encaisser la douleur.")
    print(" Plus elle est élevée, plus tu peux survivre longtemps.\n")

    slow_print("Chance :")

    print(" Mesure ta capacité à provoquer le destin.")
    print(" Elle peut t'aider à éviter un piège ou aggraver une situation.\n")

    repartir_points(perso, 5)

    slow_print("\nTrés intéressant.. Trés bien ! ton corps et ton esprit sont forgés par tes choix.")
    print("Habileté :", perso["habilete"])
    print("Endurance :", perso["endurance"])
    print("Chance :", perso["chance"])

    slow_print("Je te voyais autrement.. mais bon, passons a l'étape suivante !")
    slow_print("Maintenant, je vais te donner une liste de talent\n"
               "Les quels parmis ceux là ton personnage a su apprendre dans sa vie passé ?")

    choisir_talents(perso)
    demarrer_jeu(perso)

    # Boucle libre (DANS la partie)
    while True:
        clear()
        cmd = input("(Entrée = continuer | menu | quit) > ").strip().lower()

        if cmd == "":
            jouer_chapitre(perso)
        elif cmd == "menu":
            menu_principal(perso)
        elif cmd in ("quit", "q"):
            print("Fin du jeu.")
            break


def menu_titre():
    while True:
        clear()
        slow_print(ASCII_BANNER, 0.002)
        print("Version 0.1\n")

        print("1 - Nouvelle partie")
        print("2 - Continuer (bientôt)")
        print("3 - Options (bientôt)")
        print("4 - Quitter\n")

        choix = input("> ").strip()

        if choix == "1":
            return "nouvelle"
        elif choix == "4":
            return "quitter"
        else:
            input("Option indisponible pour l'instant. [Entrée]")


def main():
    action = menu_titre()
    if action == "nouvelle":
        nouvelle_partie()
    else:
        clear()
        print("À bientôt.")


if __name__ == "__main__":
    main()
