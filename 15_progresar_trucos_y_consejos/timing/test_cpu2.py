from timing import timing 
 
num_multiples = 50_000_000 
data = range(num_multiples) 
number = 1 
 
with timing(label="Estresamos las cpus") as t: 
   for i in data: 
       number *= 1.0000001 
 
with timing(label=" Estresamos las cpus") as t: 
   for i in data: 
       number *= 1.0000001 
       if not i % 10_000_000 and i>0: 
           t.tps_intermedio(" %s " % i)
