# Metodo de Euler para resolver ecuaciones diferenciales.

def crearFuncion(cadenaTexto):
    def funcion(x,y):
        return eval(cadenaTexto)
    return funcion
 
def metodoEuler(func,x,y,h,xFinal):
    n = 0
    listaDeIteraciones = []
    
    listaDeIteraciones.append((n, round(x,4), round(y,4)))
    
    while(x < xFinal):
        n=n+1
        y = y+h*func(x,y)
        x = x+h
        listaDeIteraciones.append((n, round(x,4), round(y,4)))
    
    return listaDeIteraciones

# Ejecucion principal del programa

opc=""

while(opc!="s" and opc!="S"):
    print("\n")
    print("    __  __ ___ _____ ___  ___   ___    ___  ___   ___ _   _ _    ___ ___   ")
    print("   |  \/  | __|_   _/ _ \|   \ / _ \  |   \| __| | __| | | | |  | __| _ \  ")
    print("   | |\/| | _|  | || (_) | |) | (_) | | |) | _|  | _|| |_| | |__| _||   /  ")
    print("   |_|  |_|___| |_| \___/|___/ \___/  |___/|___| |___|\___/|____|___|_|_\  \n\n\n")

    # Obtener la expresion para la funcion
    print('   Ingrese la funcion para "y prima" en terminos de "x" y "y"')
    cadenaFuncion = input("   Funcion: ")

    funcionEntrada = crearFuncion(cadenaFuncion)

    # Obtener los valores iniciales
    xFinal = float(input("\n   Ingrese el valor de X a calcular: "))
    print("\n   Ingresa los valores iniciales:")
    x = float(input("   X: "))
    y = float(input("   Y: "))
    print("\n   Ingresa el tamaño de paso:")
    h = float(input("   h: "))

    # Aplicar el metodo euler
    resultados = metodoEuler(funcionEntrada,x,y,h,xFinal)

    # Imprimir resultados
    print("\n   Resultados: ")

    for n,x,y in resultados:
        print(f"   No.{n}, x:{x}, y:{y}")

    print(f"\n   Resultado final de y: {y}\n")

    opc=str(input('Ingrese la letra "s" para salir del programa: '))