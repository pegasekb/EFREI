#Paul Blanc

# Crée un script qui permet d’authentifier des utilisateurs par nom et mot de passe.
# a. Les informations d’authentification doivent être stockées dans deux fichiers différents pour des questions de sécurité. User.txt et pass.txt.
# b. Le script doit stocker dans un fichier de log la date et l’heure de chaque tentative. Un fichier de log par utilisateur.
# c. Un maximum de 5 tentatives admises
# d. Le script propose un nom et un mot de passe alphanumérique à l’utilisateur

import string
import random
import time
import sys
import os
# Fonction qui logs les tenative de connection
def logs (user,etat):
    user=user+".log"
    f= open (user, "a")
    f.write ((etat+" de connection le "+time.asctime()+"\n"))
    f.close ()
    

# Fonction qui ecrit les nouveaux utilisateur
def sigin (user, passwrd):
        print ("Le mots de passe à était engregister")
        open("user.txt", "a").write("\n"+user)
        open("pass.txt", "a").write("\n"+passwrd)
        

#Décomposition lignes par lignes des fichier user.txt et pass.txt en liste pour lire les lignes plus facilement
listeuser= open("user.txt").read().splitlines()
listepass= open("pass.txt").read().splitlines()


for a in range (1,5) : # Boucle des 5 tentatives
    # Demande de login / password
    print ("Login")
    user=input()
    print ("Password")
    passwrd=input()

    compt = 0 # Compteur pour savoir a quelle ligne est le login (si il existe)

    # cherche le login ligne par linge pour voir si il exite
    for i in listeuser:
        compt=compt+1
        
        if user == i: # Si le login est dans la liste ...
            if listepass[compt-1] == passwrd: # On regard si le password est au meme numero de ligne dasn le fichier pass.txt
                print ("Vous etes authentifié") # Si oui on est authentifié
                logs (user, "Reussi") # Et l'action est loger dans un fichier $nomuser.log 
                sys.exit() #Fin du programme
            else:
                print ("Le mots de login ou password sont faux!") #Sinon pas authentifié
                logs (user, "Echec") # Et l'action est loger dans un fichier $nomuser.log 

            break # Si le log est bon mais le mdp faux il ne sert a rien de lire les autre ligens de login donc on stop la rechercehe
    print ("Le mots de login ou password sont faux!")


# Si il y a plus de 5 echec ...
print ("il y a eu trop d'echec \nVoulez-vous vous enregister ? \nOui ou Non ") # On demande si la personne veut s'engregistrer
if input() == "Oui" : # Si Oui
    print ("Choisisez un login") # Elle choisi un mdp
    user = input ()
    for i in listeuser : #On verifie que le login n'exite pas en le compart a la liste deja existant
        if user == i :
            print ("Ce login existe déjà, fin du programme") #Si le login existe ...
            sys.exit()  # On arret le programme
    print ("Choisisez un password") # Ensuite on demande de chosiir un passe word
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=16)) # permets de creer un mdp de 16 caratere alphanumerique
    print ("Je vous propose le mdp de pass suivant\n\n",x,"\n\nVous conveint-il ?") #Et presente le mdp
    if input() == "Oui" : # Si le mdp generer convient....
        sigin(user, x) # Il est stocker avec le login dans les fichier
    else : #Si l'utilisateur veut mettre son propre mdp ...

        os.system("stty -echo") # Sert a chage les mdp mais ne marche
        print ("Alors veuillez choisir un mots de passe")
        passwrd = input()  # Il le choisi 
        print("Confirmé votre mots de passe")
        passwrd1 = input () # Et le confirme
        if passwrd == passwrd1 : #Si les mdp sont identique
            sigin(user, passwrd) # Le login / mdp sont stocker dans le ficheir

        else :
            print ("Les mots de passe sont differents \nFin du programme")
else : 
    print ("Arret du script") # Si ne personne ne veut pas s'engregister on arret
    
os.system("stty echo") # Pour reactivé la vision de ce que l'on temps dans le terminal


