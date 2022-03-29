
table1=( $(ls) )

cd ..
table2=( $(ls) )

for maChaine_1 in ${table1[@]}
    do
    for maChaine_2 in ${table2[@]}
        do
        if [[ "$maChaine_1" < "$maChaine_2" ]]
            then
            echo "$maChaine_1 et plus petit que $maChaine_2"
            break
        elif [[ "$maChaine_1" > "$maChaine_2" ]]
            then
            echo "$maChaine_1 et plus grand que $maChaine_2"
        elif [[ "$maChaine_1" == "$maChaine_2" ]]
            then
            echo "Les 2 sont egal"
            break
        fi
    done
    echo " suivant"
    echo ""
done