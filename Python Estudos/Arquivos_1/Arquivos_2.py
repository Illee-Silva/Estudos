
def main():
    arquivo = open('textoArq.txt', 'w')
    
    arquivo.write('Ola\n')
    arquivo.write('Meu\n')
    arquivo.write('Mundo\n')
    arquivo.close

def rb_def():
    arquivo = open('textoArq.txt', 'rb')
    arquivo.readline()
    arquivo.readline()
    arquivo.close

def seek_def():
    arquivo = open('textoArq.txt', 'r')
    arquivo.seek(8)

def tell_def():
    arquivo = open('textoArq.txt', 'r')
    arquivo.tell

def forloops_def():
    arquivo = open('textoArq.txt', 'r')
    for x in arquivo:
        print(x)

def eval_def():
    lista = eval('[1,2,3,4,5]')
    print(lista)

eval_def()
#forloops_def()