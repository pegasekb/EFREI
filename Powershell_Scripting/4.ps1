#Paul Blanc fini

# Crée un script qui permet d’authentifier des utilisateurs par nom et mot de passe. 

# a.Les informations d’authentification doivent être stockées dans 
#   deux fichiers différents pour des questions de sécurité. User.txt et pass.txt.

# b.Le script doit stocker dans un fichier de log la date et l’heure de chaque tentative.
#   Un fichier de log par utilisateur.

# c.Un maximum de 5 tentatives admises

# d.Le script propose un nom et un mot de passe alphanumérique à l’utilisateur

$test = 0
for ($b = 0; $b -lt 5; $b++) {


$Login = Read-Host "Login" 
$Pass = Read-Host "Password" #-AsSecureString 
Write-Host $Pass
$nbline = (Get-content "user.txt").Length



    

For($i=0;$i -lt $nbline;$i++)
{
    $lignelog  = (Get-content ("user.txt"))[$i]
    if ($lignelog -eq $Login){
        $test = 1
        $lignepass  = (Get-content ("pass.txt"))[$i]
        $Dateheure= get-date
        if ($lignepass -eq $Pass) {
            Write-Host "Vous etes authentifie"
            Add-Content -Path "$Login.txt" -Value "Connection reussi sur le compte $Login à $Dateheure"
        }
        else {
            Write-Host "Mauvais login ou password"
            Add-Content -Path "$Login.txt" -Value "Connection échoué sur le compte $Login à $Dateheure"
        }
    }
    elseif ($lingelog -gt $login) {
        break
    }
    
}
}
Write-Host "Trop de connection avec echec"

if ($test -eq 0) {
Write-Host "Si vous voulez vous enregister voici votre login et password"


$Newpass = -join (1..20 | ForEach {[char]((97..122) + (48..57) | Get-Random)})
Write-Host $Login
Write-Host $Newpass
$reponse = Read-Host "Ce mdp vous convient ? O / N"
if ($reponse -eq "O")  {
    Add-Content -Path "user.txt" -Value $Login
    Add-Content -Path "pass.txt" -Value $Newpass
    Write-Host "Les infos sont enregistrer"
    
}
}

