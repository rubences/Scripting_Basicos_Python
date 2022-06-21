# ======================== 
# Asignación de una mesa
# ======================== 
 
# Tipo de mesa
P2 = 2        # 2 plazas 
P4 = 4        # 4 plazas 
P6 = 6        # ... 
P8 = 8 
 
# Tipo de Sala 
SALA1 = 1 
TERRAZA = 9 
 
## Mesas de un diccionario simple con el número como clave y
## las características número de plazas, sala en una tupla
MESAS = { 
       1: (P2, TERRAZA), 
       2: (P2, TERRAZA), 
       3: (P4, TERRAZA), 
       4: (P4, TERRAZA), 
       5: (P6, TERRAZA), 
       6: (P8, TERRAZA), 
 
       11: (P2, SALA1), 
       12: (P2, SALA1), 
       13: (P4, SALA1), 
       14: (P4, SALA1), 
       15: (P6, SALA1), 
       16: (P8, SALA1), 
 
       } 
 
## Encontrar una mesa para n personas 
def encontrar_mesa( num_pers ): 
 
   for c, t in MESAS.items(): 
       if num_pers <= t[0]: 
           return c 
 
## ver el resultado 
def table(num_pers): 
   t = encontrar_mesa(num_pers) 
 
   if t: 
       print(" Encontrar mesa Nº %s en " % t, end='') 
       if MESAS[t][1] == TERRAZA: 
           print("en Terraza") 
       elif MESAS[t][1] == SALA1: 
           print("en la sala nº 1") 
 
if __name__ == '__main__': 
   table(2) 
