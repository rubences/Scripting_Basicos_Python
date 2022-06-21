from libresto import *
from libresto.resto import bouchon_lyonnais as RESTO

num_pers = clientes.llegada_clientes()
print("Llegada de %s clientes" % num_pers)
print(bienvenido.hello())
plazas.table(num_pers)

RESTO.menu()
