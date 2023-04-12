"""Escribir un programa que guarde en una variable
El diccionario {'Euro':'€','Dolar':'$', 'Yen':'Y'} y muestre
su símbolo o un mensaje si la divisa no está en el diccionario
if divisas.get(divisa):
    print(divisas.get(divisa))"""

divisas = {'Euro':'€',
           'Dolar':'$',
           'Yen':'Y'}
print(divisas.keys())
print(divisas.values())
print(divisas['Dolar'])

divisa = input("Escribe una divisa: ")

if divisa in divisas:
    print(f"El valor de {divisa} es:  {divisas[divisa]}")
else:
    print("La divisa no se encuentra")