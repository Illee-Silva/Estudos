contas = []
depositos = []
saldo = 0

def main():

    opcao_conta = bool(int(input("Deseja criar conta ?: ")))
    while opcao_conta:
        criaConta()
        verSaldo()
        opcao_conta = bool(int(input("Deseja criar conta ?: ")))

def criaConta():
    global contas, depositos, saldo
    num_conta = int(input("Digite um numero de conta: "))

    while num_conta in contas:
        print("conta já existe")
        num_conta = int(input("Digite um numero de conta: "))
    
    contas.append(num_conta)

    deposito = float(input("Digite o  valor do seu deposito: "))
    while deposito <=0:
        print("Valor de deposito invalido")
        deposito = float(input("Digite o  valor do seu deposito: "))
    
    depositos.append(deposito)
    saldo += deposito

def verSaldo():
    global saldo
    opcao = bool(int(input("Deseja ver o saldo do banco?: ")))
    if opcao:
        print("O saldo do banco é R$", saldo)


        
main()