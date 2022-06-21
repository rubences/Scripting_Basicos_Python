import signal 
import sys 
 
def interruption(signal, contexto): 
   print("Cierre como consecuencia de CTRL-C") 
   sys.exit(0) 
 
signal.signal(signal.SIGINT, interrupcion) 
 
print("Inicio del bucle infinito...") 
while True: 
   pass
