"""Debemos tener clara cuál va a ser la condición que se debe cumplir
 para que el ciclo esté pidiendo el número contantemente.
El ciclo se va a detener solo cuando el número ingresado sea igual a 0,
así que la condición para que se siga ejecutando es que el numero NO sea 0.
Veámoslo entonces."""

numero = float(input('Ingresa un número. 0 para terminar: '))

while(numero != 0):
    numero = float(input('Ingresa un número. 0 para terminar: '))

print('Fin del programa.')