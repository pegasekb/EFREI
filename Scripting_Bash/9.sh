#Paul BLANC

# Créez un script prend plusieurs arguments :
#     a. -c
#         i. Cette option indique la création d’un fichier. Cette option doit être suivi du nom du fichier à créer. Si aucun nom n’est défini, le script retour une erreur. Le fichier est créé dans le répertoire courant, sinon un Fullpath est requis.
#     b. -r
#         i. Cette option permet d’afficher le contenu d’un fichier. Cette option doit être suivi du nom du fichier à lire, son absence retourne une erreur. Si le fichier n’existe pas, il faudrait demander à l’utilisateur de corriger le nom.
#     c. -a
#         i. Cette option permet d’ajouter des données à un fichier. Il doit être suivi du nom du fichier à modifier et ensuite la donnée à ajouter. La donnée a ajouté peut-être une chaine de caractères ou un fichier. Il faut vérifier au préalable que le fichier existe.
#     d. -d
#         i. Cette option permet de détruire un fichier. Il est suivi du nom du fichier à détruire.
#     e. -t
#         i. Cette option permet de vérifier le type du fichier. Il doit être suivi par le nom du fichier à analyser.


#!/bin/sh

#------------------------------
# Le -c
#------------------------------
if [ "$1" = "-c" ] #On verifie que l'argument 1 est bien un -c
    then
    if [ "$#" -gt "1" ] # On verifie qu'il y a au moins 2 argument
        then
        if [ -d "$3" ] # Si un argument 3 est un dossier 
            then
            cd "$3" #On se deplace dans se dossier
            touch "$2" #On creer le fichier avec le nom de l'argument 2
        else
            touch "$2"
        fi
    else
    echo "Il y a pas de nom de fichier il faut en mettre un"
    fi
fi
#------------------------
#------------------------
#Le -r
#------------------------

if [ "$1" = "-r" ] #On verifie que l'argument 1 est bien un -r
    then
    if [ "$#" -gt "1" ] # On verifie qu'il y a au moins 2 argument
        then
        if [ -f "$2" ] # Si l'argument 2 est un fichier
            then
            cat "$2" #On lit le fichier
        else
            echo "Le fichier n'existe pas"
        fi
    else
        echo "Il y a pas de nom de fichier il faut en mettre un"
    fi
fi

#------------------------
#------------------------
#Le -a
#------------------------

if [ "$1" = "-a" ] #On verifie que l'argument 1 est bien un -a
    then
        if [ -f "$2" ] && [ "$#" -ge "2" ] # On verifie si l'argument 2 est bien un fichier et qu'il y a au moins 2 argument
            then
                if [ "$#" -ge "3" ] # On verifie qu'il y a au moins 3 argument
                    then
                    if [ -f "$3" ] #On verifie que l'argument 3 est bien un fichier
                        then
                        cat "$3" >> "$2" #On ecrit le contenu du fichier de l'argument 3 dans le fichier de l'arguemnt 2
                    else
                        echo "$3" >> "$2" # On ecrit la chaines caratere de l'arguement 3 dans le fichier du l'arguement 2
                    fi
                else
                    echo "Il n'y a rien a ecrire dans le fichier"
                fi
        else
            echo "Il n'y a pas de fichier dans le quelle ecrire ou le fichier n'existe pas"
        fi
fi

#------------------------
#------------------------
#Le -d
#------------------------

if [ "$1" = "-d" ] #On verifie que l'argument 1 est bien un -d
    then
    if [ "$#" -gt "1" ] # On verifie qu'il y a au moins 2 argument
        then
        if [ -f "$2" ] # On verifie que l'arguement 2 est un fichier
            then
            rm "$2" # On supprime le fichier de l'argument 2
        else
            echo "Le fichier n'existe pas"
        fi
    else
        echo "Il y a pas de nom de fichier il faut en mettre un"
    fi
fi

#------------------------
#------------------------
#Le -t
#------------------------

if [ "$1" = "-t" ] #On verifie que l'argument 1 est bien un -t
    then
    if [ "$#" -gt "1" ] # On verifie qu'il y a au moins 2 argument
        then
        file "$2" # On analyse l'element de l'arguement 2
    else
        echo "Il y a pas de nom de fichier il faut en mettre un"
    fi
fi
