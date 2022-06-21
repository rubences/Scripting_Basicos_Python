html_doc = """\ 
       <html> 
       <head> 
       <title> Mi Página Web </title> 
       </head> 
       <body> 
       <h1> Esta es una página WEB </h1> 
       <p> A continuación se muestra un pequeño texto a encontrar </p> 
       <ul> 
       <li> <a href="http://example.com/enlace1">Enlace 1</a> </li> 
       <li> <a href="http://example.com/enlace2">Enlace 2</a> </li> 
       <li> <a href="http://example.com/enlace3">Enlace 3</a> </li> 
       <li> <a href="http://example.com/enlace4">Enlace 4</a> </li> 
       </ul> 
       <table class='mi_class'> 
           <thead> 
               <td> Sistema </td> 
               <td> Gobierno </td> 
               <td> Nivel tecnológico </td> 
               <td> Población </td> 
           </thead> 
           <tbody> 
           <tr>     
               <td>Lave</td> 
               <td>Dictatura</td> 
               <td>Agricultores ricos</td> 
               <td>2,5 M</td> 
           </tr> 
           <tr>     
               <td>Teaatis</td> 
               <td>Feodal</td> 
               <td>Agricultores normales </td> 
               <td>1,6 M</td> 
           </tr> 
           <tr>     
               <td>Riinus</td> 
               <td>Comuistas</td> 
               <td>Industria media </td> 
               <td>4,2 M</td> 
           </tr> 
           <tr>     
               <td>Diurezza</td> 
               <td>Gobierno múltiple</td> 
               <td>Industriales Ricos</td> 
               <td>8,5 M</td> 
           </tr> 
           </tbody> 
 
       </table> 
       </body> 
       </html> 
""" 
 
from bs4 import BeautifulSoup 
import pprint 
 
pp = pprint.PrettyPrinter(indent=4) 
 
soup = BeautifulSoup(html_doc, 'lxml') 
 
print("== Título de la página ==") 
print( soup.title.text ) 
 
print("== Extracción de los enlaces ==") 
for l in soup.find_all('a'): 
   print(l.text, l.get('href')) 
 
## Extracción de la tabla 
data = [] 
table = soup.find('table', attrs={ 'class':'mi_class'}) 
tbody = table.find('tbody') 
 
for row in tbody.find_all('tr'): 
   cols = row.find_all('td') 
   elt = [ x.text for x in cols ] 
   data.append( elt ) 
 
print("== Extracción de la tabla ==") 
print(pp.pprint(data))
