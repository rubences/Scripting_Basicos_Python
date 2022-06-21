import telnetlib 
 
HOST = "localhost" 
PORT=2601 
user = 'zebra'    # la conexión solo pide una 
password = ''     # contraseña 
 
tn = telnetlib.Telnet(HOST,PORT)               #conexión 
 
tn.read_until(b"Password: ")               # espera prompt 
tn.write(user.encode('ascii') + b"\n")     # envío password 
 
tn.write(b"enable\n")                      # envío comando 
tn.read_until(b"Password: ")               # esperar prompt 
tn.write(user.encode('ascii') + b"\n")     # envío password 
tn.write(b"show startup-config\n")         # envío comando 
tn.write(b"quit\n")                        # envío comando 
 
print(tn.read_all().decode('ascii'))       # recupera al info
