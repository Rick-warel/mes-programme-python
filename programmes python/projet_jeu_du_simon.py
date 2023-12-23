import random
import time
import os

def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')
        

def genere_la_sequence(nb_chiffre):
    sequence = ""
    for i in range(nb_chiffre):
        chiffre = random.randint(0, 9)
        sequence += str(chiffre)
    return sequence






print("BIENVENUE DANS LE JEU DU SIMON")
print()
print("Choisisez votre niveau de difficulté")
print("1 - Facile    2 - Normal   3 - Difficil")
niveau = input("votre choix : ")

if niveau == "1":
    nombre_chiffre = 2
    pause = 5

elif niveau == "2":
    nombre_chiffre = 3
    pause = 4

else :
    nombre_chiffre = 4
    pause = 3


sequence = genere_la_sequence(nombre_chiffre)


clear_screen()


essai = 1
point = 0

while essai > 0:
    print("Retenez la sequence suivante")
    time.sleep(2)
    print(sequence)
    time.sleep(pause)
    clear_screen()
    print("Veuillez saisir la precedante sequance")
    reponse = input("Votre reponse : ")
    clear_screen()
    if reponse == sequence:
        chiffre_suivant = random.randint(0, 9)
        sequence += str(chiffre_suivant)
        point +=1
    
    else:
        print(f"Mauvaise reponse. la bonne reponse etait : {sequence}")
        essai = 0

print(f"Votre score est de : {point}")