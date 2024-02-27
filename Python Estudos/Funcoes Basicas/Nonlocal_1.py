"""
def f1():
    comeco = 0
    def f2():
        nonlocal comeco
        print(comeco)
        comeco += 1
    return f2

g = f1()
g()
g()
g()
g()
"""

def lista():
    start = 0
    lista = []
    def incrementa(item):
        nonlocal lista, start
        lista.append(item)
        start += 1
        print(item, start)
    return incrementa

compras1 = lista()

compras1("presunto")
compras1("queijo")
compras1("macaco")