"""
def fatorial (n):
    if n==1:
        return n
    return fatorial(n-1) * n #Recursiva pois chama a si mesma para executar um calculo

print(fatorial(5))
"""
#Função recursiva que imprima um valor de x até y

def imprimir (x, y):
    print(x)
    if x == y-1:
        print(y)
        return y
    return imprimir(x+1,y)

imprimir(100, 200)