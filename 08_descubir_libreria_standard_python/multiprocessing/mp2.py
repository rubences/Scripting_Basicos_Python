import multiprocessing as mp 
import random 
import time 
 
# Definición de un canal de comunicación 
output = mp.Queue() 
 
# Función ejemplo con tiempo de espera
# + generación de números aleatorios 
def funcion(tiempo, output): 
   time.sleep(tiempo) 
   data = [ random.randint(0,100) for x in range(1,1000) ] 
   total = sum(data) 
   output.put(total) 
 
# Creación de una lista de procesos 
procesos = [mp.Process(target=funcion, args=(5, output)) for x 
in range(4)] 
 
# Ejecución de los procesos 
for p in procesos: 
   p.start() 
 
# Cierre de los procesos 
for p in procesos: 
   p.join() 
 
# Recuperación de los datos
resultados = [output.get() for p in procesos] 
 
print(resultados)
