class Pessoa:
    pass

cli1 = Pessoa()
cli1.nome = 'Lucas'
cli1.emprego = None
cli1.corCabelo = 'Preto'

print(cli1.__dict__)
