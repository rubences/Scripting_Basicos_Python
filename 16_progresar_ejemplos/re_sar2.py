import re 
from path import Path 
import matplotlib.pyplot as plt 
 
dir_base = '/var/log/sysstat' # debian ubuntu 
dir_base = '/var/log/sa'      # RedHat 
dir_base = 'sar_data'         # para el ejemplo 
 
data = {} 
 
STORE=False 
 
### recuperación de los datos 
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
                   t = d[0][0:2] 
                   pcu = 100 - int(float(d[-1].replace(',','.'))) 
                   clave = f.basename() 
                   if clave in data: 
                       data[clave][0].append(t) 
                       data[clave][1].append(pcu) 
                   else: 
                       data[clave] = [ [t], [pcu] ] 
 
## cálculo de la media 
media = {} 
for clave in data.keys(): 
   for i,c in enumerate(data[clave][0]): 
       h = data[clave][0][i] 
       v = data[clave][1][i] 
       if h in media: 
           t_v, t_nb = media[h] 
           media[h] = ( t_v + v, t_nb+1 ) 
       else: 
           media[h] = (v,1) 
 
for m in media.keys(): 
   t_v, t_nb = media[m] 
   media[m] = ( t_v, t_nb, round(t_v/t_nb)) 
 
## visualización en modo gráfico
for clave in data.keys(): 
   x = data[clave][0] 
   y = data[clave][1] 
   plt.plot(x,y, '.b') 
for clave in media.keys(): 
   x = clave 
   y = media[clave][2] 
   plt.plot(x, y, 'or', markersize=10) 
plt.gcf().autofmt_xdate() 
plt.show()
