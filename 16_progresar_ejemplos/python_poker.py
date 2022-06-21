import random 
 
simbolo = [ "Corazones", "Picas", "Diamantes", "Tréboles" ] 
valor_carta = [ "Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve", "Nueve", "Jack", "Dama", "Rey", "As" ] 
 
Juego_52_Cartas = [ (valor, color) 
       for valor in valor_carta for color in simbolo ] 
 
escalera = [] 
 
# creación de todas las escaleras posibles 
for n in range(0,9): 
   escalera.append([ valor_carta.index(x)  
                        for x in valor_carta[n:n+5] ]) 
## Un bucle infinito 
while True: 
   mezcla = [] 
 
   paquete = list(Juego_52_Cartas) 
 
   # Mezcla de cartas 
   print("Mezcla de las cartas") 
   while paquete: 
       mezcla.append( paquete.pop( 
                        paquete.index ( 
                               random.choice(paquete) ) ) ) 
 
   # número de jugadores max(10) 
   num_jugador = 10 
   main = [] 
   for m in range(0, num_jugador): 
       main.append( [] ) 
 
   print("distribución de las cartas") 
   for c in range(0,5): 
       for m in range(0, num_jugador): 
           main[m].append(mezcla.pop()) 
 
   # Para cada jugador
   for m in range(0, num_jugador): 
       print("Jugador %s: %s " % (m, main[m]) ) 
       color = dict() 
       valor  = dict() 
       for c in main[m]: 
           ## Color 
           if c[1] in color: 
               color[c[1]] += 1 
           else: 
               color[c[1]] = 1 
           ## Valor 
           if c[0] in valor: 
               valor[c[0]] += 1 
           else: 
               valor[c[0]] = 1 
       valor_mano = sorted(valor.values()) 
       ## Pareja y dobles parejas
       p = valor_mano.count(2) 
       if p == 1: 
           print("PAREJA") 
       elif p == 2: 
           print("DOBLES PAREJAS") 
       ## Full y TRIO 
       if valor_mano.count(3) == 1: 
           if p == 1: 
               print("FULL") 
           else: 
               print("TRIO") 
       ## pOKER 
       if valor_mano.count(4) == 1: 
           print("POKER") 
 
       ## Escalera 
       v_mano = sorted([ valor_carta.index(x[0]) 
                               for x in main[m] ]) 
       print("V_MANO = %s " % v_mano) 
       if v_mano in escalera: 
           q = True 
           print("REAL") 
       ## Flush 
       f = 5 in color 
       if f: 
           print("COLOR") 
       ## Escalera + Color 
       if f and q: 
           print("ESCALERA REAL") 
       print("===============================")
