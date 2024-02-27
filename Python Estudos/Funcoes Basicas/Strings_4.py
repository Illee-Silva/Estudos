

#.Lower(Converte em Minusculas)
def lower_def():
    texto = input("Insira um nome: ").lower
    print(texto)

#.upper(Oposto de Lower)
def upper_def():
    texto = input("Insira um nome: ").upper
    print(texto)

#.split
def split_def():
    texto_in = input("Insira um nome: ")
    texto = texto_in.split()
    print(texto)


#.isalpha Verifica se todos os caracteres são letras
#.islower verifica se todas as letras são minusculas
#.isupper verifica se todas as letras são maisculas

def startswith_def():
    texto = 'Sim'
    print(texto.startswith("S"))

#======================================
# Exemplo .Split
def ex_split_def(frase, separador):
    lista = []
    palavra = ''
    i = 0

    while i < len(frase) +1 - len(separador):
        if frase[i:i+len(separador)] != separador:
            palavra += frase[i]
        else:
            if palavra != '':
                lista.append(palavra)
            i += len(separador)
            palavra = ''
            continue

        i+=1
    
    palavra += frase[i:]

    if palavra != "":
        lista.append(palavra)
    
    return lista

#print(ex_split_def('Criptografar ou c ou descriptografar ou d', ' ou '))
