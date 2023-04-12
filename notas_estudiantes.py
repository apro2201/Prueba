""" Programa que toma las tres notas de un estudiante de RRCCII de UNTREF y devuelva la nota final del curso y
Tenga en cuenta que la primera y segunda nota valen el 30% y la tercera el 40% """

def calcular_nota (a1,a2,a3):
    return (a1 * 0.30) + (a2 * 0.30) + (a3 * 0.40)

n1 = float(input("Ingrese la primera nota: "))
n2 = float(input("Ingrese la segunda nota: "))
n3 = float(input("Ingrese la tercera nota: "))

resultado = calcular_nota(n1,n2,n3)

print(f" La nota final del estudiante es:  {round(resultado,2)}")