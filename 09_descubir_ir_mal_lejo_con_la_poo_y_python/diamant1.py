class A(): 
   def f1(self): 
       print(" A F1 ") 
 
class B( A ): 
   pass 
 
class C(): 
   def f1(self): 
       print(" C F1 ") 
 
class D( B, C): 
   pass 
 
o = D() 
o.f1() 
