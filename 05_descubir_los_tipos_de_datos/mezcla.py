import random   # importamos el módulo random 
                # para la generación de número aleatorios
 
## Crea un paquetee de 32 cartas
## una lista de 32 enteros del 1 al 32
paquete = [x for x in range(1, 32)] 
 
mezcla = []         # al inicio el resultado está vacío
 
 
print(paquete)        # mostramos al menos el paquete ordenado 
 
while paquete:                               # mientras que quede 
   mezcla.append(                            # añadimos
           paquete.pop(                      # lo que eliminamos 
               paquete.index(                # a este índice 
                   random.choice(paquete)    # elegido al azar 
                   )                         #    en la lista 
               ) 
           ) 
 
print(mezcla)      # Mostramos el resultado mezclado
