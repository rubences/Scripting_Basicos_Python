## ------------- 
## SQLITE MEMORY 
## ------------- 
 
from sqlalchemy import select 
from definitions import connect 
from definitions import Producto 
 
from openff import get_prod 
 
import csv 
 
## ---------------------- 
## Rellenar la BDD 
## ---------------------- 
def populate(session, data): 
   for r in data: 
       p = Producto() 
       codigo, nombre, cantidad, marca, nutri, generic = r 
       p.codigo = codigo 
       p.nombre = nombre 
       p.cantidad = cantidad
       p.marca = marca 
       p.codigo_nutri = nutri 
       p.nombre_generico = generic 
       session.add(p) 
   session.commit() 
 
## ------------------------ 
## Uso de los datos 
## ------------------------ 
def generate_all(session, archivo): 
   s = select([Producto]) 
   prods = session.execute(s) 
   with open(archivo, 'w', newline='') as csvfile: 
       writer = csv.writer(csvfile, delimiter='\t') 
       writer.writerows(prods) 
 
def generate_marca(session, archivo): 
   req = """ 
   select marca, count(*) from PRODUCTOS 
   group by marca 
   order by marca 
   """ 
   prods = session.execute(req) 
   with open(archivo, 'w', newline='') as csvfile: 
       writer = csv.writer(csvfile, delimiter='\t') 
       writer.writerows(prods) 
 
 
 
## -------------------------- 
## El tratamiento principal 
## -------------------------- 
def main(): 
   session = connect()         # Creación + Init BDD 
   print("Recup de los datos") 
   data = get_prod()           # Recuperación des lo datos 
   print("Transf BDD") 
   populate(session, data)     # Relleno de la BDD 
   print("Archivo: PRODUCTOS") 
   fic = "PRODUCTOS.csv" 
   generate_all(session, fic)  # Uso de la BDD 
   print("Archivo: MARCAS") 
   fic = “MARCAS.csv" 
   generate_marca(session, fic) 
   session.close()             # Cierre Sesión + BDD 
 
if __name__ == '__main__': 
   main()
