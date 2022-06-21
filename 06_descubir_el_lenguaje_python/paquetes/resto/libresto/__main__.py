from libresto import * 
 
## pequeña función para mostrar las opciones e indicar 1 
def opcion_resto(): 
   print(""" 
   1 - Fast Food 
   2 - Ensalada Bar 
   3 - Bouchon Lyonnais 
 
   """) 
   r = input("Su opción: ") 
   return r 
 
r = int(opcion_resto()) 
 
if r == 1: 
   from libresto.resto import fast_food as RESTO 
elif r == 2: 
   from libresto.resto import salade_bar as RESTO 
else: 
   from libresto.resto import bouchon_lyonnais as RESTO 
 
num_pers = clientes.llegada_clientes() 
print("Llegada de %s clientes" % num_pers) 
print(bienvenido.hello()) 
plazas.mesa(num_pers) 
 
RESTO.menu()
