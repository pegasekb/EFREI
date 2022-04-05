#Paul Blanc & Jay AMIN fini

# Créer un script qui prend en argument le nom d’un répertoire (fullpath).
# Le script doit s’assurer que le fichier mis en argument est un répertoire,
# ensuite compter le nombre de répertoires, le nombre d’exécutable et le nombre de 
# fichiers à l’intérieur. Le script affiche ces informations.

import os
import sys

if len(sys.argv)>1 : # Test si il y a bien un argument
    try : 
        count =0
        FichList = [ f for f in os.listdir(sys.argv [1]) if os.path.isfile(os.path.join(sys.argv [1],f)) ] # Va dans le dossier et liste tous les fichiers
        DosList = [ f for f in os.listdir(sys.argv [1]) if os.path.isdir(os.path.join(sys.argv [1],f)) ] # Va dans le dossier et liste tous les dossiers
        ExeList= [ f for f in os.listdir(sys.argv [1]) if os.access(sys.argv [1]+f, os.X_OK) ] # Va dans le dossier et liste tous les elements qui sont executable

        print ("Il y a ", len(FichList), " fichier ") # Affiche le reusltat
        print ("Il y a ", len(DosList), " dossier ") # Affiche le reusltat
        print ("Il y a " , len (ExeList), " éléments executable") # Affiche le reusltat
    except : # Si les commandes ne focntionne et donc que le lien n'est pas un dossier
        print ("Ce n'est pas un dossier")
        sys.exit()    
else : # Si pas d'argument
    print ("Pas de nom de dossier")