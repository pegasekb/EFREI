# Créer un script qui prend une chaine de caractère donné par l’utilisateur et 
# qui l’affiche mot par mot. EX : « Nous sommes au cours de Scripting»
# ******************************************************
# *                                                    *
# *         Nous sommes au cours de scripting          *
# *            *****************************           *
# *                         Date                       *
# *                         Heure                      *
# *                     ***************                *
# ******************************************************


# Arcaique mais je ne suis pas sur d'avoir bien compris le sujet
import time
import sys

print ("******************************************************\n*                                                    *\n")
print ("                      "," " .join(sys.argv[1:]),"\n*            *****************************           *")
print ("                       ", time.strftime('%Y-%m-%d'))
print ("                        ", time.strftime('%H:%M:%S'))
print ("*                     ***************                *\n******************************************************")