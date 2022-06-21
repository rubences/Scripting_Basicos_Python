## ---------------------------- 
## Generación de una tabla en pug 
## ---------------------------- 
 
TAB="\t" 
 
def encabezado(): 
   print('table(class="table table-over")') 
 
def read_data(): 
   data = [ 
        [ 'Descripción', 'Enlace' ], 
        [ 'Entorno de Producción', 'http://prod', "PROD" ], 
        [ 'Entorno de Pre-producción', 'http://preprod', "PREPROD" ], 
        [ 'Entorno de Test', 'http://test', "TEST & DES" ], 
           ] 
   return data 
 
def thead( label ): 
   print(TAB+'thead(class="thead-light")') 
   print(TAB*2+'tr') 
   for l in libel: 
       print(TAB*3+"th %s" % l) 
 
def tbody( data ): 
   print(TAB+"tbody") 
   for desc, enlace, l_boton in data: 
       print(TAB+"tr") 
       print(TAB*2+"td %s " % desc) 
       print(TAB*2+"td") 
       print(TAB*3+'a(class="btn btn-info" href="%s") %s' 
                % (lien, l_boton)) 
 
def main(): 
   encabezado() 
   data = read_data() 
   headers = data.pop(0) 
   thead( headers ) 
   tbody( data ) 
 
if __name__ == '__main__': 
   main()
