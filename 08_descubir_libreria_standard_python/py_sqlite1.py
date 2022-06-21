import sqlite3 
 
db = sqlite3.connect(':memory:') 
 
c = db.cursor() 
 
c.execute('create table contacto( id integer, nombre varchar(30), 
tel varchar(30), fecnac date) ') 
 
c.execute(' insert into contacto values (1, "linux Torvalds", 
"06 01 02 03 04", "28-12-1969") ') 
 
db.commit() 
 
for row in c.execute('select * from contacto'): 
   print(row) 
 
db.close() 
