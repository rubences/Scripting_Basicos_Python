# Ver un menú de fast food 
MENU = [ 
       [ "Hamburger", 10 ], 
       [ "CheeseBurger", 10 ], 
       [ "Patatas fritas", 3 ], 
       [ "Ketchup", 0 ] 
   ] 
 
def menu(): 
   print(" Nuestro menú: \n") 
   for plato in MENU: 
       desc = plato.pop(0) 
       precio = plato.pop(0) 
       print(" %20s: %5.2f euros" % (desc, precio)) 
 
 
if __name__ == '__main__': 
   menu()
