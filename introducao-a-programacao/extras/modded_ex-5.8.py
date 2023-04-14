numero_1 = int(input('Informe um número: '))
numero_2 = int(input('Informe outro número: '))

soma = 0
contador = 1

while contador <= numero_2:
  print(f'{numero_1}', end=' + ')

  soma += numero_1
  contador += 1

print(f'= {soma}')
