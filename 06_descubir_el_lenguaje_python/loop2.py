t1 = (1, 2, 3, 4, 5) 
t2 = ('a','b','c', 'd', 'e') 
t3 = (100, 200, 300, 400, 500) 
 
lista_de_lista = [ t1, t2, t3 ] 
 
print(" v1 |  v2 |  v3 |  v4 |  v5  " ) 
print("=============================" ) 
for v1, v2, v3, v4, v5 in lista_de_lista: 
   print( "%3s | %3s | %3s | %3s | %3s " % (v1, v2,v3,v4,v5)) 


print()

print("Num | v1  |  v2 |  v3 |  v4 |  v5  " )
print("=================================" )
for num, (v1, v2, v3, v4, v5) in enumerate(lista_de_lista):
    print( "%2s | %3s | %3s | %3s | %3s | %3s " % (num, v1, v2,v3,v4,v5))


