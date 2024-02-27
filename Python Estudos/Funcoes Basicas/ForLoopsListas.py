#Receber Notas e exibir quantidade de alunos com nota maior que 7

alunos = 4

medias = []

for i in range(1, alunos+1):
    notas = 0

    print("===========================")
    for j in range(1, 5):
        notas += float(input("Digite a nota %i de 4 do aluno %i de %i: "%(j,i,alunos)))

    notas /= 4

    medias.append(notas)

num = 0

for media in medias:
    if media >= 7:
        num += 1

print("A quantidade de alunos que estão acima da média de 7.0 é: ", num)