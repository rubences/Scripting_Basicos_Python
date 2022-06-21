##
## Factura Cliente
##

# Para todas las líneas de pedidos a entregar
# CFAC = CENTRG 
# Generación de una factura para el cliente

from sqlalchemy import select 
 
from base import connect 
from definitions import Cliente, Producto, Proveed, Stock, PedCli, 
LinCli, LinProv 
 
import sequence as seq 
 
import datetime 
import random 
 
# ------------------------------------- 
# Búsqueda de los pedidos facturables 
# ------------------------------------- 
def get_ccl_a_facturar(): 
   ccl_a_facturar = [] 
   session = connect() 
   ccl = select([PedCli]).where(PedCli.factura == 0) 
   for c in session.execute(ccl): 
       lcl = select([LinCli]).where(LinCli.numped == c.numped) 
       num_lin = num_lin_entreg = 0 
       for l in session.execute(lcl): 
           num_lin += 1 
           num_lin_entreg += (l.cped == l.centreg) 
       if num_lin == num_lin_entreg: 
           ccl_a_facturar.append(l.numped) 
   session.close() 
   return ccl_a_facturar 
 
## ---------------------------------------------- 
## Creación de una factura a partir de un pedido 
## ---------------------------------------------- 
def factura_ccl(nccl): 
   session = connect() 
   try: 
       numfac = seq.Next_val('FACTURA') 
       ccl = session.query(PedCli).filter(PedCli.numped==nccl).\ 
               update({PedCli.factura: numfac}, 
           synchronize_session=False) 
 
       lcl = session.query(LinCli).filter(LinCli.numped==nccl).\ 
               update({LinCli.cfac: LinCli.centreg}, 
            synchronize_session=False) 
       session.commit() 
   except: 
       session.rollback() 
       raise 
   finally: 
       session.close() 
   return numfac 
 
 
def run(): 
   list_ccl = get_ccl_a_facturar() 
   for c in list_ccl: 
       print("factura: %s / %s " % (c, factura_ccl(c))) 
if __name__ == '__main__': 
   run()
