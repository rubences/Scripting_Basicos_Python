## Una clase de base 
class BASE(object): 
   def quien_soy(self): 
       return type(self) 
 
## Las clases 
class A(BASE): 
   pass 
 
class B(BASE): 
   pass 
 
class C(BASE): 
   pass 
 
class D(BASE): 
   pass 
 
## La fábrica del objeto 
def FABRICA(C): 
   if C == 'A': 
       return A() 
   elif C == 'B': 
       return B() 
   elif C == 'C': 
       return C() 
   elif C == 'D': 
       return D() 
   else: 
       return None 
 
o1 = FABRICA('B') 
print(o1.quien_soy()) 
 
o2 = FABRICA('D') 
print(o2.quien_soy())
