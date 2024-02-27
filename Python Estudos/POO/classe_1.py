
class obj_Teste(object):
    def __init__(self): #Metodo Construtor(Inicializa o objeto)
        self.nome = 'Pedro'
        self.idade = 18
        print('Construtor chamado com sucesso!')
    
    def imprime(self):
        print('Ola meu nome é %s e eu tenho %d'%(self.nome, self.idade))
    
Pedro = obj_Teste()

Pedro.imprime()