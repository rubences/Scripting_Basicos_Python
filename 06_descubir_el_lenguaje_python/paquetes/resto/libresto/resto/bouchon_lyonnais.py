ENTRADA = [ 
         "Como opción: ", 
         "\tEnsalada rusa", 
         "\tEnsalada de ave", 
         "\tEnsalada de verde", 
   ] 
PLATO = [ 
            " Como opción: ", 
            "\tRabo de toro", 
            "\tMerluza", 
            "\tSolomillo", 
            "\tSalmón", 
       ] 
VERDURAS = [ 
            "Como opción: ", 
            "\tBerenjenas gratinadas", 
            "\tParrillada de verduras", 
            "\tBoletus" 
       ] 
POSTRE = [ 
            "Como opción Queso o Postre", 
            "\tPastel de manzana", 
            "\tCrema tostada" 
       ] 
 
# Visualización del menú 
def menu(): 
   print(" Nuestro menú  a 18 euros: \n") 
 
   print("\n Para comenzar le ofrecemos: \n") 
   for plato in ENTRADA: 
       print( " %s " % plato) 
 
   print("\n Para continuar: \n") 
   for plato in PLATO: 
       print( " %s " % plato) 
 
   print("\n Acompañado de : \n") 
   for plato in VERDURAS: 
       print( " %s " % plato) 
 
   print("\n Y para terminar...\n") 
   for plato in POSTRE: 
       print( " %s " % plato) 
 
if __name__ == '__main__': 
   menu()
