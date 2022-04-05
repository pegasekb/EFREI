#Paul Blanc & Jay AMIN fini

# Créer un script qui prend en entrée un chemin et un type de fichier 
# (Ex : .txt, .py, etc). Le script ouvre un terminal pour afficher le contenu
# ou exécuter chaque fichier.

import os
import sys

try :
    print (open(sys.argv[1], 'r').read) # Essaye d'ouvrir le ficheir pour voir si c'est un fichier
    test=1 # Si Oui on enregistre
        
except :
    test=0 #Si non = a 0 

if (test == 1) :
    try :
        cat ='cat '+sys.argv[1] # On ecrit la commende pour lire le fichier 
        os.system(cat) # On lit le fichier
    except: # Sinon on essaye de l'executer
        exe='./'+sys.argv[1] # On ecrit la commande
        os.system(exe) # On l'execut
else : # Si c'est une extention et pas un fichier
 
    listefichier =[_ for _ in os.listdir(".") if _.endswith(sys.argv[1])] #On mets dans un liste tous les fichier avec l'exetension
    try :
       for file in listefichier : #On fait une boucle pour passé tous les fichier trouvé
            cat ='cat '+file  #On ecrit la commende pour lire le fichier 
            print ('contenu du fichier ', file, '\n')
            os.system(cat) # On affiche le contenu de chaque fichier
    except :  
        for file in listefichier:  #On fait une boucle pour passé tous les fichier trouvé
            exe = './'+file #On ecrit la commende pour lire le fichier 
            print ('fichier ', file, " va etre executer" '\n')
            os.system(exe) # On execte les fichier 1 a 1

