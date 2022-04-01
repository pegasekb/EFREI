#Paul Blanc

# Créer un script qui prend une chaine de caractère donné par l’utilisateur et qui l’affiche mot par mot. 
#EX: «Nous sommes au cours de Scripting»
# ******************************************************
# *                                                    *
#               Nous sommes au cours de scripting       
# *               *****************************        *
# *                         Nom Host                   *
# *                    Répertoire courant              *
# *                     ***************                *
# ******************************************************
# 
# 


Write-Host "******************************************************"
Write-Host "*                                                    *"
Write-Host "                       "$args
Write-Host "*               *****************************        *"
Write-Host "                "$env:COMPUTERNAME
Write-Host "                   "$Pwd
Write-Host "*                     ***************                *"
Write-Host "******************************************************"
