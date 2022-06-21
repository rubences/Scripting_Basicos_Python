import pyexcel as pe 
from fake_contact import fake_contact 
 
 
Hoja = [ "INVITADOS", "FAMILIA", "VIP" ] 
 
data = {} 
 
encabezado = [ "NOMBRE", "FECHA_NAC", "DIRECCION", "TEL", "COMENT" ] 
 
for H in Hoja: 
   pagina = [] 
   pagina.append( encabezado ) 
   for x in range(0, 5): 
       n,d,a,t,c = fake_contact() 
       page.append( [n, d.strftime('%Y-%m-%d'), a, t, c ] ) 
   data[H] = pagina 
 
pe.save_book_as(bookdict=data, dest_file_name="LISTA_INVITADOS.ods")
