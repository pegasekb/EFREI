#Paul Blanc fini

# Créez un script prend plusieurs arguments:
# a.-c
#     i.  Cette option indique la création d’un fichier. 
#         Cette option doit être suivi du nom du fichier à créer. 
#         Si aucun nom n’est défini, le script retour une erreur.
#         Le fichier est créé dans le répertoire courant, sinon un Fullpath est requis

# b.-r
#     i.  Cette option permet d’afficher le contenu d’un fichier.
#         Cette optiondoit être suivi du nom du fichier à lire, son absence retourne une erreur. 
#         Si le fichier n’existe pas, il faudrait demander à l’utilisateur de corriger le nom.

# c.-a
#     i.  Cette option permet d’ajouter des données à un fichier. 
#         Il doit être suivi du nom du fichier à modifier et ensuite la donnée à ajouter. 
#         La donnée a ajouté peut-être une chaine de caractères ou un fichier. 
#         Il faut vérifier au préalable que le fichier existe.

# d.-d
#     i.  Cette option permet de détruire un fichier. Il est suivi du nom du fichier à détruire.

# e.-t
#     i.  Cette option permet de vérifier le type du fichier. Il doit être suivi par le nom du fichier à analyser.


$nbargs= $args.length

if ($nbargs -gt 1) {
    $existe = Test-Path $args[1]
    





    
    if ($args[0] -eq "-c"){

        if ($nbargs -gt 2){
            $dossierexiste = Test-Path $args[2]
            if ($dossierexiste -match "True"){
                New-Item -Path $args[2],$args[1] -ItemType File
                exit
            }
        }
        New-Item -Path $args[1] -ItemType File
        exit

    }

    if ($existe -match "False"){
        write-host "Le fichier n'existe pas"
        exit
    }
    if ($args[0] -eq "-r"){
        get-Content $args[1]
    }

    if ($args[0] -eq "-a"){
        Add-Content -Path $args[1] -Value $args[2]
    }

    if ($args[0] -eq "-d"){
        Remove-Item $args[1]
    } 

    if ($args[0] -eq "-t"){
        get-ItemProperty $args[1]
    }

} 
else { 
    write-host "Il n'y a pas assez d'arguments"
}