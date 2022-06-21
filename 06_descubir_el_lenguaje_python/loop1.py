
print(" Bucle con break ")
for x in range(0,10):
    print(x)
    if x == 5:
        break

print(" Bucle con continue ") 
for x in range(0,10): 
    if x == 5: 
       print(" Aquí continua") 
       continue  
    print(x)         #esta línea no se ejecuta si x vale 5 
