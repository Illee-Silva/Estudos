class ObjetoGrafico(object):
    def __init__(self, cor):
        self.cor = cor
    def area(self):
        pass
    def perimetro(self):
        pass
    def info(self):
        print('%f metros2 serao preenchidos com a cor %s'%(self.area(), self.cor))
    
    #============
class Conta(object):
    total = 10000
    reserva = 0.1

    def __init__(self, ID, saldo):
        self.ID = ID
        self.saldo = saldo
    def Deposito(self, valor):
           self.saldo += valor
           Conta.total += valor
    def Saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            Conta.total -= valor
itau = Conta(123, 5000)
itau.Deposito(1000)
itau.Saque(5000)
print(itau.saldo)
print(Conta.total)