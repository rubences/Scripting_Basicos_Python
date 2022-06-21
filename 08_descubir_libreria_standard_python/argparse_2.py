import argparse 
 
def mi_programa(opciones): 
   print("Mi programa ") 
   if opciones.verbose: 
       print("Modo verboso activado ") 
   if opciones.archivo: 
       print("Tratamiento del archivo: %s " % opciones.archivo) 
 
if __name__ == '__main__': 
   ## gestión de los argumentos 
   parser = argparse.ArgumentParser() 
   parser.add_argument('-f', '--archivo', help='Nombre de archivo' ) 
   parser.add_argument('-v', '--verbose', help='Modo verboso', 
                                       action='store_true' ) 
 
   opciones = parser.parse_args() 
 
   mi_programa(opciones)
