"""Programa que calcula el IVA de una compra,
siendo el IVA del 21% sobre el valor total de la compra"""

def calculo_iva (a1):
    IVA = a1 * 0.21
    return IVA

precio_compra = float(input("Ingrese el valor de la compra: "))

valor_con_IVA = calculo_iva(precio_compra)

print(f"El valor total de la compra (con IVA incluido) es de {precio_compra + valor_con_IVA}")