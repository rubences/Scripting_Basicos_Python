from reportlab.lib import colors 
from reportlab.lib.units import mm, cm 
from reportlab.lib.pagesizes import A4, landscape 
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle 
 
Pagina_Altura, Pagina_Anchura = A4 
 
Titulo = "Una tabla con ReportLab" 
 
from faker import Faker 
import datetime 
import locale 
locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8') 
 
ts = datetime.datetime.now().strftime("%x a %X") 
 
def set_doc(): 
   doc = SimpleDocTemplate("t9.pdf",  
               pagesize=A4, 
               rightMargin=2*cm, 
               leftMargin=2*cm, 
               topMargin=2*cm,bottomMargin=2*cm) 
   return doc 
 
def set_data(): 
   fake = Faker('es_ES') 
   data = [] 
   # Encabezado 
   row = [] 
   row.append("Nº") 
   row.append("Nombre") 
   row.append("Dirección") 
   row.append("Tel + Email") 
   data.append(row) 
 
   for i in range(200): 
       row = [] 
       row.append(i+1) 
       row.append( fake.name() ) 
       row.append( fake.address() ) 
       row.append( fake.phone_number() +'\n'+ fake.ascii_email()) 
       data.append( row ) 
 
   return data 
 
## Una función común a todas las páginas 
def MisPaginas(canvas, doc): 
   canvas.saveState() 
 
   # Visualización del título 
   canvas.setFont('Times-Roman',14) 
   canvas.drawCentredString(Pagina_Altura/2, 
                         Pagina_Anchura-1*cm, Titulo) 
   canvas.drawCentredString(Pagina_Altura/2, 
                         Pagina_Anchura-1*cm, "_"*len(Titulo)) 
 
   # Visualización del número de páginas 
   canvas.setFont('Times-Roman',9) 
   canvas.drawString(1*cm, 1*cm, "Página N° %d " % doc.page) 
   canvas.drawString(15*cm, 1*cm, "Edita el %s" % ts) 
 
   canvas.restoreState() 
  
def run(): 
   doc = set_doc() 
 
   elements = [] 
      
   data = set_data() 
      
 
 
 
 
   style = TableStyle([ 
              ('BACKGROUND',(0,0),(-1,0),colors.grey), 
              ('VALIGN',(0,0),(-1,-1),'TOP'), 
              ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black), 
              ('BOX', (0,0), (-1,-1), 0.25, colors.black), 
                      ]) 
 
   t=Table(data) 
   t.setStyle(style) 
      
   #Añadir la tabla en los elementos 
   elements.append(t) 
 
   # Se construye el documento 
   doc.build(elements, onFirstPage=MisPaginas, 
                onLaterPages=MisPaginas) 
 
if __name__ == "__main__": 
   run()
