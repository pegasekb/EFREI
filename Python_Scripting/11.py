#Paul Blanc & Jay AMIN fini

# Créez un script prend plusieurs arguments :
# a. -c
# i. Cette option indique la création d’un fichier. Cette option doit être suivi du nom du fichier à créer. Si aucun nom n’est défini, le script retour une erreur. Le fichier est créé dans le répertoire courant, sinon un Fullpath est requis.
# b. -r
# i. Cette option permet d’afficher le contenu d’un fichier. Cette option doit être suivi du nom du fichier à lire, son absence retourne une erreur. Si le fichier n’existe pas, il faudrait demander à l’utilisateur de corriger le nom.
# c. -a
# i. Cette option permet d’ajouter des données à un fichier. Il doit être suivi du nom du fichier à modifier et ensuite la donnée à ajouter. La donnée a ajouté peut-être une chaine de caractères ou un fichier. Il faut vérifier au préalable que le fichier existe.
# d. -d
# i. Cette option permet de détruire un fichier. Il est suivi du nom du fichier à détruire.
# e. -t
# i. Cette option permet de vérifier le type du fichier. Il doit être suivi par le nom du fichier à analyser.

import os
import sys

if len(sys.argv) > 1 : # On verifiqu'il ya au moins 1 argument

#Partie avec le -C
    if sys.argv[1] == "-c": # Verifie si y a le -c 
        if len(sys.argv)>2 : # Verifie si il y a bien le nom du fichier
            if len (sys.argv) >3: # Verifie si y a un repertoir d'indiqué
                try : # Verifie que ... et si possible le fait
                    os.chdir(sys.argv[3]) # Le dossier existe et va dedans
                    open(sys.argv[2], "x") # Le fichier n'existe pas et le créer
                    open(sys.argv[2], "x").close # Pour ne pas bloquer le fichier sur ouvert (mais inutile car il ne sera pas reutilisé dans le programme)
                except : # Affiche un messsage d'erreur si ca en marche pas 
                    print("Le dossier n'est pas accecible ou le fichier existe deja")
            else : # Pas de repertoir spécifié
                try : # Verifie que ... et le fait
                    open(sys.argv[2], "x") # le fichier n'existe pas et le creer
                    open(sys.argv[2], "x").close # Pour ne pas bloquer le fichier sur ouvert (mais inutile car il ne sera pas reutilisé dans le programme)
                except : # Sinon message d'erreur
                    print("Le fichier existe deja") 

        else : 
            print ("ERROR : Il faut mettre le nom du fichier que l'on veut créer")


#Partie avec -R
    if sys.argv[1] == "-r": # Verifie si y a le -r
        if len(sys.argv)>2 : # Verifie si il y a bien le nom du fichier
            try : # Verifie qu'il peut ... et le fait
                open (sys.argv[2],'r') # Ouvir le fichier en mode lecture
                print (open(sys.argv[2]).read()) # Affiche le fichier dans un print
                open (sys.argv[2],'r').close # Ferme le ficheir
            
            except : # Si pas possible
                a= 0 # Mets un variable de vérification a 0
                while a == 0 : # Tant que cette variables est a 0 on boucle
                    print ("Le nom du fichier est faux il faut en mettre un autre") # Informe l'utilisateur
                    test = input() # Demande de rentrer un nouveau nom de fichier
                    try : # Verifie qu'il peut ... et le fait si il peut
                        open(test, "r") # Ouvre le fichier en mode lecture
                        print (open(test).read()) # Affiche le fichier dans un print
                        open (test,'r').close  # Ferme le fichier
                        a=1 # Le nom rentrer existe on peut donc stop la boucle
                    except : # Sinon 
                        print () # On reboucle
        else : 
            print ("Pas de nom de fichier")

#Partie avec le -A
    if sys.argv[1] == "-a": # Verifie si y a le -a
        if len(sys.argv)>2 : # Verifie si il y a bien le nom du fichier
            if len (sys.argv)>3 : #Verifite qu'il y a un chaine de caratere ou un fichier
                try : # On test que le fichier sys.argv[2] ....
                    if open(sys.argv[2]) : # ... est Un fichier
                        try : # On voir si le sys.argv[3] est ....
                            if open(sys.argv[3],'r') : #... un fichier et qu'il est lisible
                                a = open(sys.argv[3],"r").read() # On ecrit dans "a" tous le contenu du fichier sys.argv[3]
                                open(sys.argv[2],"a").write(a) # Et on ecrit a la suite du fichier sys.argv[2] ce qui est dans "a"
                                open(sys.argv[2],"a").close() # On ferme le fichier sys.argv[2]
                        except : # Si sys.argv[3] n'est pas un fichier ... 
                            a = " ".join(sys.argv[3:]) # ... on mets dans "a" sous forme de string tous les argument a partir de l'argtument 3
                            open(sys.argv[2],"a").write(a) # Et on ecrit "a" a la suite du fichier sys.argv[2]
                            open(sys.argv[2],"a").close() # Et on le ferme
                except : # Si le fichier sys.argv[2] n'est pas lisibles ...
                    print(sys.argv[2], "ne peut pas etre ouvert ou n'existe pas")
    

#Parite avec le -D
    if sys.argv[1] == "-d": # Verifie si y a le -d
        if len(sys.argv)>2 : # Verifie si il y a bien le nom du fichier  
            try : # On essaye de   ....
                os.remove (sys.argv[2]) # Suiprimer le fichier sys.argv[2]
            except : #Sinon on affiche l'erreur
                print("Le fichier ", sys.argv[2], " n'a pas etait trouvé")

# Partie avec le -t
    if sys.argv[1] == "-t": # Verifie si y a le -t
            if len(sys.argv)>2 : # Verifie si il y a bien le nom du fichier 
                os.system("file "+sys.argv[2]) # On utilise la commande file de bash pour trouvé le type de fichier
            else: # 
                print ("Il y a pas de fichier a analyser")

else :
    print ("Il y a pas d'argument")

