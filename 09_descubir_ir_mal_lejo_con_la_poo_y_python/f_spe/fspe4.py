class A(object): 
 
   def __init__(self): 
       self.ingredients = [] 
       self.status = None 
 
   def __getattr__(self, attr): 
       if attr == 'nombre': 
           return "Hago lo que quiero con nombre" 
       else: 
           return "Inexistente" 
 
 
if __name__ == '__main__': 
   sopa = A() 
   print("sopa.nombre = ", sopa.nombre) 
   print("sopa.inexistente = ", sopa.inexistente)
