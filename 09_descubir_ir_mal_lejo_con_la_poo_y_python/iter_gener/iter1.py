class MiRango(): 
   def __init__(self, inicio, fin, paso=1): 
       self.estado = None 
       self.inicio = inicio 
       self.fin   = fin 
       self.paso   = paso 
 
   def __iter__(self): 
       print("función Iter ") 
       self.estado = self.inicio 
       return self 
 
   def __next__(self): 
       print("función next") 
       self.estado += self.paso 
       if self.estado > self.fin: 
       print("Stop") 
           raise StopIteration 
       return self.estado 
 
 
def test(): 
   a = MiRango(0,10,2) 
   for i in a: 
       print(i) 
 
if __name__ == '__main__': 
   test()
