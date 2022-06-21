import random 
 
archivo = "TEST.DAT" 
 
with open(archivo, 'w') as f: 
   for x in range(1,random.randint(1,100)): 
       fam       = random.randint(1,9) 
       fam_pro   = "F%02d" % fam 
       desc_fpro = "Familia de Productos %02d" % fam 
       cnt       = random.randint(0,100) 
       linea = "%3s:%-30s:%s\n" % (fam_pro, desc_fpro, cnt ) 
       f.write( linea )
