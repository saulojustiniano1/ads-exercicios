valores = input().split()

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

if (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
  perimetro = a + b + c
  print(f'Perimetro = {perimetro}')
else:
  area = ((a + b) * c) / 2
  print(f'Area = {area}')
