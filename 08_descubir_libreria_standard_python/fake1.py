from faker import Factory 
fake = Factory.create() 
 
for i in range(1,10): 
   print(fake.name())
