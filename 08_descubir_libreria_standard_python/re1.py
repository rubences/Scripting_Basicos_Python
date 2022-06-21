import re 
 
archivo = '/etc/group' 
 
pattern = r'\w*:\w:\d*:\w*' 
 
with open(archivo) as f: 
   for lig in f: 
       if re.match(pattern, lin): 
           pass # no hace nada si esto 'hace match' 
       else: 
           print("Línea fuera del patrón: %s " % lin)
