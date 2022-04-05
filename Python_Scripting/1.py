#Paul Blanc & Jay AMIN fini

# Créer un script qui affiche son propre nom et tous ses arguments.
# a. EX : ./monscript.py hello world
# b. Affiche : « Nom du script : monscript.sh »
# c. Affiche : « mes arguments : hello world »

import string
import sys

print ("Nom du script : ",sys.argv[0])
print ("Mes arguments : ", " ".join(sys.argv[1:]))  # Join permet de creer un chaine de caratere avec un liste 
                                                    # en faisant la joinction avec ce qui est entre ""