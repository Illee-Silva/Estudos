"""
try:
    x = int(input("Insira um valor numerico: "))
    print(x)
except:
    print("ERRO!")
"""
#============
def def_1():
    try:
        x = int(input("Insira um valor numerico: "))
    except:
        print("ERRO!")
        x = 0
    finally:
        print(x)

#def def_2():
    # é possivel especificar o erro
    #except FileNotFoundError