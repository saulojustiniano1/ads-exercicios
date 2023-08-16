pares = 0

for i in range(1, 6):
  numero = float(input())

  if numero % 2 == 0:
    pares += 1

print(f'{pares} valores pares')
