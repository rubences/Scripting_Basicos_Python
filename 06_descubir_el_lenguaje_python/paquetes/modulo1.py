def mi_funcion(apellido): 
   return "Hola desde mi módulo: {}".format(apellido) 
 
if __name__ == '__main__': 
   ## Test local 
   print( mi_funcion(" TOTO ") ) 
