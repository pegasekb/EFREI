#Paul Blanc fini

# Créer un script qui affiche son propre nom et tous ses arguments.
# a.EX : ./monscript.py hello world
# b.Affiche : « Nom du script: monscript.py»
# c.Affiche : « mes arguments : hello world »

Write-Host 'Nom du script : ' $MyInvocation.MyCommand.Name
Write-Host 'Mes arguments :' $args
