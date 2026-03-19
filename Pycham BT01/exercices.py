def analyse(eleves):
    total = 0
    count = 0
    meilleur = None

    for eleve in eleves:
        note = eleve["note"]

        if note is not None:
            total += note
            count += 1

            if meilleur is None or note > meilleur:
                meilleur = note

    if count == 0:
        return None

    moyenne = total / count
    return moyenne, meilleur


eleves = [
    {"nom": "Alice", "note": 10},
    {"nom": "Bob", "note": None},
    {"nom": "Charlie", "note": 20}
]

resultat = analyse(eleves)
print(resultat)