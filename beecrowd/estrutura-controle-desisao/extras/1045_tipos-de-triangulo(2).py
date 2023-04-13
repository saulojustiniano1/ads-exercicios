a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

if a >= b and a >= c:
  if b >= c:
    menor = c
    meio = b
    maior = a
  else:
    menor = b
    meio = c
    maior = a
elif b >= a and b >= c:
  if a >= c:
    menor = c
    meio = a
    maior = b
  else:
    menor = a
    meio = c
    maior = b
elif c >= a and c >= b:
  if a >= b:
    menor = b
    meio = a
    maior = c
  else:
    menor = a
    meio = b
    maior = c

if maior >= meio + menor:
  print('NAO FORMA TRIANGULO')
elif (maior ** 2) == (meio ** 2) + (menor ** 2):
  print('TRIANGULO RETANGULO')
elif (maior ** 2) > (meio ** 2) + (menor ** 2):
  print('TRIANGULO OBTUSANGULO')
  if maior == meio == menor:
    print('TRIANGULO EQUILATERO')
  elif maior == meio or meio == menor or menor == a:
    print('TRIANGULO ISOSCELES')
elif (maior ** 2) < (meio ** 2) + (menor ** 2):
  print('TRIANGULO ACUTANGULO')
  if maior == meio == menor:
    print('TRIANGULO EQUILATERO')
  elif maior == meio or meio == menor or menor == a:
    print('TRIANGULO ISOSCELES')
