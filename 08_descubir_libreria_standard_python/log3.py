import logging 
import mi_module 
 
def compute(): 
   logging.basicConfig(format='%(asctime)s %(message)s', 
             datefmt='%d-%m-%Y %H:%M:%S', level=logging.DEBUG) 
   logging.info('inicio de la operación') 
   mi_module.mi_funcion() 
   logging.info('Fin de la operación') 
 
if __name__ == '__main__': 
   compute()
