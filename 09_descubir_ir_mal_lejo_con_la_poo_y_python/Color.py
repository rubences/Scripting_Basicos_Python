class Color: 
   def __init__(self, r, v, b): 
       self.rojo = r 
       self.verde  = v 
       self.azul  = b 
 
   def __str__(self): 
       return "Color"+str((self.rojo, self.verde, self.azul)) 
 
   @staticmethod 
   def blanco(): 
       return Color(255, 255, 255) 
 
   @staticmethod 
   def negro(): 
       return Color(0, 0, 0) 
 
 
c = Color.blanco() 
print(c)                # muestra (255, 255, 255) 
c = Color.negro() 
print(c)                # muestra (0, 0, 0)
