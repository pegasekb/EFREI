#Paul BLANC

#Créer un script qui affiche son propre nom et tous ses arguments.

# a. EX : ./monscript.sh hello world
# b. Affiche : « mon nom : monscript.sh »
# c. Affiche : « mes arguments : hello world »

#!/bin/sh

echo "Mon nom : "$(basename "$0")""
echo "Mes aruments sont : $@"



