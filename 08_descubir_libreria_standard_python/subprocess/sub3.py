import subprocess 
import time 
 
def do_consulta(comando, consulta): 
   cmd = subprocess.Popen(comando, stdin=subprocess.PIPE, \ 
                                    stdout=subprocess.PIPE, \ 
                                    stderr=subprocess.PIPE, \ 
                                    universal_newlines=True) 
   output, error = cmd.communicate(input=consulta) 
   if error: 
       print("STDERR: %s " % error) 
   return output 
 
 
USER="userdev"            # el usuario de la base de datos
MPD="xxxxxxxx"            # su contraseña 
SERVIDOR="localhost"       # el servidor 
DATABASE="basedev"        # la base de datos
 
## el comando "mysql" 
comando = [ 
       "mysql", 
       "--user="+USER, 
       "--password="+MPD, 
       "--host="+SERVIDOR, 
       "--database="+DATABASE 
       ] 
 
## una consulta simple 
consulta = "select count(*) from ciudades_francia_free;\n" 
r = do_consulta(comando, consulta) 
print("output:\n %s" % r) 
 
## otra consulta simple 
consulta = "select count(*) from ciudades_francia_free  
            where 
            ville_departement='01';\n" 
r = do_consulta(comando, consulta) 
print("output:\n %s" % r)
