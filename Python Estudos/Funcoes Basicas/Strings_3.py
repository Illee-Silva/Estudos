#Função CHR(Imprime o caractere representado pelo ASCII)
print(chr(92))

#Função ORD(é o aposto da função CHR)
print(ord("|"))

#comparação de Strings
print('a' == 'c')
print('A' < 'a')

def main():
    texto = 'ChIcLeTE'

    print(tudoMinusculo(texto))
    print(tudoMaiusculo(texto))

def tudoMinusculo(texto_in):
    minusculo = ""

    for char in texto_in:
        if 'A' <= char <= 'Z':
            char = chr(ord(char) + (ord('a') - ord('A')))
        minusculo += char
    
    return minusculo

def tudoMaiusculo(texto_in):
    maiusculo = ""

    for char in texto_in:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - (ord('a') - ord('A')))
        maiusculo += char
    
    return maiusculo

main()