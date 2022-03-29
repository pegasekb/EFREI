# Créez un script prend plusieurs arguments :
# a. -c
# i. Cette option indique la création d’un fichier. Cette option doit être suivi du nom du fichier à créer. Si aucun nom n’est défini, le script retour une erreur. Le fichier est créé dans le répertoire courant, sinon un Fullpath est requis.
# b. -r
# i. Cette option permet d’afficher le contenu d’un fichier. Cette option doit être suivi du nom du fichier à lire, son absence retourne une erreur. Si le fichier n’existe pas, il faudrait demander à l’utilisateur de corriger le nom.
# c. -a
# i. Cette option permet d’ajouter des données à un fichier. Il doit être suivi du nom du fichier à modifier et ensuite la donnée à ajouter. La donnée a ajouté peut-être une chaine de caractères ou un fichier. Il faut vérifier au préalable que le fichier existe.
# d. -d
# i. Cette option permet de détruire un fichier. Il est suivi du nom du fichier à détruire.
# e. -t
# i. Cette option permet de vérifier le type du fichier. Il doit être suivi par le nom du fichier à analyser.