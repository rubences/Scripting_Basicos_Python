from odf.opendocument import OpenDocumentSpreadsheet 
from odf.table import Table, TableCell, TableRow 
from odf.text import P 
 
from fake_contact import fake_contact 
 
textdoc = OpenDocumentSpreadsheet() 
 
table = Table(parent=textdoc.spreadsheet, name="Contactos") 
 
for x in range(0,10): 
    tr = TableRow(parent=table) 
    c = [] 
    c = fake_contact() 
    for campo in c: 
        tc = TableCell(parent=tr) 
        p = P(parent=tc, text=campo) 
 
textdoc.save("contactos.ods")
