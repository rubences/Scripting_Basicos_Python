class Humano(): 
   class Cerebro (): 
       def do(self): 
           return "Pienso" 
   class Estomago (): 
       def do(self): 
           return "Digiero" 
   class Piernas(): 
       def do(self): 
           return "Andan" 
   class Mano(): 
       def do(self): 
           return "Hacen cosas" 
 
   def __init__(self): 
       self.organos = { 
               'cerebro': ( self.Cerebro (), ), 
               'Estomago': ( self.Estomago(), ), 
               'Piernas': (self.Pierna(), self. Pierna()), 
               'Manos': (self.Mano(), self.Mano()) 
               } 
 
   def do(self): 
       for k,v in self.organos.items(): 
           print( "%-15s" % k) 
           for m in v: 
               print( "%20s" % m.do() ) 
 
if __name__ in '__main__': 
   H = Humano() 
   H.do()
