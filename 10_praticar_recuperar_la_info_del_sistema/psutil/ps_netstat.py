import psutil 
import socket 
 
def resolve(ip): 
   try: 
       data = socket.gethostbyaddr(ip) 
       host = data[0] 
   except: 
       host = '' 
   return host 
 
## Recuperación de los números de proceso
## así como el nombre del ejecutable 
proc_names={} 
for p in psutil.process_iter(attrs=['pid', 'name']): 
   proc_names[p.info['pid']] = p.info['name'] 
 
## Listamos las conexiones actuales
fmt = "{:25s}|{:25s}| {:20s}|{:15s}|{:s}" 
titulo = fmt.format('Local', 'Distante',  
           'status', 'Process', 'Host' ) 
print(titulo) 
print('=' * len(titulo)) 
for c in psutil.net_connections(kind='inet4'): 
   l = "%15s: %s" % (c.laddr[0], c.laddr[1]) 
   if c.raddr: 
       r = "%15s: %s" % (c.raddr[0], c.raddr[1]) 
       host = resolve(c.raddr[0]) 
   else: 
       r = "" 
       host = "" 
   s = c.status 
   p = proc_names.get(c.pid, "") 
   print(fmt.format(  l, r, s, p, host ))
