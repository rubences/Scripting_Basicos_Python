from pyexcel_ods import get_data 
import random 
from faker import Faker 
 
MATERIAL = [ 
        "MADERA", 
        "PAPEL", 
        "CARTÓN", 
        "METAL", 
        "PIEDRA", 
        "MATERIA VEGETAL", 
        "PLÁSTICO", 
       ] 
 
ADJETIVO = [
     "LÁSER",
     "SONICO",
     "SILENCIOSO",
     "SUAVE",
     "DIFÍCIL",
     "BLANDO",
     "FLEXIBLE",
     "MALEABLE",
     "GAMER",
     "PRO",
     "ESTIRABLE",
     "DESLIZANTE",
     "ELÉCTRICO",
]
 
OTROS = [
     "PINTAR",
     "BRUTO",
     "PINTADO",
     "BARNIZ",
     "SATÍN",
     "BRILLANTE",
]
 
DECORACIONES = {}
MUEBLES = {}
HIGH_TECH = {}
PLATOS = {}
SERVICIOS = {}
HERRAMIENTAS = {}
CABLES = {}
 
 
PRODUCTOS = {
     "DECORACIONES": DECORACIONES,
     "MUEBLES": MUEBLES,
     "HIGH_TECH": HIGH_TECH,
     "PLATO": PLATO,
     "SERVICIOS": SERVICIOS,
    "HERRAMIENTAS": HERRAMIENTAS,
    "CABLES": CABLES,
}
 
PC_ADJECTIVE = 30
COLOR_PC = 70
PC_OTHER = 80 
fake = Faker('es_ES') 
 
## -------------------------------------- 
## La clase descripción 
## permite determinar los argumentos
## de generación aleatoria
## -------------------------------------- 
class Description(): 
   def __init__( self, dim, del peso, pu, dia,  
                  diu, coulor, material, precio, adj, otros ): 
       self.dimension = dim 
       self.du = del 
       self.diametro = dia 
       self.diu = diu 
       self.pesos = pesos 
       self.pu = pu 
       self.color = color 
       self.material = material 
       self.catprecio = precio 
       self.adjetivo = adj 
       self.otros = otros 
 
   def __str__(self): 
       r = "" 
       if self.dimension: 
           r += self.dimension 
       return r 
 
## ---------------------------------- 
## La clase Fake Producto contiene
## los datos básicos para generar
## un producto aleatorio
## ---------------------------------- 
class FakeProducto(): 
   def __init__(self, familia, nombre, descripcion): 
       self.nombre = nombre 
       self.desc = descripcion 
       self.familia = familia
 
       self.desc = "<vaio>" 
       self.precio = 0 
       self.pesos = 0 
 
   def __str__(self): 
       return "{:20s} | {:70s} | {:>8.2f}€ " 
       .format(     self.nombre, 
               self.desc, 
               self.precio ) 
 
   ## devuelve un valor en función 
   ## de la unidad 
   def set_D(self, U): 
       if U == "MM": 
           return random.randint( 1, 50) 
       elif U == "CM": 
           return random.randint( 1, 99) 
       elif U == "M": 
           return random.randint( 1, 9) 
       elif U == "KG": 
           return random.randint( 1, 99) 
       elif U == "T": 
           return random.randint( 1, 5) 
 
   ## generación de datos aleatorios 
   ## para las Dimensiones 
   def set_dim(self, dim, du): 
           if dim == "D1": 
               return "Long =  %s %s" % ( self.set_D(du) , du) 
           elif dim == "D2": 
               return "( lo x la ) %s x %s %s" % ( self.set_D(du), 
self.set_D(du) , du) 
           elif dim == "D3": 
               return "( H x lo x la ) %s x %s x %s %s" % ( self.set_D(du), self.set_D(du), self.set_D(du) , du) 
   ## Diametro 
   def set_diam(self, d, u): 
       return "Diametro =  %s %s" % ( self.set_D(u) , u) 
 
   ## Pesos 
   def set_pesos(self, p, u): 
       return "Pesos =  %s %s" % ( self.set_D(u) , u) 
 
   ## Color 
   def set_color(self): 
       return fake.color_name() 
 
   ## Material 
   def set_material(self): 
       return random.choice(MATERIAL).capitalize() 
 
   ## Adjetivo 
   def set_adjetivo(self): 
       return random.choice(ADJETIVO).capitalize() 
 
   ## Otros 
   def set_otros(self): 
       return random.choice(OTROS).capitalize() 
 
   ## Precio 
      def set_precio(self,c_precio): 
       categ = c_precio.strip() 
       if    categ == "A": 
             return random.randint(5, 100) 
       elif categ == "B": 
             return random.randint(100, 500) 
       elif categ == "C": 
             return random.randint(100, 900) 
       elif categ == "D": 
             return random.randint(1000, 5000) 
       elif categ == "E": 
             return random.randint(2000, 9000) 
       elif categ == "F": 
             return random.randint(10000, 50000) 
 
   def set_desc(self): 
       self.desc = self.nombre.capitalize() 
       x = random.randint(0, 100) 
       if self.desc.color != 'N': 
           if x > PC_COloR: 
               self.desc = "%s %s" % (self.desc,   
                                       self.set_color() ) 
           else: 
               if self.desc.adjetivo != 'N': 
                   x = random.randint(0, 100) 
                   if x > PC_ADJETIVO: 
                       self.desc = "%s %s" % (self.desc,  
                                               self.set_adjetivo() ) 
 
       x = random.randint(0, 100) 
       if x > PC_OTROS: 
           self.desc = "%s %s" % (self.desc,   
                                   self.set_otros() ) 
 
       if self.desc.material != 'N': 
           self.desc = "%s en %s " % (self.desc,   
                                       self.set_material() ) 
 
       if self.desc.dimension: 
           self.desc = "%s %s" % (self.desc,   
                                   self.set_dim( self.desc.dimension, 
                                   self.desc.du) ) 
      
   def set_alea(self): 
       self.precio = self.set_precio( self.desc.catprecio ) 
       self.set_desc() 
 
## --------------------------------- 
## Construcción de un objeto básico
## que está en el .ods 
## --------------------------------- 
def set_data( data ): 
       familia, nombre, dim, pesos, pu, dia, diu, color, material, precio, 
adj, otros = data 
       d = PRODUCTOS[familia] 
       desc = Description( dim, pesos, pu, dia, diu, color, material, 
precio, adj, otros ) 
       d[nom] = FakeProducto( familia, nombre, desc ) 
 
 
## ------------------------------------ 
## Constitución del catálogo de básico
## ------------------------------------ 
def init(): 
   data = get_data("FAKE_PRODUCTOS.ods") 
 
   F = data['Hoja1'] 
 
   for l in F[1:]: 
       l = [ x.strip() for x in l ] 
       if l: 
           set_data( l ) 
 
def genera(): 
   F = random.choice(list(PRODUCTOS)) 
   P = random.choice(list(PRODUCTOS[F])) 
   fp = PRODUCTOS[F][P] 
   fp.set_alea() 
   return fp 
 
if __name__ == "__main__": 
   init() 
   for x in range(1,1000): 
       fp = genera() 
       print( "{:20s} | {:70s} | {:>8.2f}€ ". format( 
                   fp.nombre, fp.desc, fp.precio )) 
