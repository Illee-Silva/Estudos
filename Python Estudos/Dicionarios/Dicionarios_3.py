
#metodo Get
def get_def():
    contato = {'Nome': 'Pedro', 'Telefone': '123-456', 'Celular': '789-012', 'Email': 'reidelas@gmail.com'}

    print(contato.get("Nome"))

#metodo Items(Cria Tuplas)
def items_def():
    contato = {'Nome': 'Pedro', 'Telefone': '123-456', 'Celular': '789-012', 'Email': 'reidelas@gmail.com'}

    print(contato.items())

#Metodo Keys(Cria Listas com apenas as chaves)
def keys_def():
    contato = {'Nome': 'Pedro', 'Telefone': '123-456', 'Celular': '789-012', 'Email': 'reidelas@gmail.com'}

    print(contato.keys())

#Metodo Values(Cria Listas com apenas os valores)
def values_def():
    contato = {'Nome': 'Pedro', 'Telefone': '123-456', 'Celular': '789-012', 'Email': 'reidelas@gmail.com'}

    print(contato.values())

#Metodo Copy
def copy_def():
    contato = {'Nome': 'Pedro', 'Telefone': '123-456', 'Celular': '789-012', 'Email': 'reidelas@gmail.com'}
    contato2 = contato.copy
    print(contato2)

#Metodo pop
def pop_def():
    contato = {'Nome': 'Pedro', 'Telefone': '123-456', 'Celular': '789-012', 'Email': 'reidelas@gmail.com'}

    contato.pop() #deleta uma chave
    print(contato.popitem) #Deleta A primeira chave e retorna uma tupla com o valor e a chave

#Metodo Default modifica ou adiciona uma nova chave
def Default_def():
    contato = {'Nome': 'Pedro', 'Telefone': '123-456', 'Celular': '789-012', 'Email': 'reidelas@gmail.com'}

    contato.setdefault('Nome')
    contato.setdefault('Bairro', 'Centro')

#Consultor DICT
def dict_def():
    dict() #não apresentado na aula