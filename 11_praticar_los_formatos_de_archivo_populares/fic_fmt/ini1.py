import configparser as cp 
 
config = cp.ConfigParser() 
 
config.read("test.ini") 
 
for titulo, seccion in config.items(): 
   print("Sección: ", titulo ) 
   for clave, val in seccion.items(): 
       print(" %s = %s" % (clave, val)) 
