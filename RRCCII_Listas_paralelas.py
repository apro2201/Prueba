""" Las marcas chinas como Lenovo, Huawei, Hisense, TCL y Xiaomi son populares en Europa.
A continuación se presentan dos listas con algunos de los productos electrónicos
 más importantes que China exporta a Europa"""

productos =['Teléfonos móviles', 'Computadoras', 'Tabletas', 'Paneles solares', 'Auriculares']
precio =[150,600,350,450,20]

print(precio[0])

print(type(productos))
print(sum(precio))

maxvalor = max(precio)
inprecio = precio.index(maxvalor)
inproducto = productos[inprecio]
print(inproducto,maxvalor)

psolares = productos.index('Paneles solares')
psolaprecio = precio[psolares]
print(psolaprecio)

i = 0
for i in range(len(productos)):
    maxvalor = max(precio)
    inprecio = precio.index(maxvalor)
    inproducto = productos[inprecio]
    print(productos[inprecio], precio[inprecio])
    del precio[inprecio]
    del productos[inprecio]





