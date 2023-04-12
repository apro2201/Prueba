"""Crear una lista vacia y rellenarla con el precio de retenciones
por cada uno de los bienes primarios de la lista commodities
Mostrar por pantalla el valor de retención de cada commoditie y
finalmente mostrar la suma total de retenciones de la lista
"""

commodities = ["Soja", "Maíz", "Trigo","Carne bovina", "Limones", "vino"]
commodities.append("Gas natural")

pimport =[]

for i in commodities:
    alicuota = float(input(f"Ingrese la retención de import. de {i}: "))
    pimport.append(alicuota)

for i in range(len(commodities)):
    print(f"{commodities[i]} tiene un precio de import. de {pimport[i]}")

print(f"El total de retenciones a pagar es de {sum(pimport)}")