from configparser import ConfigParser, ExtendedInterpolation 
 
config =ConfigParser(interpolation=ExtendedInterpolation()) 
 
config.read("test3.ini") 
 
for titulo, seccion in config.items(): 
   print("Sección: ", titulo ) 
   for clave, val in seccion.items(): 
       print("   clave/val  %s = %s" % (clave, val))
