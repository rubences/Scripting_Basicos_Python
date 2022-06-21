from jinja2 import Environment, FileSystemLoader 
 
## Necesario para las fechas en español
import datetime 
import locale 
locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8') 
 
TMPL_DIR = "tmpl" 
archivo = "index.jinja" 
 
templateLoader = FileSystemLoader(searchpath=TMPL_DIR) 
templateEnv = Environment(loader=templateLoader) 
template = templateEnv.get_template(archivo) 
 
data={ 
       'time_stamp':datetime.datetime.now().strftime("%x %X") 
   } 
 
print( template.render( data ) )
