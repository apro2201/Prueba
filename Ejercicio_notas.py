''' Hacer un programa que pida las notas de los parciales de la Materia
 Redes de Comercio Internacional y devuelva por pantalla el promedio de las notas y
  finalmente que nos indique si el estudiante promocionó la materia '''

#notas = int(input("Ingrese la cantidad de parciales que rindió: "))

tparcial = 0

for i in range(1, 4):
    parcial = float(input(f"Ingrese la nota del parcial numero {i}: "))

tparcial += parcial

promedio = tparcial/i

print(f"El promedio de notas es de: {promedio:.2f}")

if promedio >= 8:
    print("Felictaciones promocionó la materia")
elif promedio <8 and promedio >= 7.25:
    print("Aprobó la materia - Reveer la situación para promocionar")
elif promedio <7.25 and promedio >= 4:
    print("Aprobó la materia - debe rendir examen final")
else:
    print("Debe recursar la materia")
