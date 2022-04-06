#Paul Blanc fini

#Créer un script qui prend en argument le nom d’un répertoire. 
# Le script doit s’assurer que le fichier mis en argument est un répertoire, 
# ensuite compter le nombre de répertoires, le nombre de fichiers à l’intérieur du répertoire. 
# Le script affiche ces informations.

# Il faudrai mettre un verificateur de chemin

$result = Test-Path $args

if ($result -eq "True") {
Write-Host $args 

Write-Host "nombre de fichier : "
Get-ChildItem $args -File | Measure-Object | %{$_.Count}
Write-Host "nombre de dossier : "
Get-ChildItem $args -Directory | Measure-Object | %{$_.Count}
}
else {
    Write-Host "Le dossier n'existe pas"
}