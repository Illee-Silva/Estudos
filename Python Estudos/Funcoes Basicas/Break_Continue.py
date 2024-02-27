
"""
#Break
for i in range(10):
    if i == 5:
        break
    print(i)


for i in range(10):
    for j in range(10):
        if j == 5:
            break
        print(i,j)
"""
#escreva uma função que produza a soma dos primeiros n números de uma lista com tamanho m
"""
def criaLista():
    lista = []

    m = int(input("Digite o tamanho da lista: "))

    for i in range(m):
        elemento = float(input("Digite o elemento: %i de %i: "%(i+1, m)))
        lista.append(elemento)
    
    return lista

def main():
    l1 = criaLista()

    n = int(input("Digite o número de elementos que se deseja soma: "))

    soma = 0
    for i in range(len(l1)):
        if i == n:
            break

        soma += l1[i]

    print("A soma é: ", soma)

main()
"""
"""
#Continue
for i in range(10):
    if i == 5:
        continue
    print(i)
"""
#Escreva um programa que pegue uma lista e gere uma nova lista com apenas numeros impares
    
lista = [419, 992, 399, 643, 876, 717, 727, 961, 552, 651, 428, 278, 358, 1, 370, 150, 81, 237,
          712, 981, 888, 840, 472, 300, 451, 59, 167, 306, 570, 182, 940, 627, 400, 694, 248, 
          483, 552, 497, 639, 18, 591, 83, 682, 412, 522, 341, 831, 60, 884, 775, 81, 403, 792, 
          791, 299, 868, 422, 493, 275, 196, 899, 237, 428, 894, 827, 854, 956, 454, 536, 227, 143, 
          689, 607, 718, 880, 720, 629, 733, 540, 414, 132, 55, 245, 424, 332, 883, 998, 264, 280, 
          561, 243, 406, 867, 930, 566, 732, 267, 313, 392, 878, 122, 420, 264, 264, 797, 523, 193, 
          272, 16, 231, 935, 730, 469, 654, 690, 296, 71, 390, 187, 45, 210] 
listaimpar = []
for i in lista:
    if i % 2 == 0:
        continue
    listaimpar.append(i)

print(listaimpar)