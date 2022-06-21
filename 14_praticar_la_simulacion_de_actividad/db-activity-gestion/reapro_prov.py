## --------------------
## REAPPRO
## --------------------

# Etapa 1 : recuperación de la lista de necesidades
# Etapa 2 : para cada producto seleccionar 1 prov
# Etapa 3 : generar los comandos

from sqlalchemy import select 
 
from base import connect 
from definitions import Cliente, Producto, Proveed, Stock, PedCli, 
LinCli, LinProv 
 
import sequence as seq 
 
import datetime 
import random 
 
def get_necesidades(): 
   """ 
   Cálculo de las necesidades en pedido 
   """ 
   session = connect() 
   r = """ 
       select producto_id, sum(cped) 'cnt' 
       from LINCLI 
       where cped-centreg > 0 
       group by producto_id 
       order by producto_id 
   """ 
   lins = session.execute(r) 
   necesidad = [ x for x in lins ] 
   session.close() 
   return necesidad 
 
 
def get_cped_prov(p): 
   session = connect() 
   r = """ 
   select producto_id, sum(cped) 
   from LINPROV 
   where cped-crec > 0 
   and producto_id = %s 
   """ % p 
   lins = session.execute(r) 
   r = [ x for x in lins ] 
   session.close() 
   if r[0][1]: 
       return r[0][1] 
   else: 
       return 0 
 
def get_proveed(): 
   session = connect() 
   s = select([Proveed.id]) 
   fous = session.execute(s) 
   l = [ x[0] for x in provs] 
   session.close() 
   return random.choice(l) 
 
def get_plazo(prov): 
   session = connect() 
   s = select([Proveed]).where(Proveed.id== prov) 
   r = session.execute(s) 
   f = r.fetchone() 
   session.close() 
   return f.plazo 
 
def gnr_ped prov(necesidad): 
   session = connect() 
   for b in necesidad: 
       cpedfou = get_cped_prov(b[0]) 
       if cped prov < b[1]: 
           f = get_proveed() 
           plazo = get_plazo(f) 
           C = LinProv() 
           C.numped = seq.Next_val('COMPROV') 
           C.numlin = 1 
           C.producto_id = b[0] 
           C.prov_id = f 
           C.cped = b[1] 
           C.precio = 0 
           C.crec = 0 
           C.fprevi = datetime.datetime.now() 
           C.fprevi += datetime.timedelta(days=plazo) 
           print(" Ped %s prov =%s pro=%s cnt=%s " % 
           ( C.numped, C.prov_id, C.producto_id, C.cped )) 
           session.add(C) 
       else: 
           print("  *No hay Ped pro=%s cnt=%s cpedprov =%s" % 
            ( b[0], b[1], cpedprov)) 
 
   session.commit() 
   session.close() 
 
def run(): 
    b = get_necesidades() 
    gnr_pedprov(b) 
 
 
if __name__ == '__main__': 
   run()
