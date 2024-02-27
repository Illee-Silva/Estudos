import random

"""
#RandRange não inclui o ultimo valor (7)
for i in range(10):
    x = random.randrange(1, 7)
    print(x)

print("=====================")
for j in range(10):
    j = random.randrange(1, 7, 2)
    print(j)

#randint inclui o ultimo valor
print("=====================")
for i in range(10):
    x = random.randint(1, 7)
    print(x)
"""
#random Choice(Seleciona dentro da sequiencia criada)
for i in range(10):
    x = random.choice(["locutor", "Edens", "Ducck", "Mustang"])
    print(x)

#Random Random Seleciona entre 0 e 1
for i in range(10):
    x = random.random()
    print ("%.2g" %x)