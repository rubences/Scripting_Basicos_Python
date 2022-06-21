from jinja2 import Template 
import datetime 
 
## El template para el mail 
tmpl = """ 
 
El {{ data.fecha_del_dia }} 
 
Un archivo: {{ data.archivo }} ha llegado 
 
Contiene {{ data.regtrs }} registros 
 
A continuación se muestra el reparto: 
 
Pro | Descripción                    | Num  | Cantidad 
=================================================== 
{%- for l in data.lineas %} 
{{ l.fam_pro }} | {{ l.desc_fpro }} | {{ "%4d" % l.num_fpro}} | 
{{ "%4d" % l.cantidad_fpro}} 
{%- endfor %} 
=================================================== 
                      Total         | {{ "%4d" % data.total}} | 
{{"%4d" % data.totcnt}} 
 
Cordialmente 
Su servidor que le quiere 
 
""" 
 
 
 
## algunas variables 
fecha_del_dia = datetime.datetime.now().strftime("%x à %X") 
archivo =  "TEST.DAT" 
 
## Lectura del archivo en modo slurp 
with open(archivo) as f: 
   lins = f.readlines() 
 
## Recorrido y conteo de las familias de productos 
FAM = {} 
 
regtrs = len(lins) 
 
for l in lins: 
   l = l.rstrip() 
   f, d, q = l.split(':') 
   q = int(q) 
   if f in FAM: 
       FAM[f] = ( FAM[f][0], FAM[f][1]+q , FAM[f][2]+1) 
   else: 
       FAM[f] = (d, q, 1) 
 
## Cálculo de los acumulados 
lineas = [] 
total = 0 
totcnt = 0 
for x in sorted(FAM): 
   total += FAM[x][1] 
   totcnt += FAM[x][2] 
   lineas.append( { 
        'fam_pro'  : x, 
        'desc_fpro': FAM[x][0], 
        'num_fpro'  : FAM[x][1], 
        'cnt_fpro' : FAM[x][2], 
        } ) 
 
## generación del mail 
T = Template( tmpl ) 
 
print(T.render( data={ 
        'fecha_del_dia': fecha_del_dia, 
        'archivo': archivo, 
        'total': total, 
        'totcnt': totcnt, 
        'regtrs': regtrs, 
        'líneas': líneas, 
        } 
        ) 
        )
