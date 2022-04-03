#Paul Blanc

# Créer un script qui prend deux répertoirescomme paramètres
# a.Le script vérifie que les deux répertoires existent puis retourne un fichier «.dat» 
# contenant les fichiers partagés et non partagés entre les deux répertoires.



$dossier1 = Read-Host "Dossier 1"
$dossier2 = Read-Host "Dossier 2"

$dir1 = Get-ChildItem -Path $dossier1 -Name
$dir2 = Get-ChildItem -Path $dossier2 -Name
# Write-Host $dir1
# Write-Host $dir2

for ($linedir1 = 0; $linedir1 -lt $dir1.Count; $linedir1++) {
    # write-host " "
    # Write-Host $dir1[$linedir1]

    # Write-Host $linedir1

    for ($linedir2 = 0; $linedir2 -lt $dir2.Count; $linedir2++) {
        # Write-Host $dir2[$linedir2]
        # Write-Host $linedir2
        if ($dir1[$linedir1] -eq $dir2[$linedir2]) {
            Add-Content -Path "filecommun.dat" -Value ($dir1[$linedir1], "est dans les 2 repertoir"       )
        }
    }


}