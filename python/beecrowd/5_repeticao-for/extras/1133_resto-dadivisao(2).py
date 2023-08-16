numero_1 = int(input())
numero_2 = int(input())

for valor in range(numero_1+1, numero_2):
  if valor % 5 == 2 or valor % 5 == 3:
    print(valor)
