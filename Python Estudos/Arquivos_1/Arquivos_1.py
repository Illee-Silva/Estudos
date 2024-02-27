# 'w' = Write
# 'r' = Read
# 'a' = Append

def write_def():
    arquivo = open('OlaArquivo.txt', 'w') #Modos de abertura('w', 'r', 'a')

    arquivo.write('Macdonalds é legal')
    arquivo.write('\n')
    arquivo.writelines(["Ola ", "Arquivo ", "Essa ", "e ", "uma ", "Mensagem ", "de ", "lista"])

def read_def():
    arquivo = open('OlaArquivo.txt', 'r')
    #print(arquivo.read())

    #readline
    print(arquivo.readline())
    print(arquivo.readlines())

def append_def():
    arquivo = open('OlaArquivo.txt', 'a')
    arquivo.write("\nNova Linha")

#read_def()
#write_def()
append_def()