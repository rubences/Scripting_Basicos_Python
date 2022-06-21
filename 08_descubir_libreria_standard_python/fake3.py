from faker import Faker 
fake = Faker('es_ES') 
for _ in range(10): 
   n = fake.name() 
   d = fake.date_of_birth(tzinfo=None,  
                               minimum_age=18, maximum_age=75) 
   a = fake.address() 
   a = a.replace('\n', ' ') 
   t = fake.phone_number() 
   c = fake.sentences(nb=1, ext_word_list=None) 
    
   record = """ ================================ 
   nombre            = %s 
   fecha_nacimiento = %s 
   direccion        = %s 
   telefono      = %s 
   comentario    = %s 
   """ 
 
   print(record % (n,d,a,t,c))
