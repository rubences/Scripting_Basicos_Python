import os 
import random 
from pathlib import Path 
from faker import Faker 
fake = Faker('es_ES') 
 
## Creación de un archivo con nombre, tamaño y contenido aleatorios
def create_file(rep, tamanio=1024, max_tamanio=5): 
   ext = random.choice([ "dat", "data", "dbf", "txt", "d" ]) 
   fname = fake.file_name(extension=ext) 
   path = rep / fname 
   print("Creación del archivo %s " % path ) 
   d = [] 
   with open("/dev/urandom", "rb") as r: 
       for x in range(0, random.randint(0,max_tamanio)): 
           b = r.read(tamanio) 
           d.append(b) 
 
   with open(path, "wb") as w: 
       for b in d: 
           w.write(b) 
 
## devuelve un objet Path() con un nombre aleatorio 
def create_rep(rep): 
   d = Path(fake.file_name() ) 
   return Path( rep , d.stem ) 
 
## Función recursiva 
def cr_nivel(padre, raiz): 
   nivel = padre + 1 
 
   ## Creación del nivel actual 
   rep_actual = create_rep(raiz) 
   rep_actual.mkdir() 
   print("Creación del directorio %s " % rep_actual ) 
 
   ## Creación de archivo 
   for x in range(0, random.randint(0,max_files)): 
       create_file(rep_actual, tamanio=BLOQUE, max_tamanio=MAX_BLOQUE) 
 
   ## ¿Creación de un nivel adicional? 
   if random.randint(0, 100) > PC_CR_NIVEL: 
       cr_nivel(nivel, rep_actual) 
 
## Creación de los directorios top nivel 
def create_top_rep(nb): 
   for x in range(0, nb): 
       cr_nivel(0, ROOT_DIR) 
 
 
## MANO 
ROOT_DIR = "a_guardar" 
#os.system('rm -es '+ROOT_DIR) #ATENCIÓN 
 
p = Path(ROOT_DIR) 
p.mkdir() 
 
max_rep = 5          ## Num max de directorios de base 
max_files = 5        ## Num max archivos/rep 
MAX_NIVEL = 3       ## Max niveles de arborescencia 
PC_CR_NIVEL = 40    ## % de creación de nivel 
                     ## (0=siempre 100=nunca) 
BLOQUE=1024*1024       ## Tamaño de bloque en bytes para 
                     ## la creación de archivos 
MAX_BLOQUE=5           ## Tamaño max de los archivos en número de bloques 
 
## Creación de los directorios TOP NIVEL 
create_top_rep( random.randint(1, max_rep) )
