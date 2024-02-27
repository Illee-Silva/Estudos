#Colchetes são responsaveis pela criação de listas
lista = [1, 2, 3, 4, 5, 6]
print (lista[-1])

lista += [8]
print (lista[-1])

print(lista)
lista[6] += lista[1]
print(lista)
print(lista[0:7]) #Percorrimento

print(lista[0:7:2]) #Passamento de 2

print(lista[::-1]) #inverte a lista