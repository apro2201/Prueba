"""Escribe un programa que le pregunte al usuario
su nombre, edad, dirección, y teléfono. Estos datos lo debe guardar en un diccionario
y después debe mostrar por pantalle el mensaje <nombre> tiene <edad> años, vive en <dirección>
 y su número de teléfono es <teléfono>"""

nombre = input("Escribe tu nombre: ")
edad = int(input("Escribe tu edad: "))
direccion = input("Escribe tu dirección: ")
telefono = input("Escribe tu número de teléfono: ")

datos_usuario ={
    'nombre': nombre,
    'edad': edad,
    'dirección': direccion,
    'telefono': telefono
}

print(f"{datos_usuario['nombre']} tiene {datos_usuario['edad']}, vive en {datos_usuario['dirección']} y su número de telefono es {datos_usuario['telefono']} ")


