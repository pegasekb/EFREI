#Paul Blanc fini

# Créer un script qui renomme tous les fichiers « .txt » dans
# le répertoire courant en fichier « .dat ».

import os

f = os.listdir(".") # On liste tous les fichiers des du dossier
compteur = 0 # mise en place du compteur

for f in f : # On fait un for pour sur toute la liste du dossier
    if f.endswith(".txt"): #Si l'extension est .txt        
        ext=f.split(".") # On difise le nom en 2 au niveau du .
        os.rename(f,ext[0]+".dat") # on rename le fichier en séléctionner la premiere partie du nom et en changant la fin en .dat 
        compteur = compteur +1 # Ajoute 1  au compteur pour la fin
        
print ("Il y a ",compteur, "fichiers qui ont etait transformé de .txt à .dat")
        