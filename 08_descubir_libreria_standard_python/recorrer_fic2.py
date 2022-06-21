from path import Path            ## necesita pip install path.py 
 
p = Path('/') / 'etc'            
print('Recorrido de %s ' % p) 
for l in p.walkfiles(errors='ignore'): 
   print(l)
