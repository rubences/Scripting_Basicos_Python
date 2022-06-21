# Scripting_Basicos_Python

dirigido a ingenieros de sistemas que deseen escribir sus propias herramientas para administrar un sistema utilizando el lenguaje Python. Organizado en tres partes:

Después de algunos capítulos para presentar el entorno de trabajo y recordar los conceptos básicos del lenguaje Python, la primera parte presenta los principios de la Programación orientada a objetos en Python, así como la librería estándar de Python.

En la segunda parte se basa en cómo diseñar herramientas para recuperar información del sistema, acceder a bases de datos, utilizar diferentes formatos de archivo (.odt, .csv, .ini, .tar, .zip…), generar documentos en formato texto, CSV o HTML e incluso generar datos aleatorios, etc. Al final de esta parte, la simulación de la actividad de una pequeña empresa gestora,que permite al probar los scripts que facilitan la toma de pedidos, sus entregas y la gestión de stock.

La última parte proporciona son una serie de consejos y ejemplos concretos, que le permitirán implementar técnicas más avanzadas

## El entorno de trabajo
1. ¿ Python2 o Python3 ?
2. El entorno de trabajo
3. Un terminal y el intérprete Python
4. Configuración del entorno Python
  4.1 Etapa 1: localice el archivo binario Python que le interesa
  4.2 Etapa 2: compruebe la presencia del comando pip que acompaña a python
  4.3 Etapa 3: compruebe el módulo virtualenv
  4.4 Etapa 4: instale virtualenv wrapper
5. Las otras herramientas necesarias
## El lado funcional clásico de Python
1. Introducción
2. Primeros pasos
  2.1 El comando python
  2.2 La indentación o sangrado como sintaxis
## Algunas instrucciones básicas
1. Introducción
2. Los operadores
3. Las variables
4. Algunas instrucciones básicas
5. Resumen
## Los tipos de datos en Python
1. Introducción
2. Los booleanos
  2.1 Los operadores booleanos
  2.2 Las comparaciones lógicas
3. Los numéricos
  3.1 Los números enteros
  3.2 Los números en coma flotante
  3.3 Las operaciones
4. Los alfanuméricos
  4.1 Las operaciones aplicables a las cadenas de caracteres
  4.2 Les métodos aplicables a las cadenas de caracteres
  4.3 Los modificadores de cadenas o "string modifiers"
5. Los contenedores o secuenciales
  5.1 Las listas
  5.2 Los diccionarios
  5.3 Las tuplas
  5.4 Los sets
  5.5 Los frozensets
6. Otros tipos de datos
7. Resumen
## El lenguaje Python
1. Introducción
2. La función print()
  2.1 Print() formateado C-STYLE
  2.2 Print() formateo cadena.format()
  2.3 Print() las otras opciones
3. Las estructuras condicionales
4. Los bucles
  4.1 Algunos ejemplos simples
  4.2 La función range()
  4.3 Un "else" en los bucles
  4.4 sorted() y sort()
  4.5 enumerate()
  4.6 La asignación paralela en los bucles
  4.7 Los diccionarios y la función items()
  4.8 Las listas de comprensión
5. Las funciones
  5.1 Los argumentos de funciones con Python
  5.2 Las funciones y el alcance de las variables
  5.3 La noción de paso de argumentos por referencia
6. Los módulos y los paquetes
  6.1 Los espacios de nombres
  6.2 Los paquetes o packages
  6.3 La búsqueda de los módulos y paquetes
  6.4 El archivo __main__.py
  6.5 Ejemplo con la gestión de un restaurante
7. Las excepciones y la gestión de errores
  7.1 Las instrucciones try ... except ... finally
  7.2 La instrucción assert
  7.3 Desencadenar excepciones
8. Las entradas/salidas (archivo y otros)
9. La instrucción With
10. Ejemplo de script: hdump
11. Resumen
## El lado objeto de Python
1. Introducción
2. La POO
3. El objeto
4. La clase
5. Una clase simple
6. Añadimos atributos
7. Un primer script ”objeto”
8. La sobrecarga de funciones
9. La herencia
10. Ejemplos de scripts
  10.1 Añadimos el formato HTML
  10.2 Añadimos la etiqueta <table>
  10.3 Añadimos el formato CSV
11. Resumen
## Librería estándar y algunas otras
1. Introducción
2. El comando pip
3. Los módulos sys y os
  3.1 El módulo sys
  3.2 El módulo os
4. Las opciones de la línea de comandos
5. La interceptación de señales
6. Los archivos temporales
7. Los módulos para las operaciones en los archivos y directorios
  7.1 os.path
  7.2 shutil
  7.2.1 filecmp
  7.3 path.py
  7.4 pathlib
8. La gestión de los procesos y subprocesos
  8.1 Subprocess.run()
  8.2 subprocess.popen()
  8.3 Enviar un comando más complejo y recuperar la salida
8.4 Multiprocessing - El paralelismo de procesos
9. Mathplotlib
10. Las expresiones regulares (parece magia)
  10.1 Ejemplo: recuperar la información del estado del sistema con sar (system activity report)
  10.2 Ejemplo: recuperar la informaciónde la memoria de los procesos
11. Las fechas y el tiempo (regreso al futuro)
  11.1 stdlib: calendar, datetime, dateutil, time
  11.2 Arrow
12. El módulo logging
13. El acceso a los archivos en modo binario y el módulo struct
14. La generación de datos aleatorios
15. El acceso a las bases de datos
  15.1 Las bases de datos "SQL"
  15.2 Las bases de datos "NoSQL"
16. Los ORM u Object-Relationnal Mapping
  16.1 SQLAlchemy
  16.2 Los otros ORM
17. Red
  17.1 Un servidor web en una línea de comandos
  17.2 Enviar correos electrónico
  17.3 Python y ssh
  17.4 La transferencia de archivos con ftplib
  17.5 telnet lib
18. Python y la red de redes: Internet
  18.1 Urllib: requests
  18.2 Beautiful soup
19. Herramientas
  19.1 Pexpect
  19.2 Cmd
  19.3 shlex - Análisis léxico simple
  19.4 El módulo humanfriendly
20. Resumen
## Ir mas lejos con el lenguaje Python y la POO
1. Introducción
2. Algunos conceptos de objeto esenciales
  2.1 El polimorfismo
  2.2 La herencia múltiple
  2.3 El singleton
  2.4 La fábrica de objetos
  2.5 El cierre o closure en inglés
3. Los métodos especiales de instancias
  3.1 Las funciones especiales clásicas
  3.2 La sobrecarga de los operadores
4. El administrador de contexto (with) __enter__, __exit__
5. Los objetos mutables y no mutables
  5.1 Los mutables
  5.2 Los no mutables
6. Información adicional sobre las clases en Python
  6.1 Los atributos implícitos
  6.2 Las funciones y clases incluidas
  6.3 Los atributos estáticos y métodos estáticos
  6.4 Los __slots__ para el rendimiento
7. Las docstrings - cadenas de documentación
  7.1 Definición
  7.2 Uso
  7.3 Generación de documentación
  7.4 Pruebas
8. Los decoradores
9. Los iteradores, generadores y otras expresiones generadoras
  9.1 Los iteradores
  9.2 Los generadores
10. Gestionar sus propias excepciones
11. Las funciones nativas
11.1 Las funciones nativas in clasificables
11.2 Las funciones nativas binarias
11.3 Las funciones nativas de conversión o creación de tipo
11.4 Las funciones nativas en los iterables
11.5 Las funciones nativas en los números
11.6 Las funciones nativas en los objetos
12. Resumen
## Recuperar información del sistema
1. Introducción
2. psutil: recuperar información del sistema
3. Información de los componentes
3.1 Los procesadores
3.2 La memoria
3.3 Los periféricos de almacenamiento
3.4 La red
4. Sensores y otra información
4.1 Los sensores
4.2 Otra información
4.2.1 Boot time
4.2.2 Los usuarios
5. Información de los procesos
5.1 Clase Objeto y métodos proporcionados por psutil
5.2 Principios de uso
5.3 Ejemplos de uso
6. Resumen
## Los formatos de archivo populares
1. Introducción
2. El formato de archivo "INI"
3. Comma Separated Values: CSV
4. MS Office
5. El módulo odfpy
5.1 Documento de texto
5.2 Documento hoja de cálculo
6. El módulo multiformato pyexcel
7. El formato de archivo JSON
8. El formato de archivo XML
9. El módulo tarfile para archivos tar
10. El formato zip
11. Resumen
## Manipulación de datos
1. Introducción
2. SQLite en memoria
2.1 La misión
2.2 La recuperación de los datos
2.3 La definición de la base de datos
2.4 El script principal
3. SMS a HTML (u otro)
3.1 Extracción de los SMS
3.2 Transformación de los SMS
3.3 Conversión
3.4 Script
4. De una base de datos a otra
4.1 El contexto
4.2 Los esquemas
4.3 El script principal
5. Resumen
## La generación de informes
1. Introducción
2. La generación de PDF: Reportlab
2.1 Hola mundo en PDF y Reportlab
2.2 Una tabla con Reportlab
2.3 De nuevo una tabla, pero mejor
3. El motor de plantillas Jinja2
3.1 Jinja y el HTML
3.2 Añadamos un poco de CSS (Cascading Style Sheet)
3.3 Otro caso de uso
4. Otro motor de plantillas: Pug/Jade
4.1 Requisitos previos: instalación de Pug
4.2 El inicio del proyecto
4.3 Bootstrap, está bien
4.4 Make, está bien
5. Resumen
## Simulación de la actividad
1. Introducción
2. Descripción
3. La estructura de los datos
4. La inicialización de la base de datos
4.1 definitions.py
4.2 populate.py
5. La conexión a la base de datos
6. Los contadores
7. Los pedidos de clientes
8. La entrega de los pedidos de cliente
9. La facturación de los pedidos entregados
10. El reaprovisionamiento del stock
11. La recepción de pedidos de proveedores
12. Utilización
13. Resumen
## Trucos y consejos
1. Introducción
2. Adaptar la función copiar/pegar de una hoja de cálculo para una wiki
3. Unpacking con Python ()
4. El guion bajo y Python
4.1 En el intérprete
4.2 Para ignorar los valores
4.3 En los bucles
4.4 Par la separación de los millares
4.5 Para la nomenclatura de las variables
5. Estresar las CPU y medir el tiempo del código
6. Crear un decorador (logger interne)
7. Escribir código correctamente en Python (PEP8)
7.1 Espacios
7.2 Líneas
7.3 Tabs y encoding
7.4 Encoding: UTF8
7.5 Docstring
7.6 Nombre de variables
8. Resumen
## Ejemplos
1. Introducción
2. Python Batalla
3. Python, verificación de una mano de póquer
4. Generación de archivos y directorios aleatoria
5. Gráfica de utilización de un servidor durante un mes
6. psutil análisis de la información de los procesos
7. Mejorar Apache Index Of
7.1 WSGI
7.2 Análisis de las necesidades
7.3 Bottle
7.4 Uwsgi - ¿ Cómo hacer un entorno de test & dev ?
7.5 El script startup.py
7.6 El script page_html.py
7.7 Las plantillas
7.8 Los archivos de configuración
7.9 Puesta en producción
7.10 El resultado
8. Resumen
## Ir más lejos con Python
1. Introducción
2. Bottle y Flask
2.1 Bottle
2.2 Flask
3. Herramientas
3.1 Watchdog
3.2 paramiko
3.3 Supervisor
4. Interfaces de usuario
4.1 Interfaz gráfica: Tkinter
4.2 Otras interfaces gráficas
4.3 Interfaz de consola: curses
4.4 Interfaz de consola: Urwid
5. Resumen
Para ir incluso más lejos
1. Introducción
2. Twisted
3. Brython
4. Fuse
5. Ipython y Jupyter
6. Sphynx
7. Ansible
8. El framework Django
9. Red SCAPY
10. Apache Airflow
11. Resumen
## Anexos
1. Recursos Python
2. Memento GIT
3. Depurar en Python
4. Compilar Python desde las fuentes
5. ¿ Por qué ser fan de las expresiones regulares ?
6. Las herramientas utilizadas para esta obra
7. Creación de una máquina virtual Debian
8. Algunos consejos y aspectos a meditar
9. La última sección
