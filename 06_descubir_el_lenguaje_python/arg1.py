
def f1( *args ): 
   print("Esta es la lista de argumentos:" ) 
   for n,a in enumerate(args): 
       print("argumento no %s: %s" % (n, a)) 
 
 
lista = [ 1, "dos", [ 't','r','e','s' ], 4.0 ] 
f1( *lista ) # <====  sintaxis con estrella
