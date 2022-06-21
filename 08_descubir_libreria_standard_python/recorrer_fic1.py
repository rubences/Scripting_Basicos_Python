import os 
import tempfile 
import glob 
from path import Path   ## hay que lanzar pip install path.py 
 
def create_dir(d_base, nombre): 
   d = os.path.join( d_base, nombre) 
   os.mkdir(d) 
   return d 
 
def create_fic( rep, nombre ): 
   archivo = os.path.join( rep, nombre ) 
   with open(archivo, 'w+') as fic: 
       fic.write( "archivo: %s \n" % nombre ) 
 
with tempfile.TemporaryDirectory() as dir_base: 
   ## creamos directorios 
   rep = [] 
   rep.append( create_dir(dir_base, 'DIR1') ) 
   rep.append( create_dir(dir_base, 'DIR2') ) 
   rep.append( create_dir(dir_base, 'DIR3') ) 
 
   # después archivos 
   fic = [] 
   fic.append( create_fic(rep[0], "archivo1" ) ) 
   fic.append( create_fic(rep[1], "archivo2" ) ) 
   fic.append( create_fic(rep[1], "archivo2_1" ) ) 
   fic.append( create_fic(rep[1], "archivo2_2" ) ) 
   fic.append( create_fic(rep[2], "archivo3" ) ) 
   fic.append( create_fic(rep[2], "archivo3_1" ) ) 
   fic.append( create_fic(rep[2], "archivo3_2" ) ) 
   fic.append( create_fic(rep[2], "archivo3_3" ) ) 
 
   # y subdirectorios 
   srep = [] 
   srep.append( create_dir(rep[1], 'SDIR1') ) 
   srep.append( create_dir(rep[1], 'SDIR2') ) 
   srep.append( create_dir(rep[1], 'SDIR3') ) 
 
   # y archivos en los subdirectorios 
   fic.append( create_fic(srep[0], "sarchivo1" ) ) 
   fic.append( create_fic(srep[1], "sarchivo2" ) ) 
 
   ## recorremos este directorio dir_base ... 
 
   print("=== Recorrido con os.walk ===") 
   for l in os.walk( dir_base ): 
       print( l ) 
 
   print("=== Recorrido con glob ===") 
   for l in glob.glob( dir_base+'/**', recursive=True): 
       print(l) 
 
   print("=== Recorrido con path ===") 
   for l in Path(dir_base).walkfiles(): 
       print(l)
