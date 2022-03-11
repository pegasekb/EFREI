#Paul BLANC

# Créer un script qui prend comme argument le nom d’un fichier. 
# Le script doit rechercher le fichier dans le répertoire courant et remonter jusqu’à deux niveaux. 
# Le script va aussi rendre le nombre d’occurrences du fichier.

#!/bin/sh


for ((c=1; c<=2; c++)) #Boucle qui permet de remonter de 2 dans l'arboréssance
do
cd ..
done

find . | grep $1 # Recherche avec le find le fichier dans les dossiers 
nombre=$(find . | grep $1 | wc -l ) # Compte le nb de fois que le fichier a etait trouvé
echo "Le fichier à était trouvé $nombre fois"





