from odf.opendocument import OpenDocumentText 
from odf.style import PageLayout, PageLayoutProperties, 
MasterPage, Header, Footer 
from odf.style import Style, TextProperties 
from odf.text import H, P, Span 
from odf.table import Table, TableRow, TableCell, TableColumn 
 
from fake_contact import fake_contact 
 
from faker import Faker 
fake = Faker('es_ES') 
 
 
textdoc = OpenDocumentText() 
 
pl = PageLayout(name="pagelayout") 
pl.addElement( 
           PageLayoutProperties( 
               pagewidth="21cm", 
               pageheight="29.7cm", 
               margin="1cm", 
               marginumottom='1cm', 
               marginleft='1cm', 
               marginright='1cm', 
               margintop='1cm', 
               papertrayname='A4', 
               printorientation="portrait" 
               ) 
           ) 
textdoc.automaticstyles.addElement(pl) 
 
mp = MasterPage(name="Standard", pagelayoutname=pl) 
textdoc.masterstyles.addElement(mp) 
 
## Creación de Estilo
s = textdoc.styles 
 
## Estilo de encabezado 
h1style = Style(name="Heading 1", family="paragraph") 
h1style.addElement(TextProperties(attributes={'fontfamily':'Arial', 
'fontsize':"24pt",'fontweight':"bold" })) 
s.addElement(h1style) 
 
# Estilo de Texto 
boldstyle = Style(name="Bold", family="text") 
boldprop = TextProperties(fontweight="bold") 
boldstyle.addElement(boldprop) 
textdoc.automaticstyles.addElement(boldstyle) 
 
ItalicStyle = Style(name="Italic", family="text") 
ItalicProp = TextProperties(fontstyle="italic") 
ItalicStyle.addElement(ItalicProp) 
textdoc.automaticstyles.addElement(ItalicStyle) 
 
# Añadir texto
h=H(outlinelevel=1, stylename=h1style, text="Mi Test document ODT ") 
textdoc.text.addElement(h) 
 
p = P(text="El texto puede ser: ") 
boldpart = Span(stylename=boldstyle, text="en NEGRITA") 
p.addElement(boldpart) 
p.addText(" Pero no es obligatorio ") 
textdoc.text.addElement(p) 
 
p = P(text="Si no, también hay texto ") 
part = Span(stylename=ItalicStyle, text = "en Cursiva") 
p.addElement(part) 
textdoc.text.addElement(p) 
 
## Generación de datos 
data = [ ] 
for x in range(0,10): 
   data.append( fake_contact() ) 
 
# Tabla 
table = Table() 
 
## Añadir columnas 
for x in range(0, 4): 
   table.addElement(TableColumn()) 
 
for n,d,a,t,c in data: 
   tr = TableRow() 
   ## Nombre 
   tc = TableCell(valuetype='string') 
   tc.addElement(P(text = n )) 
   tr.addElement(tc) 
   ## Fecha de nacimiento
   tc = TableCell(valuetype='string') 
   tc.addElement(P(text = d )) 
   tr.addElement(tc) 
   ## dirección 
   tc = TableCell(valuetype='string') 
   tc.addElement(P(text = a )) 
   tr.addElement(tc) 
   ## Teléfono 
   tc = TableCell(valuetype='string') 
   tc.addElement(P(text = t )) 
   tr.addElement(tc) 
   ## dirección 
   tc = TableCell(valuetype='string') 
   tc.addElement(P(text = c )) 
   tr.addElement(tc) 
   table.addElement(tr) 
 
textdoc.text.addElement(table) 
 
textdoc.save("test_document.odt")
