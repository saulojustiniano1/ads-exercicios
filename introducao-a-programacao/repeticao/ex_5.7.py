tabuada = int(input('TABUADA: '))
inicio_tabuada = int(input('Inicio da tabuada: '))
fim_tabuada = int(input('Fim da tabuada: '))

print('=-' * 13)
while inicio_tabuada <= fim_tabuada:
  print(f'{tabuada} x {inicio_tabuada} = {tabuada * inicio_tabuada}')

  inicio_tabuada += 1
