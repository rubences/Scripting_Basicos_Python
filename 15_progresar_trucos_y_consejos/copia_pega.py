## 
## Modifica el copiar pegar
## para pasar de una hoja de cálculo scalc a un wiki 
## Idea original de JC P. 
 
import clipboard 
 
## se recuperan los datos del clipboard 
data = clipboard.paste() 
 
## se tratan 
tmp = data.split('\n') 
 
encabezado = tmp.pop(0).split('\t') 
 
tmp_data = [ '^'+x for x in encabezado ]+['^'] 
 
new_data = '\t'.join(tmp_data)+'\n' 
 
for l in tmp: 
   d = l.split('\t') 
   tmp_data = [ '|'+x for x in d ]+['|'] 
   new_data += '\t'.join(tmp_data)+'\n' 
 
# volvemos a ponerlo en el clipboard 
clipboard.copy(new_data)
