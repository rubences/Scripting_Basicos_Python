MENU = [ 
       [ "Ensalada nicolas", 15 ], 
       [ "Ensalada rusa", 14 ], 
       [ "Ensalada de ave", 16 ], 
       [ "Ensalada verde", 10 ], 
   ] 
 
# Visualización del menú 
def menu(): 
   print(" Nuestro menú: \n") 
   for plato in MENU: 
       desc = plato.pop(0) 
       precio = plato.pop(0) 
       print(" %30s: %5.2f euros" % (desc, precio)) 
 
 
if __name__ == '__main__': 
    menu()
