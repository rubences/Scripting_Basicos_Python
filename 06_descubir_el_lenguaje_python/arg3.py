def f1( **kwargs ): 
   print("A continuación se muestra la lista de argumentos:" ) 
   for n,(clave, valor) in enumerate(kwargs.items()): 
       print("argumento no %s: clave=%s / valor=%s" % (n, clave, valor)) 
 
dico = { 
        "arg1": 1, 
        "arg2": "dos", 
        "arg3": [ 'tres' ], 
        "arg4": 4.0 
       } 
 
f1(**dico)
