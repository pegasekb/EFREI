# Créer un script qui prend en entrée un chemin et un type de fichier 
# (Ex : .txt, .py, etc). Le script ouvre un terminal pour afficher le contenu
# ou exécuter chaque fichier.
from time import sleep
import os
import sys


emplacement = sys.argv [1]
os.system( 'ls ,emplacement')

sleep (1)