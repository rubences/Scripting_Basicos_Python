def pc(cantidad, total): 
   assert total > 0, 'total debe ser estrictamente positivo' 
   assert 0 <= cantidad, 'cantidad debe ser positiva' 
   assert cantidad <= total, 'cantidad debe ser inferior a total' 
   return (cantidad / total) * 100 
 
if __name__ == '__main__': 
   print( "=> %3.2f%%" % pc(15, 100)) 
   print( "=> %3.2f%%" % pc(35, 67)) 
   print( "=> %3.2f%%" % pc(23, 124)) 
   print( "=> %3.2f%%" % pc(7, 0))     ## Aquí hay una excepción
