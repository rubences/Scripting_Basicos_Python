
def f1( arg1 ): 
   arg1.append("UNO") 
   return arg1 
 
a = [1,2,3,4] 
b = f1(a[:])    # a[:] es una copia de la lista 
               # o a.copy() 
print("Después de la función a = ", a) 
print("Después de la función b = ", b)
