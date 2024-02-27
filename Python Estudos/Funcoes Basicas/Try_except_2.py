class ValorRepetidoERRO(Exception):
    def __str__(self):
        return 'Numero Repetido [%i]'

def def_1():
    try:
        raise ValueError
    except ValueError:
        print('Excessão Capturada!')

def def_2():
    try:
        a = int(input("Escolha um número entre 1 e 20: "))
        if not 1 <= a <= 20:
            raise ValueError
        else:
            print('Obrigado pela escolha')
    except ValueError:
        print("Entrada invalida!")

def def_3():
    lista = []

    for i in range(3):
        while True:
            try:
                num = int(input("Escolha um numero: "))
                break
            except ValueError:
                print('Digite apenas números!')
        
        if num not in lista:
            lista.append(num)
        else:
            raise ValorRepetidoERRO

"""
try
except (nome1, nome2, ...)
except (nome1, nome2, ...) as valor
except
else
finally
"""
def_3()