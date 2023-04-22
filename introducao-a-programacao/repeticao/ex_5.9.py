numero_1 = int(input('Informe um valor: '))
numero_2 = int(input('Informe outro valor: '))

if numero_1 > numero_2:
  maior = numero_1
  menor = numero_2
else:
  maior = numero_2
  menor  = numero_1

div = 1

while menor < maior:
  maior -= menor

  div += 1

print(f'{numero_1} / {numero_2} = {div}')
