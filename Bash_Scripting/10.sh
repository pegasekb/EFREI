#Paul BLANC

# Créez un script qui prend en argument des noms de fichier « .txt ». Ce dernier crée ces fichiers avec 1000 nombres aléatoires de l’intervalle « 0 – 10000 »


#!/bin/sh

function mille () #Boucle pour mettre les 1000 caratere dans les fichier creer
{
    for ((c=1; c<=1000; c++))
    do
    echo $((1 + RANDOM % 10000)) >> "$1"
    done
}

for count in $*
do
    if  [[ "$count" == *".txt" ]] #Verification si les argument continenne un .txt
        then
        touch "$count" # Creation du fichier.txt
        mille $count #Puis ajout des 1000 caratere
    fi
done

