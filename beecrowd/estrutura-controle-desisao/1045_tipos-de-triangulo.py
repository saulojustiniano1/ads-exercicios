valores = input().split()

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

lista = [a, b, c]
lista.sort(reverse=True)
a = lista[0]
b = lista[1]
c = lista[2]

if a >= b + c:
  print('NAO FORMA TRIANGULO')
elif (a ** 2) == (b ** 2) + (c ** 2):
  print('TRIANGULO RETANGULO')
elif (a ** 2) > (b ** 2) + (c ** 2):
  print('TRIANGULO OBTUSANGULO')
  if a == b == c:
    print('TRIANGULO EQUILATERO')
  elif a == b or b == c or c == a:
    print('TRIANGULO ISOSCELES')
elif (a ** 2) < (b ** 2) + (c ** 2):
  print('TRIANGULO ACUTANGULO')
  if a == b == c:
    print('TRIANGULO EQUILATERO')
  elif a == b or b == c or c == a:
    print('TRIANGULO ISOSCELES')
