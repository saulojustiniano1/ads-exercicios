hora_inicial, minuto_inicial, hora_final, minuto_final = input().split()

hora_inicial = int(hora_inicial)
minuto_inicial = int(minuto_inicial)
hora_final = int(hora_final)
minuto_final = int(minuto_final)

if hora_inicial > hora_final:
  hora_do_jogo = (24 - hora_inicial) + hora_final
elif hora_final >= hora_inicial:
  hora_do_jogo = hora_final - hora_inicial

if minuto_inicial > minuto_final:
  minuto_do_jogo = (60 - minuto_inicial) + minuto_final
  hora_do_jogo -= 1
elif minuto_final >= minuto_inicial:
  minuto_do_jogo = minuto_final - minuto_inicial

if hora_inicial == hora_final and minuto_inicial == minuto_final:
  hora_do_jogo = 24
  minuto_do_jogo = 0

if hora_do_jogo < 0:
  hora_do_jogo += 24

print(f'O JOGO DUROU {hora_do_jogo} HORA(S) E {minuto_do_jogo} MINUTO(S)')
