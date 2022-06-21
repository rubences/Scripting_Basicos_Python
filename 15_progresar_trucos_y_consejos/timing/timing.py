import time 
 
## --------------- 
## Clase Timing 
## --------------- 
class timing(): 
   def __init__(self, label="timing"): 
       self.inicio = 0 
       self.label = label 
    
   def _pr(self, etiqueta): 
       print( etiqueta) 
 
   def tps_intermedio(self, l_inter=""): 
       if not l_inter: 
           l_inter = self.label 
       self._pr("Tiempo intermed {label:s} timing {tiempo:.3f}" 
       .format(label=l_inter,  
               tiempo=time.time() - self.inicio)) 
 
   def __enter__(self): 
       self.inicio = time.time() 
       self._pr("Inicio de %s " % self.label) 
       return self 
 
   def __exit__(self, exc_type, exc_value, traceback): 
       self._pr("Fin de {label:s} timing {tiempo:.3f}" 
       .format(label=self.label,  
           tiempo=time.time() - self.inicio)) 
 
def test(): 
   import math 
   with timing(label="Función math.sin") as t: 
       for x in range(1, 500_000): 
           if not x % 100_000: 
               t.tps_intermedio() 
           y = math.sin(x) 
 
if __name__ == "__main__": 
   test()
