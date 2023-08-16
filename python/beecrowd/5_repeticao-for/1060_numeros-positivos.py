positivos = 0

for i in range(1, 7):
  numero = float(input())
  
  if numero > 0:
    positivos += 1

print(f'{positivos} valores positivos')
