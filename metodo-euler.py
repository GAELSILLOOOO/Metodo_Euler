# Metodo de Euler para resolver Ecuaciones Diferenciales Ordinarias (EDO).

from math import *
from tabulate import tabulate
import matplotlib.pyplot as plt  # Importar Matplotlib para graficar

def CrearFuncion(cadenaTexto):
    def funcion(x,y):
        return eval(cadenaTexto)
    return funcion

def MetodoEuler(fix,func,x,y,h,xFinal):
    listaDeIteraciones = []
    
    listaDeIteraciones.append((x,y))
    
    while(x < xFinal):
        
        # Yn+1 = Yn+h*f(Xn,Yn)
        y = round((y+h*func(x,y)),int(fix))
        
        # Xn+1 = Xn + h
        x = round((x+h),int(fix))

        listaDeIteraciones.append((x,y))
    
    return listaDeIteraciones

# Ejecucion principal del programa

opc=""

while(opc!="s" and opc!="S"):
    print("\n")
    print(r"   __  __ ___ _____ ___  ___   ___    ___  ___   ___ _   _ _    ___ ___   ")
    print(r"  |  \/  | __|_   _/ _ \|   \ / _ \  |   \| __| | __| | | | |  | __| _ \  ")
    print(r"  | |\/| | _|  | || (_) | |) | (_) | | |) | _|  | _|| |_| | |__| _||   /  ")
    print(r"  |_|  |_|___| |_| \___/|___/ \___/  |___/|___| |___|\___/|____|___|_|_\  ")
    print("\n  METODO NUMERICO PARA RESOLVER ECUACIONES DIFERENCIALES ORDINARIAS (EDO). \n\n")

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

    # Solicitar la cantidad de decimales
    decimales = int(input("\n  Ingresa la cantidad de puntos decimales a mostrar: "))

    # Aplicar el metodo euler
    resultados =  MetodoEuler(decimales,funcionEntrada,xInicial,yInicial,h,xFinal)

    # Imprimir resultados
    print("\n  Resultados: \n")

    print(tabulate(resultados,headers=["Valor de X","Valor de Y"],showindex=True,tablefmt="fancy_grid"))

    print(f"\n  Resultado final:  y({xFinal}) = {resultados[-1][1]}\n\n")

    # Intentar graficar los resultados
    try:
        x_vals = [x for x, y in resultados]
        y_vals = [y for x, y in resultados]

        # Crear la gráfica
        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals, marker="o", linestyle="-", color="b", label="Método de Euler")
        plt.title("Solución aproximada con el Método de Euler", fontsize=14)
        plt.xlabel("X", fontsize=12)
        plt.ylabel("Y", fontsize=12)
        plt.grid(True)
        plt.legend(fontsize=12)
        plt.show()

    except Exception as e:
        print(f"\nError al intentar graficar: {e}")
        print("No se pudo generar la gráfica. Asegúrese de que los valores sean correctos.")

    opc=str(input('Ingrese la letra "s" para salir del programa: '))