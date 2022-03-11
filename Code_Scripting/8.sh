#Paul BLANC

# Créez un script qui prend comme argument deux répertoires. 
# Le script retourne les fichiers communs aux deux répertoires qui ne partage pas le nom d’un répertoire. 
# Les répertoires peuvent contenir des sous répertoires. Aucune commande automatique n’est admise.



#!/bin/sh
valide=0
if [ "$#" -gt "1" ]
then
    if [ -d "$1" ] #On verifie que l'arguements est bien un dossier
        then
        if [ -d "$2" ] #On verifie que l'arguements est bien un dossier
            then
            cd "$1" #On se déplace dans le dossier 
            table1=( $(ls) ) #On mets dans un lite le resultat du ls 
            #tri_table1=( $(printf "%s\n" ${table1[*]} | sort -n) )# On les tris dans l'ordre croissant


            cd "$2" #On se déplace dans le dossier 
            table2=( $(ls) )  #On mets dans un lite le resultat du ls 
            #tri_table2=( $(printf "%s\n" ${table2[*]} | sort -n) )# On les tris dans l'ordre croissant
            

            for maChaine_1 in ${table1[@]} # On parcours 1 a 1 tous les element de la liste 1
            do
                for maChaine_2 in ${table2[@]} # On parcours 1 a 1 tous les elements de la liste 2
                do
                    if [ $maChaine_1 = $maChaine_2 ] # On comparts les 2 elements de chaques listes
                    then
                        echo "L'element $maChaine_1 est present dans les 2 dossiers"
                        valide=1
                        break # stop le for si un element a etait trouvé

                    elif [[ "$maChaine_1" < "$maChaine_2" ]]
                        then
                        break #stop la boucle si la chaine1 est petite que la chaines 2 car plus element ne peut correspondre

                    fi
                
                done
            done
        else 
            echo "Le 2eme argument n'est pas un dossier"
        fi
        else
            echo "Le 1er argument n'est pas un dossier"
    fi

else
    echo "Il faut mettre 2 arguments"

fi

if [ $valide -eq "0" ] # Si rien n'est trouvé on affiche 
then
echo "Il n'y a pas de fichier en commun dans ses dossiers"
fi
