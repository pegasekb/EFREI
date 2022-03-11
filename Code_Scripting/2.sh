#Paul BLANC

# Créer un script qui demande à l’utilisateur de taper son nom et son prénom. Ces informations sont ensuite affichées sur le STDIN.


#!/bin/sh

echo "Mettre son Prenom"
read prenom
echo "Mettre son Nom"
read nom
echo "Tu t'appel $prenom $nom"


