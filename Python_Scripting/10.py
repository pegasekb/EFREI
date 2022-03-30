#Paul Blanc

# Le script retourne les fichiers communs aux deux répertoires 
# qui ne partage pas le nom d’un répertoire. Les répertoires peuvent contenir 
# des sous répertoires. Aucune commande automatique n’est admise.

import os
import sys

liste1 = [ f for f in os.listdir(sys.argv [1]) if os.path.isfile(os.path.join(sys.argv [1],f)) ] # Pour lister seulement les fichier de l'argugment 1
liste2 = [ f for f in os.listdir(sys.argv [2]) if os.path.isfile(os.path.join(sys.argv [2],f)) ] # Pour lister seulement les fichier de l'argugment 2

count =0
for i in liste1 : # On tester les element de la liste 1
    for j in liste2: # Avec les elements de la liste 2
        if i == j : # Et on regarde si ca match
            count =1
            print ('Il y a un element en commun qui est', j)
        elif j >= i : # On evite de calculer si on a dépassé l'element
            break 
if count ==0 : #Si aucun element n'a etait trouvé
    print ("Il y a pas d'element en commun")