"""
class Minha:
    def __init__(self):
        self.x = 0
        self.y = 0

meu = Minha()

meu.z = 1
print(meu.z)
"""

class Pessoa:
    def __init__(self, nome, peso, cao):
        self.nome = nome
        self.peso = peso
        self.cao = cao
    def treinar(self):
        self.cao.daApatinha()
        self.cao.latir()

class Cachorro:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    def daApatinha(self):
        print('%s extendeu a patinha'%self.nome)
    def latir(self):
        print('auauauauauauaua')

rex = Cachorro('Rex', 'Marrom')
pedro = Pessoa('Pedro', 75, rex)

print(pedro.cao.cor)
pedro.treinar()