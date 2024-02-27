#Metodo __STR__ serve para retornar strings de Objetos

class Computador:
    def __init__(self, Linha, Modelo):
        self.Linha = Linha
        self.Modelo = Modelo
    
    def __str__(self):
        return('Modelo: %s\nLinha: %s'%(self.Modelo, self.Linha))
    def __add__(self, outro):
        self.Modelo += outro.Modelo
    
Drakstop = Computador('RTX', '3090')
print(Drakstop)

#Comparações
"""
__le__  x<=y
__eq__  x==y
__ge__  x>=y
__lt__  x<y
__gt__  x>y
__ne__  x!=y
"""
    