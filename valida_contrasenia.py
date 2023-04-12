"""Programa con función que valida si una contraseña es segura
Es posible aplicarlo en banca electronica en relación a la carrera RRCCII UNTREF

-> Tiene más de 8 caracteres
-> Tiene al menos una letra mayúscula
-> Tiene al menos un número """

"""print(len("Agustin"))
print("a".isupper())
print("1".isnumeric())
cadena = "HOLA"
print(cadena[3])

for i in range(len(cadena)):
    print("holis")"""

def contrasenia (password):

    largo = False
    mayus = False
    numer = False
    espa = False

    if len(password) > 8:
        largo = True
        for i in range(len(password)):
            if password[i].isupper():
                mayus = True
            if password[i].isnumeric():
                numer = True
            if password[i].isspace():
                espa = True

    if largo and mayus and numer and espa == False:
        return True
    else:
        return False

password = input("Ingresar la contrasenia: ")

verificar = contrasenia(password)

if verificar == True:
    print("La contraseña es segura")
else:
    print("La contraseña no es segura")














