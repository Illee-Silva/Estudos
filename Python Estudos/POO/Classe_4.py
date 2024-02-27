#Herança e Polimorfismo

class Mamifero(object):
    def __init__(self, cor_de_pelo, genero, andar):
        self.cor_de_pelo = cor_de_pelo
        self.genero = genero
        self.num_de_patas = andar

    def Falar(self):
        print('Ola sou um mamifero e eu sei falar')
    def Andar(self):
        print('Estou andando sobre %i patas'&self.num_de_patas)
    def Amamentar(self):
        if self.genero.lower()[0] == 'm':
            print('Machos não amamentam')
            return
        print('Amamentando meu filhote')

class Pessoa(Mamifero):
    def __init__ (self, cor_de_pelo, genero, andar, cabelo):
        super(Pessoa, self).__init__(cor_de_pelo, genero, andar)
        self.cabelo = cabelo
    def Falar(self):
        print("Eu sou um mamifero e sei falar")
#==================================================#
Rex = Mamifero('Marrom', 'masculino', 4)
Julia = Pessoa('Preta', "Feminino", 2, 'Loiro')

Julia.Falar()
