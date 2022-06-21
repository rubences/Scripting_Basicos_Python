import time 
 
inicio = time.time() 
 
num_mul = 50_000_000     #alrededor de 15s 
data = range(num_mul) 
numero = 1 
 
for i in data: 
   numero *= 1.0000001 
 
fin = time.time() 
 
print("Resultado = {}".format(numero)) 
print("Tiempo = {}".format(fin – inicio))
