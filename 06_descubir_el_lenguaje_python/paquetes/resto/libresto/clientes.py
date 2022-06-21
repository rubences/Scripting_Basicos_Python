## 
## Clientes: Llegada de un número aleatorio de clientes 
## 
 
import random 
 
def llegada_cliente(): 
    return random.randrange(1,5) 
 
if __name__ == '__main__': 
    print("Llegada de %s cliente(s)" % llegada_cliente())
