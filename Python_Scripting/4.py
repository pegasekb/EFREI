# Créer un script qui permet de générer deux suites d’entier contigu.
#  Les bornes sont données par l’utilisateur. Ensuite le script retourne « True »
#  si les deux suites d’entiers ont un intervalle en commun.

print ("Définisez l'intervale 1 :")  # On demande les intervales
a1 = input ()
a2 = input ()
print ("Définisez l'intervale 2 :") # On demande les intervales
b1 = input ()
b2 = input ()

if a1 > a2 or b1 > b2 : # on verifié que les bornes soit du plus grand au plus petit dans chaque intervales
    print ("Les bornes de lun des intervales sont à l'enverre")
    
if a2 < b1 or b2 < a1 : # On s'assure que les intervales n'ont rien en commun 
    print ("Il n'y a pas l'élément en commun")
else : # On peut donc en conclure qu'il y a un intervale en commun
    print ("True")