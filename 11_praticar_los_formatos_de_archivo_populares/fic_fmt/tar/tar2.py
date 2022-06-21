import tarfile 
from pathlib import Path 
 
archivo='test.tgz' 
a_guardar = 'test' 
 
p = Path(a_guardar) 
 
with tarfile.open(archivo, "w:gz") as tar: 
   for name in p.iterdir(): 
       print(name) 
       tar.add(name)
