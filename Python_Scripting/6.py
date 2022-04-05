#Paul Blanc

# Créer un script qui prend en entrée un chemin et un type de fichier 
# (Ex : .txt, .py, etc). Le script ouvre un terminal pour afficher le contenu
# ou exécuter chaque fichier.

import os
from posixpath import split
import string
import sys

try :
    print (open(sys.argv[1], 'r').read)
    test=1
        
except :
    test=0

if (test == 1) :
    try :
        cat ='cat '+sys.argv[1]
        os.system(cat)
    except: 
        exe='./'+sys.argv[1]
        os.system(exe)
else : 
 
       os.listdir ('.')




# emplacement = sys.argv [1]
# os.system( 'ls ,emplacement')