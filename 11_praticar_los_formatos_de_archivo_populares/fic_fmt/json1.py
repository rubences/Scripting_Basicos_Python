import json 
 
data = { 
    'quiz': { 
    'Capítulo 1: primer paso': { 
    'Pregunta 1': { 
      'pregunta': 'De qué se compone un bloque de código python', 
      'opciones': [ 
            "de instrucciones agrupadas en bloques de código", 
            "de fórmulas mágicas", 
            "de bloques de cemento", 
            "de bloques en plástico", 
                  ], 
      'respuesta' : '1' 
       }, 
    'Pregunta 2': { 
    'pregunta': 'un bloque de código se define en función de ', 
      'opciones' : [ 
            "su nivel de indentación", 
            "su tasa de alcohol", 
            "su densidad", 
            "su peso en kilos", 
            "su número de líneas" 
                  ], 
    'respuesta' : '1' 
                } 
            } 
        } 
    } 
 
data_json = json.dumps(data) 
#print( data_json ) # verificable en https://jsonlint.com/ 
 
data_py = json.loads( data_json ) 
for capitulos in data_py['quiz'].values(): 
    for pregunta, detalle in capitulos.items(): 
        print(" Pregunta: ",detalle['pregunta'] ) 
        for n, opcion in enumerate(detalle['opciones']): 
            print("  %s: %s " % (n+1, opcion))
