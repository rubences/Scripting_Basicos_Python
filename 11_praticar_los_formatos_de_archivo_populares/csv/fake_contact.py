from faker import Faker 
fake = Faker('es_ES') 
 
def fake_contact(num=1): 
   for _ in range(num): 
       n = fake.name() 
       d = fake.date_of_birth(tzinfo=None,  
                   minimum_age=18, maximum_age=75) 
       a = fake.address() 
       a = a.replace('\n', ' ') 
       t = fake.phone_number() 
       c = fake.sentences(num=1, ext_word_list=None) 
   return n,d,a,t," ".join(c) 
 
def fake_contact_asdict(): 
   n,d,a,t,c = fake_contact() 
   return { 
           ’nombre': n, 
           'fecha_nacimiento': d, 
           'dirección': a, 
           'teléfono': t, 
           'comentario': c 
           } 
 
if __name__ == "__main__": 
   print(fake_contact()) 
   print(fake_contact_asdict())
