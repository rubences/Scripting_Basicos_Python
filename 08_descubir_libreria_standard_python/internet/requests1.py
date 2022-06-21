import requests 
from bs4 import BeautifulSoup 
 
while palabra:= input("Palabra a buscar: "): 
   if palabra!= "salir": 
       url = "https://es.wiktionary.org/wiki/%s" % palabra 
       url += "#español" 
       try: 
           req = requests.get(url) 
           soup = BeautifulSoup(req.text, "lxml") 
           print(" Título: %s " % soup.h1.text ) 
           ol = soup.find_all('ol')[0] 
           print(ol.text) 
           print("-" * 70 ) 
       except: 
           print("Error ...") 
   else: 
       break
