from datetime import datetime 
 
class Document: 
   def __init__(self, titulo="Título del documento", autor="Lui" ): 
       self.titulo = titulo 
       self.autor = autor 
       self.fecha_creacion = datetime.now(). 
                        strftime("%d/%m/%Y à %H: %M: %S") 
       self.contenido = None 
 
   def __str__(self): 
       t = """ 
Título: %s 
 
%s 
 
Creado el: %s par %s 
 
       """ % (self.titulo, self.contenido,  
                        self.fecha_creacion, self.autor ) 
       return t 
 
   def __repr__(self): 
       return "<Documento: %s : %d >" % (self.titulo, id(self)) 
 
if __name__ == '__main__': 
   D = Document( "Título", "Mí") 
   D.contenido = """ 
Hola, 
soy el contenido de este documento 
y debo ser imprimido como tal 
   """ 
   print(D) 
