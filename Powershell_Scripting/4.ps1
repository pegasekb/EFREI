#Paul Blanc

# Crée un script qui permet d’authentifier des utilisateurs par nom et mot de passe. 

# a.Les informations d’authentification doivent être stockées dans 
#   deux fichiers différents pour des questions de sécurité. User.txt et pass.txt.

# b.Le script doit stocker dans un fichier de log la date et l’heure de chaque tentative.
#   Un fichier de log par utilisateur.

# c.Un maximum de 5 tentatives admises

# d.Le script propose un nom et un mot de passe alphanumérique à l’utilisateur

$Login = Read-Host "Login" 
$pass = Read-Host "Password" -AsSecureString 
$nbline = (Get-content "user.txt").Length


For($i=0;$i -lt $nbline;$i++)
{
    $ligne  = (Get-content ("user.txt"))[$i]
    if ($ligne -eq $Login){
        Write-Host $ligne
    }

}
# Write-Host $Login $pass
Write-Host $nbline


