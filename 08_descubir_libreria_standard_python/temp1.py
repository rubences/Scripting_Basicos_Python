import tempfile 
 
data = [ 'línea 1\n', 'línea 2\n', 'línea 3\n' ] 
 
with tempfile.TemporaryFile(mode='w+') as fic: 
   fic.writelines( data )                     # escritura 
   fic.flush()                                # forzada 
   fic.seek(0)                                # rewind 
   print(fic.read())                          # lectura
