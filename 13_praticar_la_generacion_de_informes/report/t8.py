from reportlab.lib import colors 
from reportlab.lib.units import mm, cm 
from reportlab.lib.pagesizes import A4, landscape 
from reportlab.platypus import SimpleDocTemplate 
from reportlab.platypus import Table, TableStyle 
 
import leer_csv 
 
## Definición del documento 
def set_doc(): 
   doc = SimpleDocTemplate("t8.pdf", 
                   pagesize=A4, 
                   rightMargin=2*cm, 
                   leftMargin=2*cm,  
                   topMargin=2*cm, 
                   bottomMargin=2*cm 
               ) 
   # para el formato paisaje 
   # doc.pagesize = landscape(A4) 
   return doc 
 
## Lectura de los datos 
def set_data(): 
   data = leer_csv.leer_csv('data.csv') 
   return data 
 
## Bucle principal 
def run(): 
   doc = set_doc() 
 
   elements = [] 
      
   data = set_data() 
      
   style = TableStyle([ 
              ('BACKGROUND',(0,0),(-1,0),colors.grey), 
              ('ALIGN',(0,0),(0,-1),'CENTER'), 
              ('ALIGN',(1,0),(1,-1),'CENTER'), 
              ('ALIGN',(3,0),(3,-1),'RIGHT'), 
              ('ALIGN',(4,0),(4,-1),'RIGHT'), 
              ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black), 
              ('BOX', (0,0), (-1,-1), 0.25, colors.black), 
                      ]) 
 
   t=Table(data, colWidths=[15*mm, 15*mm, 90*mm, 20*mm,20*mm]) 
   t.setStyle(style) 
      
   #Añadir la tabla en los elementos 
   elements.append(t) 
 
   ## Se construye el documento, lo que genera el archivo 
   doc.build(elements) 
 
if __name__ == "__main__": 
   run()
