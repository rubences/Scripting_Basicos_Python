from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker 
 
from definitions import Base, BASE_NAME 
from definitions import Cliente, Producto, Proveed, Stock, Contador 
import datetime 
import random 
 
from faker import Faker 
fake = Faker('es_ES') 
import FakeProducto 
 
## ------------------------- 
## Creación de la sesión 
## ------------------------- 
 
engine = create_engine(BASE_NAME) 
Base.metadata.bind = engine 
 
DBSession = sessionmaker(bind=engine) 
session = DBSession() 
 
## ------------------------ 
## Creación de los Contadores 
## ------------------------ 
def contadores(): 
   r = Contador() 
   r.nombre = "FACTURA" 
   r.val = 1 
   session.add(r) 
 
   r = Contador() 
   r.nombre = "PEDCLI" 
   r.val = 1 
   session.add(r) 
 
   r = Contador() 
   r.nombre = "COMPROV" 
   r.val = 1 
   session.add(r) 
   session.commit() 
 
## --------------------- 
## Creación de los clientes 
## --------------------- 
def clientes(nb): 
   for c in range(1,nb): 
       r = Cliente() 
       t = random.choice( [ 'Ets', 'Sté' ] ) 
       r.nombre = "%s %s" % (t, fake.company()) 
       print("Creación Cliente de %s " % r.nombre) 
       session.add(r) 
       try: 
           session.commit() 
       except: 
           session.rollback() 
 
#Proveed 
def proveed(nb): 
   for c in range(1,nb): 
       r = Proveed() 
       t = random.choice( [ 'Ets', 'Sté' ] ) 
       #r.plazo = random.randint(5, 30) 
       ## para probar reappro 
       r.plazo = 0 
       r.nombre = "%s %s" % (t, fake.company()) 
       print("Creación Prov de %s " % r.nombre) 
       session.add(r) 
       try: 
           session.commit() 
       except: 
           session.rollback() 
 
 
#Producto 
def productos(nb): 
   ## Preparación de los productos 
   FakeProducto.init() 
   for c in range(1,nb): 
       r = Producto() 
       fp = FakeProducto.genera() 
       r.desc = fp.desc 
       r.precio = fp.precio 
       print("Creación de %s " % r.desc) 
       session.add(r) 
       try: 
           session.commit() 
       except: 
           session.rollback() 
 
 
#Stock 
def stock( almacen ): 
   prods = session.query(Producto).all() 
   for p in prods: 
       r = Stock() 
       r.almacen = almacen 
       r.producto = p 
       r.qstock = 10000 
       print("Creación de %s/%s " % (r.almacen,p.desc)) 
       session.add(r) 
       try: 
           session.commit() 
       except: 
           session.rollback() 
 
def main(): 
   contadores() 
   clientes(10) 
   proveed(10) 
   productos(10) 
   stock('D1') 
 
if __name__ == '__main__': 
   main() 
