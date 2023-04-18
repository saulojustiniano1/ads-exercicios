soma_valor = 0

m, n = map(int, input().split())

while True:
  if m == 0:
    break
  elif n == 0:
    break 

  if n <= m:
    print(f'{n}', end=' ')
    soma_valor += n
    n += 1
    continue
  
  elif m <= n:
    print(f'{m}', end=' ')
    soma_valor += m
    m += 1
    continue
  
  elif m <= n:
    break
  elif n <= m:
    break

if m > 0 and n > 0:
  print(f'Sum={soma_valor}')

