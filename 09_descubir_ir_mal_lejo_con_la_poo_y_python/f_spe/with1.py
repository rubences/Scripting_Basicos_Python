import math 
import time 
 
class timing(): 
   def __init__(self, label=""): 
       self.inicio = 0 
       self.label = label 
       if label: 
           print("inicio de %s " % label) 
 
   def __enter__(self): 
       self.inicio = time.time() 
 
   def __exit__(self, exc_type, exc_value, traceback): 
       if self.label: 
           print("Fin de %s " % self.label, end="") 
       print('Timing {:.3}s'.format(time.time() - self.inicio)) 
 
def test(): 
   with timing(label="Función math.sin"): 
       for x in range(1, 1000): 
           y = math.sin(x) 
   with timing(label="Función math.cos"): 
       for x in range(1, 1000): 
           y = math.cos(x) 
 
if __name__ == "__main__": 
   test()
