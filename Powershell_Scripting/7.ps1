#Paul Blanc fini

# Créer un script qui prend en entrée des noms de fichier (Fullpath)(quantité illimité)
# a.Le script exécute le fichier si c’est un exécutable
# b.Le script imprime à vidéo si c’est un fichier textuel
# c.Retourne une erreur dans tous les autres cas

$nbarguments= $args.length

for ($arg = 0; $arg -lt $nbarguments; $arg++){
    $argencours = $args[$arg]
    $existe = Test-Path $argencours
    if ($existe -eq "True"){
        if ($argencours -match ".txt"){
            write-host "Voici le contenu du fichier ", $argencours
            Get-Content $argencours   
        }
        elseif($argencours -match ".ps1"){
            write-host "Le fichier ", $argencours," va etre executer"
            powershell $argencours
        }
        else {
            write-host "Le fichier ", $argencours, " n'est pas un .txt ou .ps1 rien n'est fait"
        }

    }
    else {
        write-host "Ce n'est pas un fichier"
        break
    }
}