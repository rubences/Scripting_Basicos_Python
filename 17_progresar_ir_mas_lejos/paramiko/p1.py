import paramiko 
 
host = '<direccion_ip o_nombre dns>' 
user = 'usuario' 
pwd  = 'contraseña' 
 
ssh_client=paramiko.SSHClient() 
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
ssh_client.connect(hostname=host,username=user,password=pwd) 
 
stdin,stdout,stderr=ssh_client.exec_command('hostname; ls -l') 
 
stdout.channel.recv_exit_status() 
 
lineas = stdout.readlineas() 
 
for linea in lineas: 
   print(linea) 
 
ssh_client.close()
