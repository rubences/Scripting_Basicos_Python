from datetime import datetime 
import random 
 
class Document: 
   def __init__(self, titulo="Título del documento", autor="root" ): 
       self.titulo = titulo 
       self.autor = autor 
       self.fecha_creacion = datetime.now(). 
               strftime("%d/%m/%Y à %H: %M: %S") 
       self.contenido = None 
 
   
    ## una función para devolver el contenido en forma
    ## de caracteres independientemente de su tipo.
   def devuelve_contenido(self): 
       if self.contenido == None: 
           t = "<VACIO>" 
       elif type(self.contenido) is str: 
           t = self.contenido 
       elif type(self.contenido) is list: 
           t = "\n".join(self.contenido) 
       return t 
 
   def __str__(self): 
       t = """ 
Título: %s 
 
%s 
 
Creado el: %s par %s 
 
       """ % (self.titulo, self.devuelve_contenido(), 
self.fecha_creacion, self.autor ) 
       return t 
 
   def __repr__(self): 
       return "<Documento: %s : %d >" % (self.titulo, id(self)) 
 
if __name__ == '__main__': 
 
   D = Document('Resultado de las copias de seguridad de la semana', 'root') 
   D.contenido = [] 
   fmt_linea = "%10s %10s %10s %10s" 
   encabezado = fmt_linea % ("Date", "PROD", "EVOLUTIVO", "DEV & TEST") 
   D.contenido.append(encabezado) 
   linea = "-" * len(encabezado) 
   D.contenido.append(linea) 
 
 
   dias = [ 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes' ] 
   resultado = [ 'Ok', 'Error', '<VACIO>' ] 
 
   for n in range( 0, 5 ): 
       linea = fmt_linea % ( dias[n], random.choice(resultado), 
                random.choice(resultado), random.choice(resultado) ) 
       D.contenido.append(linea) 
   print(D)
