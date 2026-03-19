from numpy.ma.core import append
from pkg_resources import non_empty_lines

colonists = [
    {"name": "Arno", "role": "Farmer", "shooting": 3, "melee": 4, "plants": 14, "mood": 72},
    {"name": "Lyra", "role": "Guard", "shooting": 11, "melee": 7, "plants": 2, "mood": 66},
    {"name": "Dax", "role": "Hunter", "shooting": 15, "melee": 5, "plants": 3, "mood": 59},
    {"name": "Mira", "role": "Doctor", "shooting": 4, "melee": 3, "plants": 6, "mood": 83},
    {"name": "Kurt", "role": "Builder", "shooting": 6, "melee": 8, "plants": 4, "mood": 61},
    {"name": "Elin", "role": "Farmer", "shooting": 2, "melee": 2, "plants": 16, "mood": 77}
]
#Affiche le nombre total de colons.
print("Nombre total de colons : ", len(colonists))

#Affiche le nom de tous les colons.
print("Noms des colons présents :")
for colon in colonists:
    print(colon["name"])

#Affiche les colons qui ont un moral inférieur à 65.
print("Colons avec moral inférieur a 65 :")
for colon in colonists:
    if colon["mood"] < 65:
        print(colon["name"])

#Trouve le colon avec la meilleure compétence plants.
meilleur_plants = colonists[0]
for colon in colonists:
    if colon["plants"] > meilleur_plants["plants"]:
        meilleur_plants = colon
print("Colons avec meilleur *plants* :", meilleur_plants["name"], "avec", meilleur_plants["plants"])

#Calcule le moral moyen de la colonie.
somme_mood = 0
for colon in colonists:
    somme_mood += colon["mood"]
moyenne_moral = somme_mood // len(colonists) #Arondie avec //
print("Moral moyen de la colonie :", moyenne_moral)

#Compte combien de colons ont chaque rôle.
roles = {}
for colon in colonists:
    role = colon["role"]
    if role not in roles:
        roles[role] = 1
    else:
        roles[role] += 1
print(roles)

#Trouve le meilleur tireur parmi les Hunters uniquement
meilleur_tireur = None
for colon in colonists:
    if colon["role"] == "Hunter":
        if meilleur_tireur is None or colon["shooting"] > meilleur_tireur["shooting"]:
            meilleur_tireur = colon
print("Meilleur tireur parmis hunters :", meilleur_tireur["name"])
print("Tir :", meilleur_tireur["shooting"])


