"""Generar números aleatorios entre 1 y 6 (función randint del módulo random)
5 veces y cada vez se halla su máximo utilizando una función programada por nosotros."""

import random as rd

def maxim(num1,num2):
    '''Devuelve el valor máximo entre num1 y num2'''
    if num1 > num2:
        maxnum=num1
    else:
        maxnum=num2
    return maxnum

for i in range(1,6):
    a =rd.randint(0,10)
    b =rd.randint(0,10)
    print(f"Pasada número {i}")
    print(f"{a} y {b}  el mayor es : {maxim(a,b)}")