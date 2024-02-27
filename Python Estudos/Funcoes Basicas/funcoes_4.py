matriz = []

m = int(input("Digite o numero de linhas da matriz: "))
n = int(input("Digite o numero de colunas da matriz: "))

def constroimatriz(m, n, matriz):
    for i in range(1, m+1):
        linha = []
        for j in range(1, n+1):
            x = int(input("Digite o elemento %i|%i da matriz: "%(i,j)))
            linha.append(x)
        
        matriz.append(linha)


def trocaElemento(pos1, pos2, matriz):
    elemento1 = matriz[pos1[0]][pos1[1]]
    elemento2 = matriz[pos2[0]][pos2[1]]
    matriz[pos1[0]][pos1[1]] = elemento2
    matriz[pos2[0]][pos2[1]] = elemento1

constroimatriz(m, n, matriz)
pos1 = [int(i) for i in input("Digite a posição do elemento 1: ").split()]
pos2 = [int(i) for i in input("Digite a posição do elemento 2: ").split()]
#trocaElemento(pos1, pos2, matriz)
#print(matriz)
print(pos1)
print(pos2)