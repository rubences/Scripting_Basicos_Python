lista = [ 
   list(range(0,10)), 
   list(range(0,6)), 
   list(range(0,12)), 
   ] 
 
print(lista) 
 
for x,*y,z in lista: 
   print( "x=", x) 
   print( "y=", y) 
   print( "z=", z)
