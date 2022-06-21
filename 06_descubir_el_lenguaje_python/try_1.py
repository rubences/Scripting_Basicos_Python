
OK = False 
 
while not OK: 
   try: 
       n = int(input("Escriba un número: ")) 
       OK = True 
   except TypeError, ValueError: 
       print(" Error de tipo ... ") 
   else: 
       print("Cláusula Else") 
   finally: 
       print("Clásula Finally") 
 
print("Salida del bucle")
