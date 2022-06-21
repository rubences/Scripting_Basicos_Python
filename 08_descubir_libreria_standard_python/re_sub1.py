import path 
from path import Path 
import re 
 
with path.TempDir() as dir_base: 
 
   archivo = Path(dir_base) / 'archivo1' 
 
   ## generación de un archivo con números de líneas 
   lins = [] 
   for n in range(995,1005): 
       lins.append( '{0:03d} Línea no {0:3d}\n'.format(n) ) 
   archivo.write_lines(lins) 
 
   print("ANTES DE LA MODIF") 
   print(archivo.text()) 
 
    
   ## Modificamos los números de línea 
   p = Path(dir_base) / 'archivo1' 
   assert p.isfile() 
   with p.in_place() as (reader, writer): 
       for n, lig in enumerate(reader, 995): 
           num = '{0:05d}:'.format(n) 
           lig = re.sub(r"^\d{3,4}", num, lig) 
           writer.write(lig) 
 
   print("DESPUÉS DE MODIF") 
   print(p.text()) 
