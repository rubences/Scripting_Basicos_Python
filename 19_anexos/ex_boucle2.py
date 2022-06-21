
##
## Bucle while simple
##
import pdb 

contador = 1

while contador <= 10:
    print("Contador : %s " % contador)
    contador += 1

pdb.set_trace()
for n in [1,2,3]:
    print(n)

##
## Bucle for
##

f = open("/etc/group")
for l in f.readlines():
    print(l)
f.close()
