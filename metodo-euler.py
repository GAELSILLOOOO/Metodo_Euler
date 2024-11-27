# Metodo de Euler para resolver Ecuaciones Diferenciales Ordinarias (EDO).

from math import *
from tabulate import tabulate

def CrearFuncion(cadenaTexto):
    def funcion(x,y):
        return eval(cadenaTexto)
    return funcion
 
def MetodoEuler(func,x,y,h,xFinal):
    listaDeIteraciones = []
    
    listaDeIteraciones.append((x,y))
    
    while(x < xFinal - 1e-9):
        y = y+h*func(x,y)
        x = x+h
        if (x>xFinal):
            x = xFinal
        listaDeIteraciones.append((x,y))
    
    return listaDeIteraciones

# Ejecucion principal del programa

opc=""

while(opc!="s" and opc!="S"):
    print("\n")
    print("   __  __ ___ _____ ___  ___   ___    ___  ___   ___ _   _ _    ___ ___   ")
    print("  |  \/  | __|_   _/ _ \|   \ / _ \  |   \| __| | __| | | | |  | __| _ \  ")
    print("  | |\/| | _|  | || (_) | |) | (_) | | |) | _|  | _|| |_| | |__| _||   /  ")
    print("  |_|  |_|___| |_| \___/|___/ \___/  |___/|___| |___|\___/|____|___|_|_\  \n\n\n")

    # Obtener la expresion para la funcion
    print('  Ingrese la funcion para "y prima" en terminos de "x" y "y"')
    cadenaFuncion = input("  Funcion: ")

    funcionEntrada = CrearFuncion(cadenaFuncion)

    # Obtener los valores iniciales
    xFinal = float(input("\n  Ingrese el valor de X a calcular: "))
    print("\n  Ingresa los valores iniciales:")
    xInicial = float(input("  X: "))
    yInicial = float(input("  Y: "))
    print("\n  Ingresa el tamaño de paso:")
    h = float(input("  h: "))

    # Aplicar el metodo euler
    resultados =  MetodoEuler(funcionEntrada,xInicial,yInicial,h,xFinal)

    # Imprimir resultados
    print("\n  Resultados: \n")

    print(tabulate(resultados,headers=["Valor de X","Valor de Y"],showindex=True,tablefmt="fancy_grid"))

    print(f"\n  Resultado final:  y({xFinal}) = {resultados[-1][1]}\n\n")

    opc=str(input('Ingrese la letra "s" para salir del programa: '))