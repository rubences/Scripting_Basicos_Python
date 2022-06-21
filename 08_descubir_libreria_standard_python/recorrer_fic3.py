from path import Path 
import re 
 
d = Path('/proc') 
 
memoire = {} 
 
for p in d.glob('*/stat'): 
   if p.isfile(): 
       with open(p) as f: 
           m = re.search(r'^([0-9]*)\s\((.*)\)(.*)$', 
                                f.readline()) 
           pid, comm, el_resto = m.groups() 
           data = el_resto.split() 
           vsize = int(data[20])/1024 
           clave = pid 
           if clave in memoria: 
               memoria [clave] += vsize 
           else: 
               memoria [clave] = vsize 
 
# muestra el resultado 
p = [ (v,k) for k,v in memoria.items() ] 
for v,k in sorted(p): 
   if v: 
       print("%20s: %10d Kb" %(k,v) )
