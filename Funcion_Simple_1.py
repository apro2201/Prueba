#Definimos la Funcion

def prueba (a,b):
    total = a + b
    a += 1  # modifico un argumento
    b += 1
    return total

# Llamamos a la Función

n1 = 10
n2 = 20

resultado = prueba(n1,n2)

print(prueba(n1,n2))

print ("La función nos devolvió como resultado : ", resultado )
print ("Ahora la variable a es ",n1," y variable b es ",n2, " - No cambiaron")