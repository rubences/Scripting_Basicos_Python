from jinja2 import Environment, FileSystemLoader 
import datetime 
import locale 
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8') 
 
from path import Path 
from humanfriendly import format_size 
 
import configparser as cp 
 
## Los argumentos 
params = cp.ConfigParser() 
params.read("params.ini") 
 
## Algunos argumentos 
TMPL_DIR = params.get("ARGUMENTOS",'TMPL_DIR') 
DATA_DIR = params.get("ARGUMENTOS",'DATA_DIR') 
FIC_DESC = params.get("ARGUMENTOS",'FIC_DESC') 
BASE_DOWNLOAD = params.get("ARGUMENTOS", 'BASE_DOWNLOAD') 
HOME = params.get("ARGUMENTOS",'HOME') 
 
if BASE_DOWNLOAD == '': 
   BASE_DOWNLOAD = '/'+DATA_DIR 
 
desc_archivos = cp.ConfigParser() 
desc_archivos.read(FIC_DESC) 
 
templateLoader = FileSystemLoader(searchpath=TMPL_DIR) 
templateEnv = Environment(loader=templateLoader) 
 
DOWNLOAD = chr(8659) 
DOWNLOAD = "Descargar" 
 
## Recuperación de la información de los archivos 
def get_info(archivo): 
   try: 
       desc = desc_archivos.get(str(archivo.relpath(start=DATA_DIR)), 'description') 
   except: 
       desc = '' 
   return desc 
 
## Construcción del breadcrum 
def make_breadcrum( ruta ): 
   breadcrum = '''<nav aria-label="breadcrumb"> 
                 <ol class="breadcrumb"> 
                 ''' 
   p = Path(ruta) 
   bc = '' 
   for n in p.splitall()[1:]: 
       if n == DATA_DIR: 
           bc += '/'+n 
           n = HOME 
           nav = '<li class="breadcrumb-item"> 
               <a href="%s">%s</a></li>' % ( bc, n ) 
       else: 
           bc += '/'+n 
           nav = '<li class="breadcrumb-item"> 
               <a href="%s">%s</a></li>' % ( bc, n ) 
       #print(n, bc) 
       breadcrum += nav +'\n' 
   breadcrum += ''' </ol> </nav> ''' 
   return breadcrum 
 
## se recuperan los directorios 
def get_dirs(rep): 
   p = Path(rep) 
   return sorted(list(p.dirs())) 
 
def get_files(rep): 
   p = Path(rep) 
   l = [ f for f in p.files() if not f.name.startswith('.') ] 
   return sorted(l) 
 
def get_page( env ): 
   URI = env['REQUEST_URI'] 
   if URI == '/': 
       URI = '/'+DATA_DIR 
   URI = URI[1:] 
   ## Los directorios 
   directorios = [] 
   for r in get_dirs(URI): 
       mod_date = datetime.datetime.fromtimestamp(r.getmtime()) 
       r1 = {  'nombre':'<a href="%s">%s</a>' % 
                ( '/'+str(r.relpath()), str(r.name)), 
               'fecha':  mod_date.strftime("%d %B %Y à %X"), 
               'info': get_info( r ) 
           } 
       directorios.append(r1) 
 
   ## Los archivos 
   archivos = [] 
   for f in get_files(URI): 
       f_name = f.name 
       f_dir  = f.padre.split('/')[1:] 
       f_dir.append(str(f.name)) 
       f_lnk  = "/".join(f_dir) 
       dl_lnk = BASE_DOWNLOAD+'/'+f_lnk 
       mod_date = datetime.datetime.fromtimestamp(f.getmtime()) 
       f1 = {  ’nombre’: str(f.name), 
               'download':'<a href="%s"  
               class="badge badge-pill badge-primary">%s 
               </a>' % (dl_lnk, DOWNLOAD), 
               'size': format_size(f.size), 
               'date':  mod_date.strftime("%d %B %Y à %X"), 
               'info': get_info( f ) 
              } 
       archivos.append(f1) 
 
   ## Suma de la info 
   page_data = { 
           'time_stamp':datetime.datetime.now() 
                       .strftime("%x %X"), 
           'archivos': archivos, 
           'rep': directorios, 
           'breadcrum': make_breadcrum(URI) 
           } 
   archivo = "index" 
   template = templateEnv.get_template(archivo+".jinja") 
   page = template.render( data=page_data ) 
   return page 
 
## Para probar 
def get_page_t( env ): 
   page = "Hello World" + '\n' 
   page += '<br/>' 
   page += ' Directorio = %s ' % env['REQUEST_URI'] + '\n' 
   page += '<br/>' 
   return page 
 
if __name__ == '__mano__': 
   p = get_page( { 'REQUEST_URI': '/' }) 
   #p = make_breadcrum( '/data/dolores' ) 
   print(p)
