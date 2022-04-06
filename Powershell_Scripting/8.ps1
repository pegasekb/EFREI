#Paul Blanc fini

# Créer un script qui renomme tous les fichiers «.txt» dans le répertoire courant en fichier «.dat».

$listetxt = Get-ChildItem -Name *.txt
Write-Host $listetxt
for ($line = 0; $line -lt $listetxt.Count; $line++) {
    Dir *.txt | Rename-Item -NewName { $_.name -Replace '\.txt$','.dat' }
}
