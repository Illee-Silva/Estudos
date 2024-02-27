import random 

Participantes = []

Jogadores = int(input("Insira a quantidade de jogadores: "))
Tamanho_Time1 = int(input("Insira o tamanho do time 1: "))
Tamanho_Time2 = int(input("Insira o tamanho do time 2: "))

for i in range(Jogadores):
    Participantes_in = input("Insira o nome do jogador %i de %i: " % (i+1, Jogadores))
    Participantes.append(Participantes_in)

def RoletarTimes():
    print("\n" + 40 * "=")

    Times = {'Time_1': [], 'Time_2': []}

    for i in range(Tamanho_Time1 + Tamanho_Time2):
        jogador = random.choice(Participantes)
        time = 'Time_1' if len(Times['Time_1']) < Tamanho_Time1 else 'Time_2'
        Times[time].append(jogador)
        Participantes.remove(jogador)

        jogador_str = jogador.ljust(15)
        time_str = time.ljust(10)

        print('Jogador: %s | Time: %s' % (jogador_str, time_str))

RoletarTimes()
