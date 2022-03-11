#Paul BLANC

# Crée un script qui permet d’authentifier des utilisateurs par nom et mot de passe. 
# Les informations d’authentification doivent être stockées dans deux fichiers différents pour des questions de sécurité. User.txt et pass.txt.


# Les User et est password sont dans 2 fichier difference et pour que l'Authentification soit valide il faut que le pwd soit sur le meme numero de ligne que le login:
# Exemlpe: 
# -----------------
# user.txt:
# -----------------
# user
# root
# admin
# test
# -----------------
# -----------------
# pass.txt:
# -----------------
# coucou
# salut
# password
# mdp


#La combinaison user - coucou fonctionnera
# Mais root - mdp non alors que test - mdp fonctionnera



#!/bin/sh
echo "Login :"
read log
echo "password :"
read pass

echo "Merci vous allez être authentifié"

compter=0
plus=1
for line in $(cat user.txt) 
    do
    compter=$(( $compter + $plus )) # compte le nombre de lignes 
    a=$(echo "$line") # ecrit le compte dans une variable  (j'ai eu des pb en utilisant la variable line directement)
    if [ "$a" = "$log" ] # Verifie que le login remplie correspond a la ligne du fichier user.txt
        then
        p="p"
        num="$compter$p" # Je fais on une concatenation car j'ai besion d'avoir le nombre du compter et un "p" pour que la commande mache
        if [ "$(sed -n $num pass.txt)" = "$pass" ] # Verification que le mdp est bien sur le meme numero de ligne que le login
            then
            echo "Mots de passe juste. Vous êtes authentifié"
        else
            echo "MDP faux"
        fi
    fi
done



