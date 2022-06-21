import re 
from path import Path 
import matplotlib.pyplot as plt 
 
dir_base = '/var/log/sysstat'  # puede ser diferente en el resto 
                               # de distribuciones     
data = {} 
 
STORE=False 
 
### recuperación de datos 
for f in Path(dir_base).glob('sar*'): 
   with open(f) as fic: 
       lins = fic.readlines() 
       for l in lins: 
           d = re.findall( r'\S+', l) 
           if '%idle' in d: 
               STORE = True 
               continue 
           if 'Media' in d: 
               STORE = False 
               continue 
           if STORE: 
               if 'all' in d: 
                   t = d[0] 
                   pcu = 100 - int(float(d[-1].replace(',','.'))) 
                   cle = f.basename() 
                   if cle in data: 
                       data[clave][0].append(t) 
                       data[clave][1].append(pcu) 
                   else: 
                       data[clave] = [ [t], [pcu] ] 
   break  # un único archivo 
 
## visualización en modo gráfico 
clave = list(data.keys())[0] 
x = data[clave][0] 
y = data[clave][1] 
plt.plot(x,y) 
## Eliminación de las etiquetas del eje X por ilegibles 
plt.xticks([],[]) 
plt.show()
