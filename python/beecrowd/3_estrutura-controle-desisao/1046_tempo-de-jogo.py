horario = input().split()

hora_inicial = int(horario[0])
hora_final = int(horario[1])

if hora_inicial > hora_final:
  tempo_de_jogo = (24 - hora_inicial) + hora_final
elif hora_inicial < hora_final:
  tempo_de_jogo =  hora_final - hora_inicial
else:
  tempo_de_jogo = 24

print(f'O JOGO DUROU {tempo_de_jogo} HORA(S)')
