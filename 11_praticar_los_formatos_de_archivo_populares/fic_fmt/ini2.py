import configparser as cp 
 
config = cp.ConfigParser() 
 
data_default = { 
           "default_user": "demo", 
           "default_password": "demo", 
           "server":"localhost", 
           "port":27017 
       } 
 
config['DEFAULT'] = data_default 
 
data_cap1 = { 
       "multi lineas": """ 
        Podemos almacenar múltiples líneas  
      en los archivos .ini 
        lo que es muy práctico 
       """ 
       } 
 
config['Capítulo 1'] = data_chap1 
 
with open('test2.ini', 'w') as config_file: 
   config.write(config_file)
