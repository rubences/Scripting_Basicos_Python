from pymongo import MongoClient 
 
## creación de una sesión 
sesion  = MongoClient("mongodb://localhost:27017/") 
 
## conexión a la base de datos test 
db = sesion.test 
 
## La colección que nos interesa 
contactos = db.contactos 
 
## Empezamos limpiándola 
contactos.drop() 
 
## Creación de un contacto 
first_contacto = { 
       'name': 'Linus Torvalds', 
       'tel': '06 01 02 03 04', 
       'date_nai': '28-12-1969' 
       } 
 
result = contactos.insert_one(first_contacto) 
 
## Desde otro contacto 
otro_contacto = { 
       'name': 'Luke Skywalker', 
       'tel': '06 01 02 03 04', 
       'date_nai': '28-12-1969', 
       'comment': 'Chevalier Djedi' 
       } 
result = contactos.insert_one(otro_contacto) 
 
## Visualización de los contactos creados 
for doc in db.contactos.find(): 
   print(doc)
