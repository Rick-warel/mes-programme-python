import random


def demander_nombre(nbr_min, nbr_max):
    nombre_int = 0
    while nombre_int == 0:
        nombre_str = input(f"Quel est le nombre magique entre ({nbr_min} et {nbr_max}) : ")
        try:
            nombre_int = int(nombre_str)
        except:
            print("ERREUR veuillez saisir uniquement des nombres... Réessayez")
        else:
            if nombre_int < nbr_min or nombre_int > nbr_max:
                print(
                    f"ERREUR veuillez saisir uniquement un nombre compris entre ({nbr_min} et {nbr_max})... Réessayez")
                nombre_int = 0
    return nombre_int


nombre_min = 1
nombre_max = 10
nombre_magique = random.randint(nombre_min, nombre_max)
nombre_vie = 5

nombre = 0
vie = nombre_vie

while not nombre == nombre_magique and vie > 0:
    print(f"Il vous reste ({vie}) vie")
    nombre = demander_nombre(nombre_min, nombre_max)
    if nombre < nombre_magique:
        print("Le nombre magique est supperieur au nombre que vous avez saisie... Réessayez")
        vie -= 1
    elif nombre > nombre_magique:
        print("Le nombre magique est inferieur au nombre que vous avez saisie... Réessayez")
        vie -= 1
    else:
        print("...BRAVO VOUS AVEZ TROUVER LE NOMBRE MAGIQUE...")

if vie == 0:
    print(f"OUPSSSSSSSSS. VOUS AVEZ PERDU LE NOMBRE MAGIQUE ETAIT ({nombre_magique})")