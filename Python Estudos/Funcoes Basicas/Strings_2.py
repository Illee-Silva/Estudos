nome = "Antonio \n"
n=1

while nome[len(nome)-n] == " " or nome[len(nome)-n] == "\n":
    n += 1

print(nome[len(nome)-n])