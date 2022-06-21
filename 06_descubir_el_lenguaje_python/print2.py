bases = [ "Dec", "Hex", "Byt", "Bin" ] 
fmt_titulo = "|{d[0]:^5s}|{d[1]:^5s}|{d[2]:^5s}|{d[3]:^5s}|" 
titulo = fmt_titulo.format( d=bases ) 
 
print('-' * len(titulo)) 
print(titulo) 
print('-' * len(titulo)) 
 
for num in range(0,16): 
   print("|", end='') 
   for base in 'dXob': 
       print('{0:5{base}}'.format(num, base=base), end='|') 
   print() 
 
print('-' * len(titulo))
