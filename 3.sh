#Paul BLANC

# Créer un script qui permet de générer deux suites d’entier.Les bornes sont données par l’utilisateur. 
# Ensuite le script retourne « True » si les deux suites d’entiers on un intervalle en commun.


#!/bin/sh

echo "Interval 1"
read a1
read a2
echo "Interval 2"
read b1
read b2

if [ $a1 -gt $a2 ] # Verification que les bornes sont dans le bon ordres
then
    echo "Les bornes de l'interval 1 sont a l'enverre"
fi
if [ $b1 -gt $b2 ] # Verification que les bornes sont dans le bon ordres
then
    echo "Les bornes de l'interval 2 sont a l'enverre"
fi

if [ $a2 -lt $b1 -o $b2 -lt $a1 ] # Verification que les intervales ne se touche pas 
then
    echo "pas d'element en commun"
else 
    echo "TRUE"
fi

