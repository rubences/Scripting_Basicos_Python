try: 
   raise NameError(" Mi Texto …")      # desencadenamiento 
except NameError as err: 
   print("Error de nombre: %s " % err )  # intercepción
   raise                                # propagación
