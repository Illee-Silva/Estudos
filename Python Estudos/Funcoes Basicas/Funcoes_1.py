"""
def função(arg1, arg2,...., argn):
    script
    return val1, val2, ..., valn
"""

#Exemplo 1
"""
def soma():
    a = 2
    b = 3
    soma_de_ab = a + b
    return
"""

#Exemplo 2
"""
def potencia(base, exp):
    pot = base**exp
    return pot

val1 = 2
val2 = 3

print(potencia(val1,val2))
"""

#Exemplo 3
"""
def soma_3(num1, num2, num3):
    return num1+num2+num3

print(soma_3(1, 3, 5))
"""

#Teste 1
def opMath(num1, num2):
    multi = num1*num2
    divis = num1/num2
    return(multi, divis)

in_val1 = int(input("Insira o valor 1: "))
in_val2 = int(input("Insira o valor 2: "))

print("a multiplicação dos numeros inserios é: %i \nA divisão dos numeros inseridos é: %i"%(opMath(in_val1, in_val2)))