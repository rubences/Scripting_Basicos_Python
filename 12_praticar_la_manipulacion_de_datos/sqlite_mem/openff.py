import requests 
 
def get_prod(): 
   s_terms = { 
               'action':'process', 
               'tagtype_0':'countries', 
               'tag_contains_0':'contains', 
               'tag_0':'Spain', 
               'tagtype_1':'ingredients', 
               'tag_contains_1':'contains', 
               'tag_1':'taurina', 
               'page_size':500, 
               "json": 1 
             } 
 
   url = "https://es.openfoodfacts.org/cgi/search.pl?" 
   res = requests.get(url, params=s_terms) 
 
   resultados = res.json() 
   productos = resultados["productos"] 
 
   data = [] 
   data.append( [  ”Código”, “Nombre", “Cantidad",  ”Marca", 
                   ”Nutrición", “Nombre Genérico" 
                ] ) 
   for producto in productos: 
       row = [     producto[“code”], 
                   producto["product_name"], 
                   producto.get("quantity", ""), 
                   producto.get("brands", ""), 
                   producto.get("Nutritio_grade_es", ""), 
                   producto.get("generic_name", "") 
               ] 
       data.append(row) 
   return data 
 
def main(): 
   data = [] 
   data = get_prod() 
   print(data) 
 
if __name__ == '__mai 
   main()
