
def soma(*lista):
    soma_num = 0

    for num in lista:
        soma_num += num
    
    return soma_num



def media(p1, p2, p3, peso1 = 1 , peso2 = 1, peso3 = 1):
    return(p1*peso1 + p2*peso2 + p3*peso3) /soma(peso1, peso2, peso3)

print(media(5, 4, 6))