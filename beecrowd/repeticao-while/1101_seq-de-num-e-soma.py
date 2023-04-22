contador = 0

while contador < 1:
  m, n = map(int, input().split())

  soma_valor = 0

  if m == 0 or m < 0:
    contador += 1
  elif n == 0 or n < 0:
    contador += 1

  if m > n:
    maior = m
    menor = n
  else:
    maior = n
    menor = m
    
  if maior > 0 and menor > 0:
    while menor <= maior:
      print(f'{menor}', end=' ')
      soma_valor += menor
      menor += 1

  if maior > 0 and menor > 0:
    print(f'Sum={soma_valor}')
