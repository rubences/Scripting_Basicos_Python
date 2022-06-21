from pymongo import MongoClient 
from faker import Faker 
import random 
import datetime 
 
## creación de una sesión 
sesion  = MongoClient("mongodb://localhost:27017/") 
 
## conexión a la base de datos test 
db = sesion.test 
 
## Se recupera la lista de las colecciones de la base de datos 
colec = db.list_collection_names() 
 
## La colección que interesa 
contactos = db.contactos 
 
## Empezamos por limpiar la que existe 
if 'contactos' in colec: 
   print("Limpieza de la colección") 
   contactos.drop() 
 
fake = Faker('es_ES') 
nb = 100 
 
populate = [] 
 
for i in range(1, nb): 
   g = random.choice(['Masculino','Femenino']) 
   if g == 'Masculino': 
       n = fake.name_male() 
   else: 
       n = fake.name_female() 
   t = fake.phone_number() 
 
   ##  Fecha de nacimiento 
   dd = fake.date_of_birth(tzinfo=None, 
                              minimum_age=18, 
                              maximum_age=75) 
   dt = fake.time_object(end_datetime=None) 
   d = datetime.datetime.now() 
   d = d.combine( dd, dt) 
 
   j = fake.job() 
 
   populate.append( { 
       'nombre': n, 
       'teléfono': t, 
       'fecha_de_nacimiento': d, 
       'sexo': g, 
       'profesion': j, 
       }) 
 
## insertamos todo de golpe 
contactos.insert_many(populate) 
 
ed = datetime.datetime(2009, 11, 12, 12) #entorno de 18 años 
sd = datetime.datetime(1989, 11, 12, 12) #entorno de 30 años 
 
consulta = { 
           "fecha_de_nacimiento": { "$lt": ed, "$gte": sd } , 
           "sexo": "Masculino" 
       } 
 
fmt  = "| {:30s} | {:20s} | {:10s} | {:10s} | {:40s} |" 
for e in db.contactos.find( consulta ).sort("nombre"): 
   print( fmt.format( 
       e['nombre'], e['teléfono'],   
       e['fecha_de_nacimiento'].strftime("%x"), e['sexo'],   
       e['profesion'] 
       ) 
   )
