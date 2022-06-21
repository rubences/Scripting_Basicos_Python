import tarfile 
archivo = "test.tgz" 
fmt = "|{name:30s}|{size:10s}|{typ:20s}|" 
tar = tarfile.open(archivo, "r:gz") 
total = 0 
 
## Encabezado
info = { 'name': 'Fichero ', 'size': 'Tamaño', 'typ': 'Tipo' } 
t = len(fmt.format(**info)) 
print("-" * t) 
print(fmt.format(**info)) 
print("-" * t) 
 
## para todas las entradas del archivo 
fmt = "|{name:30s}|{size:10d}|{typ:20s}|" 
for tarinfo in tar: 
   info = tarinfo.get_info() 
   total += info['size'] 
   #print(info) 
   if tarinfo.isreg(): 
       info['typ'] = "Fichero" 
   elif tarinfo.isdir(): 
       info['typ'] = "Directorio" 
   else: 
       info['typ'] = "Otro" 
   print(fmt.format(**info)) 
tar.close() 
 
info = { 
       'name': 'Total ', 
       'size': total, 
       'typ': '' 
       } 
print("-" * t) 
print(fmt.format(**info)) 
print("-" * t)
