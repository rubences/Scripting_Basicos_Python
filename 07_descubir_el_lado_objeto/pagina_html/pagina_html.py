import Documento # Debo importar el módulo Documento 
 
## La clase PaginaHtml con Documento.Document (módulo.clase) 
## como clase madre 
 
class PaginaHtml(Documento.Document): 
   def __init__(self, titulo="Page HTML"): 
       super().__init__(titulo)  ## __init__ de la clase madre
       self.contenido = []        ## fuerzo contenido en lista vacia 
 
   def head(self): 
       return """ 
           <head> 
               <title> %s </title> 
           </head>\n 
           """ % self.titulo 
 
   def body(self): 
       return """ 
           <body> 
           %s 
           </body>\n 
           """ % self.devuelve_contenido() 
 
   def footer(self): 
       return """ 
           <footer> Creado por %s el %s </footer>\n 
           """ % ( self.autor, self.fecha_creacion) 
 
   def __str__(self): 
       t = """ 
           <html> 
           %s 
           %s 
           %s 
           </html> 
       """ %  ( self.head(), self.body(), self.footer() ) 
       return t 
 
   def __repr__(self): 
       return "<PaginaHtml: %s : %d >" % (self.titulo, id(self)) 
 
if __name__ == "__main__": 
   P = PaginaHtml() 
   P.titulo = "Page HTML" 
   P.contenido.append( " <p> Hola mundo</p>" ) 
   print(P)
