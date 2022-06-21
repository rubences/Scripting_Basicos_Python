from jinja2 import Environment, FileSystemLoader 
import datetime 
import locale 
locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8') 
 
TMPL_DIR = "tmpl" 
 
templateLoader = FileSystemLoader(searchpath=TMPL_DIR) 
templateEnv = Environment(loader=templateLoader) 
 
data={ 
       'time_stamp':datetime.datetime.now().strftime("%x %X") 
   } 
 
 
archivos = [ "index", "about" ] 
 
for archivo in archivos: 
   template = templateEnv.get_template(archivo+".jinja") 
   page = template.render( data ) 
   with open( archivo+".html", "w") as f: 
       print("Writing: %s " % archivo) 
       f.write(page)
