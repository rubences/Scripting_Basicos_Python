import multiprocessing 
 
class MiProceso(multiprocessing.Process): 
 
   def run(self): 
       print('Soy el %s' % self.name) 
       return 
 
if __name__ == '__main__': 
   PROC = [] 
   for i in range(5): 
       p = MiProceso() 
       PROC.append(p) 
       p.start() 
 
   for p in PROC: 
       p.join()
