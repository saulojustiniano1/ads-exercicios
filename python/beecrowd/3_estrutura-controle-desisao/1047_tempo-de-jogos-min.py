horario = input().split()

hora_inicial = int(horario[0])
minuto_inicial = int(horario[1])
hora_final = int(horario[2])
minuto_final = int(horario[3])

if hora_inicial > hora_final:
  hora_do_jogo = (24 - hora_inicial) + hora_final
  if minuto_inicial > minuto_final:
    minuto_do_jogo = (60 - minuto_inicial) + minuto_final
  elif minuto_final > minuto_inicial:
    minuto_do_jogo = minuto_final - minuto_inicial

elif hora_final > hora_inicial:
  hora_do_jogo = hora_final - hora_inicial
  if minuto_inicial > minuto_final:
    minuto_do_jogo = (60 - minuto_inicial) + minuto_final
  elif minuto_final > minuto_inicial:
    minuto_do_jogo = minuto_final - minuto_inicial

else:
  hora_do_jogo = 24
  minuto_do_jogo = 0

print(f'O JOGO DUROU {hora_do_jogo} HORA(S) E {minuto_do_jogo} MINUTO(S)')
