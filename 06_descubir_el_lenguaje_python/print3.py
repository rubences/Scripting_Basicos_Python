contactos = [ 
       { "nombre": "Dark", “apellido”: "Vador" }, 
       { "nombre": "Luke", “apellido”: "Skywalker" }, 
       { "nombre": "Han", “apellido”: "Solo" }, 
       ] 
 
for num, contacto in enumerate(contactos): 
   print( "{num:05d}|{contacto[nombre]:15s}|{contacto[nombre]:15s}"  
.format( num=num, contacto=contacto))
