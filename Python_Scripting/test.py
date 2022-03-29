import os

f = os.listdir(".")
compteur = 0

for f in f :
    if f.endswith(".txt"):        
        ext=f.split(".")
        os.rename(f,ext[0]+".dat")
        f.split
        compteur = compteur +1
        
print ("Il y a ",compteur, "fichiers qui ont etait transformé de .txt à .dat")
