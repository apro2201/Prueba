# Hacer un programa que pida tres numeros y determine cual es el mayor

a = int(input("Ingrese el valor de a >"))
b = int(input("Ingrese el valor de b >"))
c = int(input("Ingrese el valor de c >"))

if a>b and a>c:
    print(f"{a} es el mayor de los tres")
elif b>a and b>c:
    print(f"{b} es el mayor de los tres")
elif c>a and c>b:
    print(f"{c} es el mayor de los tres")
else:
    print("Todos los numeros son iguales")