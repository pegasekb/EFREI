#Paul Blanc fini

# Créer un script qui prend comme argument le nom d’un fichier.
# Le script doit rechercher le fichier dans le répertoire courant 
# et remonter jusqu’à deux niveaux. Le script va aussi rendre le nombre d’occurrences 
# du fichier.


import sys
import os


fichier = sys.argv[1] # On mets le nom du fichier dans la variable
count = 0 # On mets a 0 un compteur
        

for i in range (0,3) : # On defini de compbien on va remonter dans l'arboraisance
    f = os.listdir(".") # On defini f comme une liste de tous les elements present dans le repertoir courant
    for f in f: # On fait une boucle pour tester tous les elements de la liste
        print (f)
        if f == fichier : # On compart si l'element de la liste est = au nom du fichier
            count =  count+1 # Si on trouve une corespondance on ajoute +1 au compteur
        elif f > fichier : # Si f plus grand que le nom du fichier on stop pour etre plus optimiser
            break
    os.chdir ("..") # On va dans le repertoir parents
    

    
print("Le fichier à était trouvé ", count, " fois") # On affiche les resultat

