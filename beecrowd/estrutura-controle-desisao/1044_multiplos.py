valores = input().split()

a = int(valores[0])
b = int(valores[1])

if a > b:
  maior = a
else:
  maior = b

if a < b:
  menor = a
else:
  menor = b

if maior % menor == 0:
  print('Sao Multiplos')
else:
  print('Nao sao Multiplos')
