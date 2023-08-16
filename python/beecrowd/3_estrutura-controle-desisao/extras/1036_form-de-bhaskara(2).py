valores = input().split()

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

if a != 0:
  delta = (b ** 2) - (4 * a * c)
  if delta > 0:
    x1 = (- b + (delta ** 0.5)) / (2 * a)
    x2 = (- b - (delta ** 0.5)) / (2 * a)
    if x1 == x2:
      print(f'R = {x1:.5f}')
    else:
      print(f'R1 = {x1:.5f}')
      print(f'R2 = {x2:.5f}')
  else:
    print('Impossivel calcular')
else:
  print('Impossivel calcular')
