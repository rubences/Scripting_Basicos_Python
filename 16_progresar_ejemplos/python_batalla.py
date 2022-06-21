import random 
 
simbolo = [ "Corazones", "Picas", "Diamantes", "Tréboles" ] 
valor_carta = [ "Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve", "Nueve", "Jack", "Dama", "Rey", "As" ] 
 
Juego_52_Cartas = [ (valor, color) for valor in valor_carta for 
color in simbolo ] 
 
mezcla = [] 
 
paquete = list(Juego_52_Cartas) 
 
print("Mezcla de las cartas") 
while paquete: 
   mezcla.append( paquete.pop( 
               paquete.index( 
                     random.choice(paquete) 
                           ) 
                     ) 
                ) 
 
print("Distribución") 
j1 = [] 
j2 = [] 
while mezcla: 
   j1.append( mezcla.pop() ) 
   j2.append( mezcla.pop() ) 
 
tmp = [] 
 
## El juego de la batalla 
while j1 and j2: 
   c1 = j1.pop(0) 
   c2 = j2.pop(0) 
   v_c1 = valor_carta.index( c1[0] ) 
   v_c2 = valor_carta.index( c2[0] ) 
   print( "j1 %25s / j2 %25s = " % (c1, c2), end='') 
   if v_c1 > v_c2: 
       print("J1 Gana ", end='') 
       j1.extend( [c1, c2] ) 
       if tmp: 
           j1.extend( tmp ) 
           tmp = [] 
   elif v_c1 < v_c2: 
       print("J2 Gana ", end='') 
       j2.extend( [c1, c2] ) 
       if tmp: 
           j2.extend( tmp ) 
           tmp = [] 
   else: 
       print("BATALLA ", end='') 
       tmp = [c1, c2, j1.pop(0), j2.pop(0)] 
       print(tmp, end='') 
   print(" Paquetes: %02d / %02d " % ( len(j1), len(j2) )) 
 
 
## FIN DE LA PARTIDA 
if j1: 
   print(" J1 GANA LA PARTIDA") 
if j2: 
   print(" J2 GANA LA PARTIDA")
