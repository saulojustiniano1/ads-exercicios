numero_1 = int(input())
numero_2 = int(input())

if numero_1 > numero_2:
  maior = numero_1
  menor = numero_2
else:
  maior = numero_2
  menor = numero_2

soma_impares = 0

for valor in range(menor+1, maior):

  if valor % 2 != 0:
    soma_impares += valor

print(soma_impares)
