def MiRango(inicio, fin, paso=1): 
   i = inicio 
   while i < fin: 
       i += paso 
       yield i 
 
 
def test(): 
   for i in MiRango(0,10): 
       print(i) 
 
if __name__ == '__main__': 
   test()
