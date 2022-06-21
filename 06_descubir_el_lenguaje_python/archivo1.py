
archivo = "data.txt"           # el nombre del archivo 
 
fd = open(archivo)             # apertura 
 
for l in fd:                   # lectura línea a línea 
   print("l=%s" % l, end='')   # utilización de los datos
 
fd.close()                     # cierre
