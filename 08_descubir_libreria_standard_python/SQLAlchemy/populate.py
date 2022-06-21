from sqlalchemy import create_engine 
from sqlalchemy.orm import sesionmaker 
from sqlalchemy import select 
 
from definitions import Base, BASE_NAME 
from definitions import Contact 
 
from faker import Faker 
fake = Faker('es_ES') 
 
import datetime 
import random 
 
## Declaraciones de la base 
engine = create_engine(BASE_NAME) 
Base.metadata.bind = engine 
 
## Declaración de la sesión 
DBSession = sesionmaker(bind=engine) 
sesion = DBSession() 
 
## Nuestra función populate 
def populate( n ): 
 
   for c in range(1,n): 
 
       g = random.choice(['M','F']) 
       if g == 'M': 
           n = fake.name_male() 
       else: 
           n = fake.name_female() 
       t = fake.phone_number() 
       d = fake.date_of_birth(tzinfo=None, 
                   minimum_age=18, 
                   maximum_age=75) 
       j = fake.job() 
 
       ## La inserción de los datos
       r = Contact() 
       r.nombre = n 
       r.sexo = g 
       r.fecnac = d 
       r.tel = t 
       r.profesion = j 
       sesion.add(r) 
 
   ## Se valida todo de golpe 
   sesion.commit() 
 
def lista_contacto(): 
   #pudb.set_trace() 
   s = select([Contact]) 
   result = sesion.execute(s) 
 
   titulo  = "| {:30s} | {:20s} | {:10s} | {:5s} | {:30s} 
|".format( "Nombre", "Telefono", "Fecha N.", "Sexo", "Profesion" ) 
   print("=" * len(titulo)) 
   print(titulo) 
   print("=" * len(titulo)) 
   fmt  = "| {nombre:30s} | {tel:20s} | {fecnac:%d/%m/%Y} | 
{sexo:5s} | {profesion:30s} |" 
   for row in result: 
       print( fmt.format(**row) ) 
   print("=" * len(titulo)) 
 
if __name__ == "__main__": 
   if sesion.query(Contacto).count() == 0: 
       populate( 20 ) 
   lista_contacto()
