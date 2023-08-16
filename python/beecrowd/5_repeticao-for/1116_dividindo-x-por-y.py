valor = int(input())

for i in range(1, valor+1):
  numero_1, numero_2 = map(int, input().split())

  if numero_2 == 0:
    print('divisao impossivel')
  else:
    d = numero_1 / numero_2
    print(d)
