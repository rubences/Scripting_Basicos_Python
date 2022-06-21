import logging 
import mi_module 
 
def compute(): 
   logging.basicConfig(filename='test.log',  
                  filemode='w', level=logging.DEBUG) 
   logging.info('inicio de la operación') 
   mi_module.mi_funcion() 
   logging.info('Fin de la operación') 
 
if __name__ == '__main__': 
   compute()
