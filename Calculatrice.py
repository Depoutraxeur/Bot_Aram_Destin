def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b


def lire_nombre(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("⚠️ Entre un nombre valide.")


def afficher_menu():
    print("\n=== CALCULATRICE ===")
    print("1 - Addition")
    print("2 - Soustraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Quitter")


def main():
    operations = {
        "1": addition,
        "2": soustraction,
        "3": multiplication,
        "4": division,
    }

    while True:
        afficher_menu()
        choix = input("Choix : ").strip()

        if choix == "5":
            print("Bye 👋")
            break

        if choix not in operations:
            print("⚠️ Choix invalide.")
            continue


        if choix == "4" and n2 == 0:
            print("⚠️ Division par zéro impossible.")
            continue

        n1 = lire_nombre("Nombre 1 : ")
        n2 = lire_nombre("Nombre 2 : ")

        resultat = operations[choix](n1, n2)
        print("Résultat :", resultat)

#On récupère la bonne opération,
#Puis on l’exécute avec les deux nombres et on stock le résultat.


if __name__ == "__main__":
    main()
