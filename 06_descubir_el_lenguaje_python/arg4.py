def f1( *args, **kwargs ): 
   if kwargs: 
       print("A continuación se muestra la lista de argumentos (kwargs):" ) 
       for n,(clave, valor) in enumerate(kwargs.items()): 
           print("argumento no %s: clave=%s / valor=%s" % (n, clave, valor)) 
   if args: 
       print("A continuación se muestra la lista de argumentos (args):" ) 
       for n,a in enumerate(args): 
           print("argumento no %s: %s" % (n, a)) 
 
 
print("=> Los argumentos en lista") 
f1( 1,2,3 ) 
 
print("=> Los argumentos en diccionario") 
f1( arg1=1, arg2=2, arg3=3 ) 
 
 
print("=> Los 2 al mismo tiempo") 
f1( 1,2,3, arg1=1, arg2=2, arg3=3 )
