# Créez un script qui prend comme argument deux répertoires. 
# Le script retourne les fichiers communs aux deux répertoires 
# qui ne partage pas le nom d’un répertoire. Les répertoires peuvent contenir 
# des sous répertoires. Aucune commande automatique n’est admise.

import os
import sys

liste1 = os.listdir (sys.argv[1])
liste2 = os.listdir (sys.argv[2])
#Reste a trouvé un moyen de filtrer les repertoir

for i in liste1 :
    for j in liste2: 
        if i == j : 
            print ('Il y a un element en commun qui est', j)