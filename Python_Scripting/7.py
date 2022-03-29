# Créer un script qui prend comme argument le nom d’un fichier.
# Le script doit rechercher le fichier dans le répertoire courant 
# et remonter jusqu’à deux niveaux. Le script va aussi rendre le nombre d’occurrences 
# du fichier.


import sys
import os


fichier = sys.argv[1]
count = 0
        

f = os.listdir(".")
for i in range (0,3) :
    f = os.listdir(".")
    for f in f:
        if f == fichier :
            count =  count+1
    os.chdir ("..")
    

    
print("Le fichier à était trouvé ", count, " fois")

