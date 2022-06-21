class Singleton(object): 
  class __Singleton:     ## Subclase interna 
     def __init__(self): 
        self.val = None 
     def __str__(self): 
         return 'self: ' + self.val 
 
  instancia = None 
 
  def __new__(class__): 
     if not Singleton.instancia: 
         Singleton.instancia = Singleton.__Singleton() 
     return Singleton.instancia 
 
  def __getattr__(self, attr): 
     return getattr(self.instancia, attr) 
 
  def __setattr__(self, attr, val): 
     return setattr(self.instancia, attr, val) 
 
 
if __name__ == '__main__': 
   Una = Singleton() 
   print("Instancia Una   : %s " % id(Una)) 
   Una.val = 'Una' 
   print(" Una.val   = ", Una.val ) 
   dos = Singleton() 
   print("Instancia dos  : %s " % id(Dos)) 
   print(" Dos.val  = ", Dos.val ) 
   Dos.val = 'Dos' 
   print(" Dos.val  = ", Dos.val ) 
   Tres = Singleton() 
   print("Instancia Tres : %s " % id(Tres)) 
   print(" Tres.val = ", Tres.val ) 
   Tres.val = 'Tres' 
   print(" Tres.val = ", Tres.val ) 
   print("===============================") 
   print(" Una.val   = ", Una.val ) 
   print(" Dos.val  = ", Dos.val ) 
   print(" Tres.val = ", Tres.val )
