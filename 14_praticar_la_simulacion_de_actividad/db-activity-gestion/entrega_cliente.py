##
## ENTREGA CLIENTE
##


# Para todas las líneas de pedidos a entregar
#  (Por cliente/Por Producto ... )
#  - Asignar en función de la fecha de pedido
#  - y si CSTOCK - CCOM > 0
#  - decrementar el stock

from sqlalchemy import select 
 
from base import connect 
from definitions import Cliente, Producto, Proveed, Stock, PedCli, 
LinCli, LinProv 
 
import sequence as seq 
 
import datetime 
import random 
import pdb 
 
## Devuelve las líneas de pedidos a entregar
def get_bl_aenrte(): 
   session = connect() 
   r = """ 
       select numped, numlin, producto_id, cped, centreg 
       from LINCLI 
       where cped-centreg > 0 
       order by numped, numlin 
   """ 
   b = session.execute(r) 
   bls = [ (x.numped, x.numlin, x.producto_id, x.cped, x.centreg) for x in b ] 
   session.close() 
   return bls 
 
def get_stock(almacen, pro): 
   session = connect() 
   s = select([Stock]).where(Stock.producto_id==pro).\ 
                       where(Stock.almacen==almacen) 
   r = session.execute(s) 
   f = r.fetchone() 
   session.close() 
   return f.qstock 
 
def allocate(nped, nlin, almacen, prod, cnt): 
   session = connect() 
   ## inicio de la transacción 
   try: 
       ## reducción del stock de la cnt 
       stock = session.query(Stock).filter( Stock.almacen==almacen, 
                         Stock.producto_id==prod ).first() 
       ## Control de stock: aquí
       stock.qstock -= cnt 
       linc = session.query(LinCli).filter( 
                  LinCli.numped==nped, 
                  LinCli.numlin==nlin ).first() 
       linc.centreg += cnt 
       ## actualización del pedido 
       session.add(linc) 
       session.add(stock) 
       session.commit() 
   except: 
       session.rollback() 
       raise 
   finally: 
       session.close() 
 
 
def run(): 
   ALMACEN = 'D1' 
   ## Para todas las líneas de pedidos a entregar
   b = get_bl_aenrte() 
   for l in b: 
       print(" Trato: ", l) 
       nped, nlin, prod, cped, centreg = l 
       ## Se recupera el stock 
       s = get_stock(ALMACEN, prod) 
       print("Stock Pro Almacén %s: %s = %s " % (ALMACEN, prod, s)) 
       if s >= (cped-centreg): 
           print("Asignación %s %s %s %s " % (nped, 
                                                  nlin,      
                                                  prod, 
                                                  cped-centreg)) 
           allocate( nped, nlin, ALMACEN, prod, cped-centreg ) 
 
if __name__ == '__main__': 
   run()
