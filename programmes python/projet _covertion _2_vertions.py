print("BIENVENUE DANS LE PROGRAMME DE CONVERTION POUCE-CM")
print()

choix = 0
while choix == 0:
    choix_str = input("Entrez 1 pour convertir (centimetre en pouce) et 2 pour (Pouce en centimetre) : ")
    print()
    try:
        choix = int(choix_str)
    except:
        print("Vous avez Saisi des carracteres invalides... REESSAYEZ...")
        print()

    else:
        if choix < 1 or choix > 2:
            print("ERREUR VEUILLEZ SAISIR UNIQUEMENT (1) ou (2)... REESSAYER...")
            choix = 0
            print()
            print()

if choix == 1:
    valeur = input("Veuilez entrer la valeur en centimetre : ")
    print()
    convertion = round(float(valeur) * 0.394, 2)
    print(f"{valeur} cm = {convertion} pouces")
else:
    valeur = input("Veuilez entrer la valeur en pouce : ")
    print()
    convertion = round(float(valeur) * 2.54, 2)
    print(f"{valeur} pouces = {convertion} centimetre")



------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                        """version numero 2 avec les fonction"""


def convertir_valeur(unite1, unite2, coefficiant):
    print(f"---- convertion de {unite1} en {unite2} ----")
    valeur_float = 0
    while valeur_float == 0:
        valeur_str = input(f"Entrer la valeur a convertir en {unite2} : ")
        try:
            valeur_float = float(valeur_str)
        except:
            print("ERREUR Veuillez saisir uniquement des nombres... Reessayez...")
    convertion = valeur_float * coefficiant
    print(f"{valeur_float} {unite1} = {convertion} {unite2}")




print("BIENVENUE DANS LE PROGRAMME DE CONVERTION POUCE-CM")
print()

choix = 0
while choix == 0:
    choix_str = input("Entrez 1 pour convertir (centimetre en pouce) et 2 pour (Pouce en centimetre) : ")
    print()
    try:
        choix = int(choix_str)
    except:
        print("Vous avez Saisi des carracteres invalides... REESSAYEZ...")
        print()

    else:
        if choix < 1 or choix > 2:
            print("ERREUR VEUILLEZ SAISIR UNIQUEMENT (1) ou (2)... REESSAYER...")
            choix = 0
            print()
            print()

if choix == 1:
    convertion_pouce_cm = convertir_valeur("pouces", "centimetre", 2.54)
else:
    convertion_cm_pouce = convertir_valeur("centimetre", "pouces", 0.394)