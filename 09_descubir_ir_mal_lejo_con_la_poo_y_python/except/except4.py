class MiExcepcion(Exception): 
   """ 
   La documentation es primordial sobre todo para las excepciones 
   que, recuerdo, no son objetos sin importancia
   """ 
   def __init__(self, message): 
       self.message = message 
 
   def __str__ (self): 
       return "MiExcepcion msg=%s" % self.message 
 
 
try: 
   print("Antes del error") 
   raise MiExcepcion("MENSAJE DE ERROR") 
   print("Después del error") 
except MiExcepcion as err: 
   print("Error: [%s]" % err )
