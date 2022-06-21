import string 
archivo = "/usr/share/games/fortunes/fortunes" 
 
Palabras = {} 
 
with open(archivo) as f: 
   lineas=f.readlines() 
   for l in lineas: 
       for c in string.punctuation: 
           if c in l: 
               l = l.replace(c, ' ') 
       for m in l.split(): 
           palabra = m.lower() 
           if palabra in Palabras: 
               Palabras[palabra] += 1 
           else: 
               Palabras[palabra] = 1 
 
for clave, valor in Palabras.items(): 
   print(" Hay %s %s en el texto" % (valor, clave))
