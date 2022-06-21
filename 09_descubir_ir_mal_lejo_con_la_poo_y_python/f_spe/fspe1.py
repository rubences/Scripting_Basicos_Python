class A(object): 
 
   def __init__(self): 
       self.ingredients = [] 
       self.status = None 
 
   def __getattribute__(self, attr): 
       __dict__ = object.__getattribute__(self, '__dict__') 
       if attr in __dict__: 
           return object.__getattribute__(self, attr) 
       else: 
           if attr == 'nombre': 
               if self.status: 
                   s = self.status 
               else: 
                   s = "Sopa" 
               if len(self.ingredients) > 1: 
                   s += " de " 
                   s += " ,".join(self.ingredients[:-1]) 
                   s += " y de "+self.ingredients[-1] 
               elif len(self.ingredients) == 1: 
                   s += " de "+self.ingredients[0] 
               return s 
 
 
if __name__ == '__main__': 
   sopa = A() 
   sopa.ingredients.append("Calabaza") 
   sopa.ingredients.append("Zanahoria") 
   sopa.ingredients.append("Patata") 
   sopa.status = "Batido" 
   print(sopa.nombre) 
 
   sopa = A() 
   sopa.ingredients.append("Zanahoria") 
   sopa.ingredients.append("Calabaza") 
   sopa.status = "Consomé" 
   print(sopa.nombre) 
 
   sopa = A() 
   sopa.ingredients.append("Zanahoria") 
   print(sopa.nombre)
