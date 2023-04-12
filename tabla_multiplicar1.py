# Programa con funciones que realiza la tabla de multiplicar de un numero entero que ingresa
# Debe calcular la tabla del 0 al 12


n = int(input("Ingrese el numero para crear la tabla: "))

for i in range(0,13):
    print(f"el numero {n} * {i} = {n*i}")



