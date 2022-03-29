#Paul BLANC

# Créer un script qui prend comme argument le nom d’un fichier. 
# Le script doit rechercher le fichier dans le répertoire courant et remonter jusqu’à deux niveaux. 
# Le script va aussi rendre le nombre d’occurrences du fichier.

#!/bin/sh

nombre=0

nombre=$(ls -l | egrep -v 'd' | grep $1 | wc -l ) # COmment pour voir si le fichier existe dans le dossier courant
for ((c=1; c<=2; c++)) #Boucle qui permet de remonter de 2 dans l'arboréssance
do
cd ..
nombre=$(( $nombre + $(ls -l | egrep -v 'd' | grep $1 | wc -l ) )) # Compteur du nombre de fois que le fichier apparait
done

echo "Le fichier à était trouvé $nombre fois"





