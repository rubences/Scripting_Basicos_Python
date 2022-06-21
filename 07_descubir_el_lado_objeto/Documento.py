class Document: 
   def __init__(self): 
       self.titulo = "" 
       self.autor = "" 
       self.fecha_de_actualizacion = "" 
       self.contenido =  "" 
 
   def __str__(self):                # comportamiento para iprint 
       tmp = """ 
       Documento: %s 
       Creado por: %s 
 
       %s 
 
       """ % (self. titulo, self.autor , self.contenido) 
       return tmp 
 
if __name__ == '__main__': 
   A = Document() 
   A.titulo = "Mi primer objeto" 
   A.autor = "Chris" 
   A.contenido = "Este es un ejemplo de clase simple" 
   print(A)
