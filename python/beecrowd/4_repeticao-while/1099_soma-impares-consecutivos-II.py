contador = int(input())

while contador > 0:
  valor_x, valor_y = map(int, input().split())

  soma_impar = 0

  if valor_x > valor_y:
    maior = valor_x
    menor = valor_y
  else:
    maior = valor_y
    menor = valor_x

  while menor < maior:
    maior -= 1
    if menor < maior:
      if maior % 2 != 0:
        soma_impar += maior
  
  contador -= 1

  print(soma_impar)
