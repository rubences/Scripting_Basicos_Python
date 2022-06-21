import smtplib 
import datetime 
 
## Los argumentos de autenticación
gmail_user = '<su_cuentagmail>' 
gmail_password = '<su_contraseña_gmail>' 
 
## Time stamp 
ts = datetime.datetime.now().strftime("el %X a %x") 
 
## los argumentos del mensaje
from_user = gmail_user 
to_user = ['test@chrislyon.es', 'root@example.com'] 
asunto = 'PRUEBA DE MENSAJE '+ts 
cuerpo = """ 
 
Hola 
Soy una prueba y el cuerpo del mensaje
 
Cordialmentec 
Chris 
 
""" 
 
## La construcción del mensaje y la codificación
email = """\ 
From: %s 
To: %s 
Subject: %s 
 
%s 
""" % (from_user, ", ".join(to_user), asunto, cuerpo) 
 
email_text = email.encode( encoding='UTF-8', errors='ignore') 
 
## La conexión y el envío del mensaje vía gmail 
try: 
   server = smtplib.SMTP_SSL('smtp.gmail.com', 465) 
   server.ehlo() 
   try: 
       server.login(gmail_user, gmail_password) 
   except: 
       print("Error en la autenticación") 
   server.sendmail(from_user, to_user, email_text) 
   server.close() 
 
   print('Envío del email realizado') 
except: 
   print('Problemas durante el envío del email')
