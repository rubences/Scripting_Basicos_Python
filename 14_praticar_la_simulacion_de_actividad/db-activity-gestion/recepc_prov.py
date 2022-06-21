## -------------------------
## Recepción Proveedor
## -------------------------

# Para todos los pedidos a recepcionar
# - Se recepciona la Cantidad (CREC)
# - Se incrementa el STOCK

from sqlalchemy import select 
 
from base import connect 
from definitions import Cliente, Producto, Proveed, Stock, PedCli, 
LinCli, LinProv 
 
import sequence as seq 
 
import datetime 
import random 
 
def get_cprov_ar(fecha_actual): 
   session = connect() 
   r = select([LinProv]).\ 
       where(LinProv.cped-LinProv.crec > 0).\ 
       where(LinProv.fprevi <= fecha_actual) 
   cprovar = session.execute(r).fetchall() 
   c = [ x for x in cprovar] 
   session.close() 
   return cprovar 
 
def reception( nprev, nlin, pro, cnt, almacen): 
   session = connect() 
   try: 
        stock = session.query(Stock).\ 
       filter( Stock.almacen==almacen, 
            Stock.producto_id==pro ).first() 
        stock.qstock += cnt 
        linprov = session.query(LinProv).\ 
       filter( LinProv.numped == nprev,  
           LinProv.numlin == nlin).first() 
        linprov.crec += cnt 
        session.add(stock) 
        session.add(linprov) 
        session.commit() 
   except: 
       session.rollback() 
       raise 
   finally: 
       session.close() 
 
def run(): 
   ALMACEN = 'D1' # almacén por defecto 
   fdia = datetime.datetime.now() 
   ped = get_cprov_ar(fdia) 
   for c in ped: 
       reception( c.numped, c.numlin, 
           c.producto_id, c.cped, ALMACEN) 
       print(" Ped a rec:  %s %s | pro=%s | cnt=%s | date=%s " 
       % (c.numped, c.numlin, 
           c.producto_id, c.cped, c.fprevi)) 
 
if __name__ == '__main__': 
   run()
