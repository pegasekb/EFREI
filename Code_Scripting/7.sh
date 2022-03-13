#Paul BLANC

# Créer un script qui prend en argument le nom d’un répertoire (fullpath). 
# Le script doit s’assurer que le fichier mis en argument est un répertoire, ensuite compter le nombre de répertoires, 
# le nombre d’exécutable et le nombre de fichiers à l’intérieur. Le script affiche ces informations


#!/bin/sh


if [ -d "$1" ] #On verifie que l'argument donnée est bien un dossier
then

cd "$1" #On se deplace dans ce dossier

exe=$(ls -Fla | grep \*$ | wc -l) # Compte les fichier qui sont  executable dans le repertoir courant
dir=$(ls -d */ | wc -l) # Compte les dossier dans le repertoir courant
file=$(ls -l | egrep -v '^d' | wc -l) # Compte les fichier dans le repertoir courant


echo "Dans le repertoir $(pwd) :"
echo "Il y a $dir dossier(s)"
echo "Il y a $file fichier(s)"
echo "Dont $exe fichier(s) executable"
fi