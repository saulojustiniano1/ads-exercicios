dia_inicial, data_inicial = input().split()
hora_inicial, minuto_inicial, segundo_inicial = map(int, input().split(' : '))

dia_final, data_final = input().split()
hora_final, minuto_final, segundo_final = map(int, input().split(' : '))

data_inicial = int(data_inicial)
data_final = int(data_final)

dia_de_jogo = data_final - data_inicial

if hora_inicial > hora_final:
  hora_de_jogo = (24 - hora_inicial) + hora_final
  dia_de_jogo -= 1
elif hora_inicial <= hora_final:
  hora_de_jogo = hora_final - hora_inicial

if minuto_inicial > minuto_final:
  minuto_do_jogo = (60 - minuto_inicial) + minuto_final
  hora_de_jogo -= 1
  if hora_de_jogo < 0:
    hora_de_jogo += 24
    dia_de_jogo -= 1
elif minuto_inicial <= minuto_final:
  minuto_do_jogo = minuto_final - minuto_inicial

if segundo_inicial > segundo_final:
  segundo_do_jogo = (60 - segundo_inicial) + segundo_final
  minuto_do_jogo -= 1
  if minuto_do_jogo < 0:
    minuto_do_jogo += 60
    hora_de_jogo -= 1
elif segundo_inicial <= segundo_final:
  segundo_do_jogo = segundo_final - segundo_inicial

print(f'{dia_de_jogo} dia(s)')
print(f'{hora_de_jogo} hora(s)')
print(f'{minuto_do_jogo} minuto(s)')
print(f'{segundo_do_jogo} segundo(s)')
