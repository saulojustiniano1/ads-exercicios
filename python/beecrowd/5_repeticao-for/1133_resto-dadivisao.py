numero_1 = int(input())
numero_2 = int(input())

if numero_1 > numero_2:
  maior = numero_1
  menor = numero_2
else:
  maior = numero_2
  menor = numero_1

for valor in range(menor+1, maior):
  if valor % 5 == 2 or valor % 5 == 3:
    print(valor)
