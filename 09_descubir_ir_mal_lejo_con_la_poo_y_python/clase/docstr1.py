# ----------------------- 
# Un módulo documentado 
# ----------------------- 
 
""" 
   Un módulo documentado 
   =================== 
 
Este es un ejemplo para probar y ver qué
    podemos hacer con docstrings
 
  :Example: 
 
   >>> from docstr1 import agregar 
   >>> agregar(1, 1) 
   2 
 
   Ponemos subtítulo 
   ------------------------------ 
 
   Si tiene indicaciones sobre este módulo 
   este es el sitio correcto 
 
 
   Otro subtítulo 
   -------------------- 
 
   Lorem ipsum dolor sit amet, consectetur adipisicing elit, 
   tempor incididunt ut labore y dolore magna aliqua. 
   quis nostrud exercitation ullamco laboris nisi ut 
   
""" 
 
def agregar(a, b): 
   """ 
       Añade 2 números y devuelve el resultado 
 
esta función no hace nada mejor que este viejo
        operador '+' pero es un ejemplo de docstring
 
       : param a: el primer argumento
       : param b: el segundo argumento
       : escriba a: int o float
       : tipo b: int o float
       : return: El resultado de sumar a + b
       : rtype: int o float
 
      :Example: 
 
       >>> agregar (1, 1)        # int 
       2 
       >>> agregar (2.1, 3.4)    # float 
       5.5 
 
.. seealso:: PEP 257 que describe las buenas
              prácticas para las docstrings
        .. warning:: En ningún caso se trata de un módulo real
                     Es solo para mostrar lo que
                     puede hacer con docsstrings
        .. note :: Agregar una nota
        .. todo :: Si tiene un todo relacionado con este módulo
   """ 
   return a + b
