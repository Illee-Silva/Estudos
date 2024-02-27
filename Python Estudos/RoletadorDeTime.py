import random 

Participantes = []

Jogadores = int(input("Insira a quantidade de jogadores: "))
jogadores_c = 0
jogadores_c += Jogadores

Tamanho_Time1 = jogadores_c//2
Tamanho_Time2 = jogadores_c - Tamanho_Time1

for i in range(Jogadores):
    Participantes_in = input("Insira o nome do jogador %i de %i: " % (i+1, Jogadores))
    Participantes.append(Participantes_in)

def RoletarTimes():
    print("\n" + 40 * "=")

    Times = {'Time_1': [], 'Time_2': []}

    gatilho = True

    for i in range(Tamanho_Time1 + Tamanho_Time2):
        jogador = random.choice(Participantes)
        time = 'Time_1' if len(Times['Time_1']) < Tamanho_Time1 else 'Time_2'
        Times[time].append(jogador)
        Participantes.remove(jogador)

        jogador_str = jogador.ljust(15)
        time_str = time.ljust(10)

        print('Jogador: %s | Time: %s' % (jogador_str, time_str))
        
        if len(Times['Time_1']) == Tamanho_Time1 and gatilho == True:
            print(40*'=')
            gatilho = False

    print(4*"\n")
    x = input("Aperte Qualquer tecla para continuar...")

RoletarTimes()
