print("Bienvenue dans le programme pour majeur")
Nom = str(input("quel est votre nom : "))
print("Bienvenue monsieur ", Nom)
print("Pour votre securité nous devons verifier que vous etes majeur")
annee_de_naissance = int(input("Quel est votre année de naissance : "))
statut = 2023 - annee_de_naissance
if statut < 18:
    print("dsl vous etes mineur vous ne pouvez pas acceder au programme car vous n'avez que ", statut, " ans.")
else:
    print("Vous etes majeur, vous pouver acceder au programme car vous avez ", statut, " ans")

if statut > 18:
    mot_de_passe = input("Crée un mot de passe pour vous connecter a votre compte :")
    autorisation = input("Souhaitez vous vous connectez à votre compte? Tapez (Yes) pour continuer ou taper (Non) pour sortir ")
    if autorisation == "Yes" :
        input("nom d'utilisateur : ")
        password = ""
        while not password == mot_de_passe:
            password = input("mot de passe : ")
            if password != mot_de_passe:
                print("mot de passe inccorect veuillez saisir le bon mot de passe")
            else:
                print("bienvenue sur votre compte monsieur", Nom)
    elif autorisation == "No":
        print("au revoir et a bientot monsieur", Nom)
