import random 
 
numero_al_azar = random.randint(1,5) 
ENCONTRADO = False 
numero_intento = 0 
 
while not ENCONTRADO: 
 
   intento = input("Escriba un número de 1 a 5: ") 
 
   if int(intento) == numero_al_azar: 
       ENCONTRARO = True 
   else: 
       print("\n Lo siento... \n") 
 
   numero_intento += 1 
 
print("\n Bravo lo ha encontrado en %s intento(s)" % numero_intento )
