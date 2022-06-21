from odf.opendocument import OpenDocumentSpreadsheet 
from odf.style import ParagraphProperties, Style, 
TableColumnProperties, TextProperties 
from odf.style import TableCellProperties 
from odf.table import Table, TableCell, TableColumn, TableRow 
from odf.text import P 
 
from fake_contact import fake_contact 
 
doc= OpenDocumentSpreadsheet() 
table= Table(parent=doc.spreadsheet, name="Contactos") 
 
# Columna Nombre 
Col5 = Style(parent=doc.automaticstyles, name='Col5', 
family='table-column') 
TableColumnProperties(parent=Col5, columnwidth='5cm') 
TableColumn(parent=table, numbercolumnsrepeated=1, stylename=Col5) 
 
# Columna Fecha Nacimiento 
Col3 = Style(parent=doc.automaticstyles, name='Col3', family='table-column') 
TableColumnProperties(parent=Col3, columnwidth='3cm') 
TableColumn(parent=table, numbercolumnsrepeated=1, stylename=Col3) 
 
# Columna dirección 
Col12 = Style(parent=doc.automaticstyles, name='Col12', family='table-column') 
TableColumnProperties(parent=Col12, columnwidth='12cm') 
TableColumn(parent=table, numbercolumnsrepeated=1, stylename=Col12) 
 
# Columna teléfono 
TableColumn(parent=table, numbercolumnsrepeated=1, stylename=Col5) 
 
# Columna Comentario 
TableColumn(parent=table, numbercolumnsrepeated=1, stylename=Col12) 
 
# Definición de un estilo para el título 
TituloAzul= Style(name="TituloAzul", family="table-cell") 
TituloAzul.addElement(TextProperties(fontweight="bold", fontsize="13", 
color="#0000ff")) 
doc.automaticstyles.addElement(TituloAzul) 
 
## Definición del encabezado de columna 
EncCol= Style(name="EncCol", family="table-cell") 
EncCol.addElement(TextProperties(fontweight="bold")) 
EncCol.addElement(TableCellProperties(backgroundcolor="#AEAEAE")) 
doc.automaticstyles.addElement(EncCol) 
 
# Añadir el título 
 
tr= TableRow() 
table.addElement(tr) 
tc= TableCell(stylename="TituloAzul") 
tc.addElement(P(text="Lista de contactos")) 
tr.addElement(tc) 
 
table.addElement(TableRow()) 
 
# Añadir encabezados 
tr= TableRow() 
table.addElement(tr) 
for encabezado in ["Nombre", "Fecha de nacimiento", "Dirección", "Teléfono",  "Com-mentario"]: 
   tc= TableCell(stylename="EncCol") 
   tc.addElement(P(text=encabezado)) 
   tr.addElement(tc) 
 
for x in range(0,10): 
   tr = TableRow(parent=table) 
   c = [] 
   c = fake_contact() 
   for campo in c: 
       tc = TableCell(parent=tr) 
       p = P(parent=tc, stylename='table-column', text=campo) 
 
 
doc.save("contactos.ods")
