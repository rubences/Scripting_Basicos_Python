## -------------------------
## Librería de secuencias
## -------------------------
## -------------------------------------
## No es super eficaz pero es portable
## -------------------------------------

## ------------------------- 
## Librería de las secuencias 
## ------------------------- 
 
from sqlalchemy import create_engine, select 
from sqlalchemy.orm import sessionmaker 
 
from base import connect 
from definitions import Contador 
 
def cr_Contador(nombre): 
   session = connect() 
   c = Contador() 
   c.nombre = nombre 
   c.val = 1 
   session.add(c) 
   session.commit() 
   session.close() 
 
def Curr_val(nombre): 
   session = connect() 
   s = select([Contador]).where(Contador.nombre==nombre) 
   r = session.execute(s) 
   cpt = r.fetchone() 
   session.close() 
   return cpt.val 
 
def Next_val(nombre): 
   session = connect() 
   cpt = session.query(Contador).filter_by(nombre=nombre).first() 
   cpt.val += 1 
   r = cpt.val 
   session.add(cpt) 
   session.commit() 
   session.close() 
   return r 
 
 
def run(): 
   ## Creación de un contador TEST 
   cpt = 'TEST' 
   try: 
       cr_Contador(cpt) 
   except: 
       pass 
   ## Valor actual
   print( "Valor actual: %s = %s" % (cpt, Curr_val(cpt))) 
   ## next_val 
   print( "Valor Siguiente: %s = %s" % (cpt, Next_val(cpt))) 
   ## Valor Actualde 
   print( "Valor actual: %s = %s" % (cpt, Curr_val(cpt))) 
 
 
if __name__ == '__main__': 
   run()
