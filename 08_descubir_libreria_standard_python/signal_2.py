import signal 
import os 
import time 
 
def alarme(signal, contexto): 
   print("Recepción de la señal no %s " % signal ) 
   raise OSError("ALARMA") 
 
MAX_TIME = 5          # en segundos 
 
signal.signal(signal.SIGALRM, alarma) 
signal.alarm(MAX_TIME) 
 
print("Inicio del tiempo de espera") 
try: 
   time.sleep(15)    # aquí el procesamiento que no debe exceder 
                     # MAX_TIME 
except: 
   pass              # Aquí la intercepción del error 
                     # y de la alarma 
 
# si no continuaos
print("Fin del tiempo de espera") 
 
signal.alarm(0)
