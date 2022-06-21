## -------------------------- 
## Recuperación de los archivos 
## -------------------------- 
 
import os 
import time 
import ftplib 
 
HOST="host.distant.es" 
LOGIN="login_distant" 
PASSE="contraseña_secreta" 
 
DEST_DIR="data/ftp_in" 
REP_DATA="data" 
 
## -------------------------------- 
# En primer lugar cambiamos el directorio 
## -------------------------------- 
print( "Inicio: %s " % time.asctime()) 
print( "Cambio de directorio: %s " % DEST_DIR) 
os.chdir(DEST_DIR) 
 
print( "Conexión: %s %s/%s " % ( HOST, LOGIN, PASSE )) 
rl = ftplib.FTP(HOST) 
rl.login(LOGIN, PASSE) 
 
print( "Cambio de directorio: %s " % REP_DATA) 
rl.cwd(REP_DATA) 
 
print( "Lista de los archivos") 
lista=[] 
rl.dir(lista.append)   ## ver explicaciones 
 
archivos=[] 
 
## solo los archivos terminan por dat 
for l in lista: 
   if l.endswith('dat'): 
       archivos.append(l.split()[-1]) 
 
print( "transferencia de los archivos ") 
for f in archivos: 
   print( "    Recup de %s " % f) 
   with open( f , "wb") as fp: 
       rl.retrbinary("RETR %s" % f, fp.write) 
 
print( "Fin de la conexión") 
rl.quit() 
print( "Fin  : %s " % time.asctime())
