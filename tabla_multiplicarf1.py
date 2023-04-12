# Programa con funciones que realiza la tabla de multiplicar de un numero entero que ingresa
# Debe calcular la tabla del 0 al 12

def tabla_de_multiplicar (a,b):
    return str(a) + "*" + str(b) + "=" +str(a*b)

n = int(input("Ingrese el numero para crear la tabla: "))

for i in range(0,13):
    print(tabla_de_multiplicar(i,n))



