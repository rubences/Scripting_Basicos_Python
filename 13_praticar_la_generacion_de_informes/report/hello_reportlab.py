from reportlab.pdfgen import canvas 
c = canvas.Canvas("hello.pdf") 
c.drawString(100,100,"Hola mundo en pdf con reportlab") 
c.save()
