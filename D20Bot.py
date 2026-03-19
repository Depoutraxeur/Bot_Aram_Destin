import discord
import random
import asyncio
import time
import os

import os
print("TEST OK")
TOKEN = os.getenv("DISCORD_TOKEN")
print("TOKEN?", TOKEN is not None)
print("LEN", len(TOKEN) if TOKEN else 0)

dernier_destin = 0
cooldown = 300

TOKEN = os.getenv("DISCORD_TOKEN")
print("Token trouvé :", TOKEN is not None)

if TOKEN:
    print("Longueur du token :", len(TOKEN))
    print("Début du token :", TOKEN[:4])
    print("Fin du token :", TOKEN[-4:])
else:
    print("Aucun token trouvé")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

phrases = [
"""📣 Un allié sera AFK dès les premières minutes.
La game se transformera lentement en marche funèbre vers le Nexus.
Personne ne saura vraiment pourquoi il est parti, mais la défaite sera déjà écrite.""",

"""📣 Un coéquipier tentera un dive sous tour niveau 3 avec 
une confiance inexplicable et le premier sang sera offert.
Ce fils de pute osera envoyer un ping « ? » collectif.
À partir de là, la partie prendra une direction très sombre direction la défaite.""",

"""📣 L’équipe ennemie aura une composition absolument ignoble.
Du poke, du contrôle, et probablement un champion qui ne devrait même pas exister en ARAM.
Tous ce qu'il faut pour un lavage d'anus total.""",

"""📣 Un abrutie décidera d’engager seul contre cinq ennemis parfaitement groupés.
Dans son esprit c’était peut-être un move héroïque.
Dans la réalité, ce sera surtout celuis qui causera la défaite.""",

"""📣 Un fils de pute va aller récupérer les derniers PV restant en fin de game.
Alors que ce même trou du cul sera full life et provoquera la défaite du groupe
pour en plus dire a la fin : Useless fr.""",

"""📣 Le destin de la game est flou, trés difficile a prédire
Un joueur vas éssayer de faire le malin mais se fera éclater la tronche a la place.
Ce qui va entrainer une déco de ce dernier afin de finir en 4v5.""",

"""📣 Un allié ignorera soigneusement de soigné ses mates tous le long de la game.
L’équipe ennemie, elle, en profiteras a son avantage.
Petit à petit, la différence de santé deviendra insurmontable.""",

"""📣 La première tour tombera bien trop vite.
Et avec elle disparaîtra le dernier espoir d’avoir une game équilibrée.
À partir de là, chaque fight semblera de plus en plus désespéré.""",

"""📣 Un enfoiré de la team ennemi commencera à accumuler les kills 
comme un gros cochon et personne ne saura vraiment comment ce pédé est devenu si fort.
Mais ce qui est sùr, c'est que c'est lui qui vas faire la game.""",

"""📣 Un teamfight éclatera sans que personne ne sache vraiment pourquoi.
Les compétences partiront dans tous les sens et toucherons personne.
Et à la fin, seuls la team ennemis restera debout.""",

"""📣 Un joueur annoncera fièrement : « JE SUIS FRANÇAIS ».
Personne ne comprendra vraiment le rapport avec la situation.
Mais étrangement, la game se terminera très peu de temps après.""",

"""📣 Les compétences ennemies toucheront avec une précision presque surnaturelle.
Les esquives seront ratées, les positions douteuses.
Chaque erreur coûtera un peu plus cher que la précédente.""",

"""📣 Un allié poursuivra un ennemi presque mort jusqu’au bout du pont.
Il découvrira malheureusement que l’ennemi n’était pas seul.
La contre-attaque sera rapide et brutale.""",

"""📣 La coordination de l’équipe disparaîtra progressivement.
Chacun combattra dans son coin avec son propre plan mystérieux.
Et aucun de ces plans ne fonctionnera vraiment.""",

"""📣 Un abrutie finis va être present dans l'équipe, qui causera
a lui seul la défaite car ce gros con ne sais pas jouer à cause
de son cerveau athrofier.""",

"""📣 Le Tabouret du PMU vas officiellement porter son équipe.
Cependant la victoir disparaîtra si la réserve de drogue atteint le seuil critique.
Un pré-roulage est nécessaire""",

"""📣 Un allié utilisera toutes ses compétences sur une vague de sbires.
Exactement au moment où l’équipe ennemie décidera d’engager.
Ce qui provoquera la victoire a coup sùr du PMU.""",

"""📣 Le dernier teamfight semblera enfin gagnable.
Les ennemis seront bas en vie, le Nexus presque à portée.
Un membre du PMU portera le coup final afin d'amener la win.""",

"""📣 Le scripte a l'air de joué en la faveur du PMU ! 
Aucun fils de putes n'a été détécter lors de l'analyse.
Les conditions on l'air favorable.""",

"""📣 Contre toute logique, contre toute attente,
le PMU remportera officiellement cette game.
Personne ne comprendra vraiment comment c’est arrivé."""
]

annonces_resultat = [
    " Même le bot en est cuit..",
    " Il n'est pas encore trop tard pour reculer..",
    " L'oracle du PMU observe le résultat avec gravité.",
    " Une vision du futur vient de se matérialiser.",
    " Une issue défavorable semble déjà se dessiner."
]


async def ecrire_lentement(channel, texte, vitesse=1.5):
    lignes = texte.strip().split("\n")

    for ligne in lignes:
        ligne = ligne.strip()
        if ligne != "":
            await channel.send(ligne)
            await asyncio.sleep(vitesse)


async def lancer_de(channel):
    message = await channel.send("🎲 Le dé est lancé...")

    for i in range(7):
        valeur = random.randint(1, 20)
        await asyncio.sleep(0.4)
        await message.edit(content=f"🎲 {valeur}")

    resultat_final = random.randint(1, 20)
    await asyncio.sleep(0.6)
    await message.edit(content=f"🎲 **Résultat du D20 : {resultat_final}**")

    return resultat_final


async def analyse_partie(channel):
    etapes = [
        "♻️ Analyse de la future team",
        "♻️ Calcul du taux de drogue présent"
    ]

    for etape in etapes:
        await channel.send(etape)
        await asyncio.sleep(1.2)


@client.event
async def on_ready():
    print(f"Bot connecté : {client.user}")


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.lower() == "!destin":
        global dernier_destin

        maintenant = time.time()

        if maintenant - dernier_destin < cooldown:
            reste = int(cooldown - (maintenant - dernier_destin))
            await message.channel.send(f"L'oracle est épuisé. Cette vision lui a coûté énormément.\n"
f"Il doit méditer avant d'oser regarder à nouveau le futur.\n"
f"Reviens dans {reste}s... (5€ pour ignorer les règles.)")
            return

        dernier_destin = maintenant

        intros = [
            """ L'oracle observe la file ARAM...
Le hasard prépare déjà une immense mauvaise foi.""",

            """ L'oracle consulte le dé sacré...
Les probabilités de défaite semblent très élevées.""",

            """ L'oracle contemple les joueurs adverse...
La mauvaise foi semble déjà s'accumuler ici.""",

            """ Une vision trouble traverse l'esprit de l'oracle...
Mais est-ce une bonne chose ?""",

            """ L'oracle examine les signes de l'algorithme.
Le "hasard" semble encore avoir des comptes à régler."""
        ]

        intro = random.choice(intros)
        await ecrire_lentement(message.channel, intro)

        await analyse_partie(message.channel)

        resultat = await lancer_de(message.channel)

        annonce = random.choice(annonces_resultat)

        if resultat <= 5:
            couleur = 0xff0000  # rouge
            emoji = "🔴"
            annonce = random.choice([annonces_resultat[1], annonces_resultat[2]])

        elif resultat <= 15:
            couleur = 0xf1c40f  # jaune
            emoji = "🟡"
            annonce = annonces_resultat[4]

        else:
            couleur = 0x2ecc71  # vert
            emoji = "🟢"
            annonce = random.choice([annonces_resultat[0], annonces_resultat[3]])

        description = phrases[resultat - 1]

        if resultat == 1:
            description = "**💀 ÉCHEC CRITIQUE - DÉFAITE ASSURÉE 💀**\n\n" + description

        elif resultat == 20:
            description = "**🍀 LES ÉTOILES S'ALIGNENT 🍀**\n**VICTOIRE INÉVITABLE**\n\n" + description

        embed = discord.Embed(
            title=f"{emoji} {annonce}",
            description=description,
            color=couleur
        )

        await message.channel.send(embed=embed)


client.run(TOKEN)