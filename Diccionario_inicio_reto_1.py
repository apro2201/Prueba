"""Realizar un programa que permita llevar a cabo las siguientes opciones:
consultar el valor de la retención de un de producto,
consultar a que prodcuto pertenece una retención especifica,
y listar todos los pruductos con sus respectivas retenciones."""

productos_exp = {'Soja': 35,
                'Carne vacuna': 32,
                'Vino': 22,
                'Maíz': 23}

consultando = True

while True:

    print(" ")
    print("             PRODUCTOS DE EXPORTACIÓN")
    print("------------------------------------------------")
    print("1 - CONSULTAR POR PRODUCTO")
    print("2 - CONSULTAR POR RETENCIÓN")
    print("3 - LISTAR TODOS LOS PRODUCTOS CON SUS RETENCIONES")
    print("4 - SALIR")

    numero = "0"
    print(type(numero))
    while numero not in ("1","2","3","4"):
        numero = input("Ingrese opción: ")

    if numero == "1":
        producto = input("Ingrese el producto a consultar => ")
        print(f" El {producto}, tiene la siguiente retención {productos_exp.get(producto, 0)}")

    elif numero == "2":
        retencion = float(input("Ingrese el valor de la retención a consultar => "))
        if retencion in productos_exp.values():
            for clave in productos_exp.keys():
                if productos_exp[clave] ==retencion:
                    print(retencion, clave)

    elif numero == "3":
        for clave, valor in productos_exp.items():
                print(clave, ":", valor)

    elif numero == "4":
            break
