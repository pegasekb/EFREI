#Paul BLANC

# Créer un script qui prend une chaine de caractère donné par l’utilisateur et qui l’affiche mot par mot. EX : « Nous sommes au cours de Scripting»
# ******************************************************
# *                                                    *
#              Nous sommes au cours de scripting       *
# *             ******************************
#                            Date                      *
#                            Heure                     *
# *                    ****************
# ******************************************************

# La methode est arcaique et je n'etait pas sur d'avoir compris l'ennocé

#!/bin/sh
date=$(date +%x)
heure=$(date +%T)

echo "******************************************************"
echo "*                                                    *"
echo "                          $@"
echo "*             ******************************         *"
echo "                         $date"
echo "                          $heure"
echo "*                    ****************                *"
echo "******************************************************"

