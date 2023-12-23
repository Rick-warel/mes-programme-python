import random
import time
import os

def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')
        

sequence = ""

for i in range(4):
    chiffre = random.randint(0, 9)
    sequence += str(chiffre)

clear_screen()
print("BIENVENUE DANS LE JEU DU SIMON")

essai = 1
point = 0

while essai > 0:
    print("Retenez la sequence suivante")
    time.sleep(2)
    print(sequence)
    time.sleep(3)
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