from  pyexcel import get_records 
 
records = get_records(file_name="contactos.ods") 
 
 
fmt = "|{NOM:30s} | {FECHA_NAC:10s} | {TEL:20s} |" 
 
for record in records: 
    print( fmt.format( **record ))
