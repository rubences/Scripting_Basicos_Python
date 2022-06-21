
def logitud(function):
    def funcion_interna( *args, **kwargs):
        print("============ LOGITUD ============")
        print("Funcion: {}".format(function.__name__))
        print("Argumento transmitido: ")
        print("  args    : {} ".format(args))
        print("  kwargs  : {} ".format(kwargs))
        print("================================")
        return( function(*args, **kwargs) )
    return funcion_interna


@logitud
def test1( a, b ,c):
    print(a, b ,c)

@logitud
def test2(a="?", b="?" , c="?"):
    print(a,b,c)



test1( 1, 2, 3)
test2( a="hola", b="chris")
