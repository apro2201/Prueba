"""Crear una lista vacia y rellenarla con el precio en relación
a la lista productos por cada uno de los productos de la misma lista
Estos productos son importados a Argentina desde China y todos tienen
la misma retención o arancel de ingreso al pais (retencion 21%)
Mostrar por pantalla la lista con los valores de los productos y
finalmente mostrar la suma total de valores de la lista
"""

productos = ["televisores","computadoras", "cámaras", "accesorios"]
valor_producto =[]

retencion = 1.21

for i in productos:
    producto = int(input(f"Ingrese el importe de retención para {i}:"))
    valor_producto.append(producto * retencion)

print(valor_producto)
print(f"El total a pagar de retención o arancel que se aplica a los productos importados a Argentina desde China es de: {sum(valor_producto)}")

