# Faire un scrpit qui :
#Scann le reseaux
#Trouver les service important
#Touver la version des services
#Touver les vulnérabilité
#Searchploit acces a la BDD de exploit DB

import socket 
import time
import nmap
  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
cible = (input('La machine à scanner ?')) 
  
def port_scan(port): 
    try: 
        s.connect((cible, port)) 
        return True
    except: 
        return False
  
  
for port in range(5): 
    if port_scan(port): 
        print(f'le port {port} est ouvert') 
    else: 
        print(f'le port {port} est fermé') 

