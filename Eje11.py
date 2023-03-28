"""11.	Ingresar la longitud del radio de un círculo. Calcular e imprimir:
•	La superficie del círculo Sup = pi * r ^2
•	El perímetro de la circunferencia Per = pi * diámetro
•	La superficie de la esfera Sup = 4 pi r ^ 2
•	El volumen de la esfera Vol = 4/3 pi r ^3"""

import math
print(math.pi)
rad=float(input("Ingrese el radio para el que desea hacer los cálculos : "))
sup = math.pi*rad ** rad
per = math.pi * rad * 2
print("Para el radio",rad,"""los cálculos son:
Sup. Círculo :""",sup,"""
Perímetro :""",per)


