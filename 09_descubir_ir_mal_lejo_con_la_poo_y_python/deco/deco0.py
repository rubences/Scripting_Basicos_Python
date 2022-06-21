def mi_deco(función): 
   return función 
 
@mi_deco 
def funcion1(): 
    print("Soy la función 1 ") 
 
@mi_deco 
def funcion2(): 
    print("Soy la función 2 ") 
 
@mi_deco 
def funcion3(): 
    print("Soy la función 3 ") 
 
## Llamada a las funciones 
funcion1() 
funcion2() 
funcion3() 
funcion1()
