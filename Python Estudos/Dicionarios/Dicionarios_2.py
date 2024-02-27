
#Permite guardar "Lambdas" dentro de um dicionario
Dicionario = {'Lambda': lambda x: x+1}
Dicionario1 = {'Nome': 'Pedro', 'Telefone': '123-456', 'Celular': '789-012', 'Email': 'reidelas@gmail.com'}

print(Dicionario['Lambda'](3))

#Utilizar um For Loop em um dicionario, exibe as chaves.
for coisa in Dicionario1:
    print(coisa)

#In, verifica se uma chave está inclusa no dicionario
print("Nome" in Dicionario1)
