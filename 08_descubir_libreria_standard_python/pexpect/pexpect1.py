import pexpect 
servidor = "speedtest.tele2.net" 
username = "anonymous" 
password = "root@ejemplo.com" 
 
child = pexpect.spawn ('ftp %s' % servidor)# ejecución del binario 
child.expect ('Name .*: ')                  # espera 
child.sendline (username)                   # envía 
child.expect ('Password:')                  # espera 
child.sendline (password)                   # envía 
child.expect ('ftp> ')                      # etc ... 
child.sendline ('ls -l') 
child.expect ('ftp> ') 
print(child.before)   # Muestra el resultado 
child.sendline ('sale') 


