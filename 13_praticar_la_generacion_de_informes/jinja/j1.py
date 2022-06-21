from jinja2 import Template 
 
repuesta = input("Su nombre: ") 
 
tm = Template("Hola {{ nombre }}") 
texte = tm.render(nombre=reponse) 
 
print(texto)
