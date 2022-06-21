## -------------------- 
## Toma del pedido 
## CLIENTE 
## -------------------- 

#Etapa 1 : => import 
#Etapa 2 : Recuperación del catálogo
#Etapa 3 : Elección del cliente 
#Etapa 4 : Generación de comandos
 
from sqlalchemy import select 
 
from base import connect 
from definitions import Cliente, Producto, Stock, PedCli, LinCli 
 
import sequence as seq 
 
import datetime 
import random 
 
def get_catalog(): 
   session = connect() 
   s = select([Producto]) 
   p = [ (x.id, x.precio) for x in session.execute(s) ] 
   session.close() 
   return p 
 
def get_cliente(): 
   session = connect() 
   s = select([Cliente.id]) 
   clis = [ x.id for x in session.execute(s)] 
   session.close() 
   return random.choice(clis) 
 
def get_prods(cat): 
   max_cmd = len(cat) 
   num_pro_cmd = random.randint(0, max_cmd-1)+1 
   pros = random.sample(cat, num_pro_cmd) 
   return pros 
 
def gnr_comcli(cli, prods): 
   print("Cliente: %s " % cli ) 
   print("Número de Productos pedidos: %s " % len(prods) ) 
   print("Productos pedidos: %s " % sorted(prods) ) 
   print("Generación del pedido") 
   session = connect() 
   try: 
       numped = seq.Next_val('PEDCLI') 
       C = PedCli() 
       C.numped = numped 
       C.fecped = datetime.datetime.now() 
       C.cliente_id = cli 
       C.factura = 0 
       session.add(C) 
       print( "Pedido Nº: " , C.numped ) 
       n = 1 
       for p in prods: 
           L = LinCli() 
           L.numped = numped 
           L.numlin = n 
           L.producto_id = p[0] 
           L.cped = random.randint(1, 5000) 
           L.centreg = 0 
           L.cfac = 0 
           L.precio = p[1] 
           print("%s: %s" % (n,L)) 
           n += 1 
           session.add(L) 
       session.commit() 
   except: 
       session.rollback() 
       raise 
   finally: 
       session.close() 
 
def run(): 
   catalog = get_catalog() 
   cliente = get_cliente() 
   prods_cmd = get_prods(catalog) 
   gnr_comcli(cliente, prods_cmd) 
 
 
if __name__ == '__main__': 
   run()
