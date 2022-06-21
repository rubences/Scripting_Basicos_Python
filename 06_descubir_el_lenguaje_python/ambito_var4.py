
def funcion(): 
   global a        # 'a' se hace accesible en  modo lectura/escritura 
   a = 12 
   print(" La variable en la función a = {}".format(a) ) 
 
 
a = 5 
funcion() 
print(" La variable a = {}".format(a) ) 
a="DOS" 
funcion() 
print(" La variable a = {}".format(a) )
