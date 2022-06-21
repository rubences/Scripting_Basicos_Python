import matplotlib.pyplot as plt 
import random 
 
data = [ random.randint(5, 25) for x in range(0,20) ] 
 
plt.title(" Datos Aleatorios")     # el título
plt.plot(data)                       # transmisión de los datos
plt.ylabel('Label axe des Y')        # título del eje Y 
plt.xlabel('Label axe des X')        # título del eje X 
plt.show()                           # Visualización
