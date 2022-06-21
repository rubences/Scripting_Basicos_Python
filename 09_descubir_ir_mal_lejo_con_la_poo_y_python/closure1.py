## Fábrica de función 
def func1(): 
   def s_func1(): 
       print(" S_func1 ") 
   return s_func1 
 
## Recupeamos una función 
f = func1() 
 
## La utilizamos 
f() 
f()
