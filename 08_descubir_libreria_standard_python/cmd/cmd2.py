import cmd 
import multiprocessing as mp 
import time 
 
procesos = {}    # el almacenamiento de los procesos 
 
p_id = 0        # un Contador para la creación 
 
# Mi clase proceso 
class MiProceso(mp.Process): 
   def __init__(self, tiempo=5): 
       self.tiempo = tiempo 
       super().__init__()    # Python3 simplifica las cosas 
                             # lo que permite usar
                             # la función __init__ de la  
                             # clase madre
 
   ## La función que hay que sobrecargar 
   def run(self): 
       time.sleep(self.tiempo) 
       return 
 
# La gestion de la línea de comandos 
class Cli(cmd.Cmd): 
   def do_create(self, line): 
       global p_id 
       obj, tiempo = line.split() 
       if obj == "process": 
           p = MiProceso(int(tiempo)) 
           p_id += 1 
           procesos[str(p_id)] = p 
 
   def help_create(self): 
       s = """ 
       create process [tiempo] por defecto tiempo=5 
       """ 
       print(s) 
 
   def do_list(self, line): 
       if procesos: 
           tit = "| %10s | %20s | %10s | %10s |" % ("Proceso Nº",  "Name","Pid", "Is Alive") 
           print(tit) 
           print("-" * len(tit)) 
           for k,p in procesos.items(): 
               print( "| %10s | %20s | %10s | %10s |" % (k, p.name,  p.pid, p.is_alive() )) 
           print("-" * len(tit)) 
       else: 
           print("Nº procesos") 
 
   def do_start(self, line): 
       if line in procesos: 
           p = procesos[line] 
           print("Ejecución de: %s " % p.name) 
           p.start() 
 
   def do_join(self, line): 
       if line in procesos: 
           p = procesos[line] 
           print("Join en: %s " % p.name) 
           p.join() 
 
   def do_quit(self, line): 
       return True 
 
   def do_EOF(self, line): 
       return True 
 
if __name__ == '__main__': 
   Cli().cmdloop() 
