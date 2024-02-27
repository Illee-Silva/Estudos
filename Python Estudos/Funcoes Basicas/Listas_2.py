import random

#É possivel criar multiplas listas dentro de listas

"""
lista_1 = []

for i in range(1, 11):
    num = random.randint(0, 100)
    lista_1.append(num)

print(lista_1)
"""

#len = Mostra a quantidade de elementos em uma lista
"""
lista_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(lista_1))

#Count permite contar quantas vezes um elemento aparece
n = 1000 #quantidade de X que vai ser lançado
lancamentos = []
for i in range(n):
    lancamentos.append(random.randint(1, 6))

for i in range (1, 7):
    print("A face %i apareceu %.2f%%"%(i, 100*lancamentos.count(i)/n))
"""

#metodo Reverse

""" 
lista_2 = [1, 2, 3, 4, 5, 6]
print(lista_2)

lista_2.reverse()
print(lista_2)
"""

#metodo Remove
"""
lista_3 = [1, 2, 3, 4, 6, 6, 7]
print(lista_3)

lista_3.remove(6) #remove o primeiro elemento 6
"""

#metodo Pop Remove por indice
"""
lista_4 = [3, 4, 5, 3, 6, 7, 8]
print(lista_4)

lista_4.pop(3)
print(lista_4)
"""

#metodo Insert. Insere o elemento na posição desejada
"""
lista_5 = [1, 2, 3, 4, 5, 6]
print(lista_5)

lista_5.insert(3, 8000)
print(lista_5)
"""

#metodo sort, organiza crescentemebte
"""
lista_6 = []

for i in range(10):
    num = random.randint(1, 1000)
    lista_6.append(num)

print(lista_6)

lista_6.sort()
print(lista_6)
"""

#Metodos Clear & Copy

lista_7 = []

for i in range(10):
    num = random.randint(1, 1000)
    lista_7.append(num)

print(lista_7)

lista_7.clear()
print(lista_7)

lista_8 = []

for i in range(10):
    num = random.randint(1, 1000)
    lista_8.append(num)

print(lista_8)

lista_8b = lista_8.copy()
print(lista_8b)