contactos = [ 
       { "nombre": "Dark", “apellido”: "Vador" }, 
       { "nombre": "Luke", “apellido”: "Skywalker" }, 
       { "nombre": "Han", “apellido”: "Solo" }, 
       ] 
 
for num, contacto in enumerate(contactos): 
   contacto['num'] = num 
   print( "%(num)05d | %(apellido)20s | %(nombre)20s |" % contacto) 
