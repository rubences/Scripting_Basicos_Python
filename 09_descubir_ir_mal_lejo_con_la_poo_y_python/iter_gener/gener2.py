def gener(): 
   print(" Hola, empezamos ...    : Antes del primer yield") 
   yield(" Esta parte está al inicio: 1er yield") 
   yield(" Esta al final del inicio: 2º yield") 
   yield(" Esta en la mitad: 3er yield") 
   yield(" Esta al inicio del final    : 4º yield") 
   yield(" Casi al final : 5º yield") 
   yield(" Todavía falta un poco: 6º yield") 
   print(" The End                     : no hay más yield") 
 
for i in gener(): 
   print(i)
