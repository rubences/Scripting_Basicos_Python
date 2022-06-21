from datetime import * 
from dateutil.relativedelta import * 
 
## Hoy
today = datetime.now() 
 
# Fecha de salida de la primera versión de python 
python_v1 = datetime(1991, 2, 20, 12, 00, 00) 
 
## Cálculo del número de días desde una fecha con datetime 
print( 'datetime today - python_v1: ', today - python_v1) 
 
# cálculo con dateutil  
print( 'dateutil today - python_v1: ', relativedelta(today, python_v1)) 
 
# dateutil permite añadir meses y años 
print("relative delta: aáde de 1 año + 1 mes: ", 
today+relativedelta(years=+1, months=+1)) 
 
# y también resta 
print("relative delta: resta 1 año: ", today+relativedelta(years=-1))
