
def exp(n):
    def eleva(x):
        print(x**n)
    return eleva

f = exp(3)

while 0==0:
    z = int(input("Insira a base: "))
    f(z)
