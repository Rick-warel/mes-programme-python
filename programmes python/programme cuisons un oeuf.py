import time 

print("BIENVENUE AU RESTO CONNECTE...")
print()
print("----- Au menu du jour nous avons -----")
print()
print("1- Oeufs à la coque : 3 minutes")
print("2- Oeufs mollets : 6 minutes")
print("3- Oeufs durs : 9 minutes")
print()
print()



choix_int = 0
while choix_int == 0:
    choix = input("Quel est votre choix? 1 ou 2 ou 3... : ")
    try:
        choix_int = int(choix)
    except:
        print("CARRACTER INVALIDE... REESAYEZ...")
        print()
    else:
        if choix_int > 3 or choix_int < 1:
            print("ERREUR VEUILLEZ SAISIR UNE VALEUR ENTRE 1 ET 3... REESSAYEZ...")
            print()
            choix_int = 0



if choix_int == 1:
    duree = 3*60

elif choix_int == 2:
    duree = 6*60

else:
    duree = 9*60


minute = duree//60
sec = duree-minute*60

while duree > 0:
    for i in range(10):
        print(".", end="", flush=True)
        time.sleep(0.2)
        duree -=1
    print()
    
    minute = duree//60
    sec = duree-minute*60
    print(f"Temps restant : {minute:02d}:{sec:02d} ", end="", flush=True)
    
print()
print()
print("Cuisson terminée... Bonne appetit...")
