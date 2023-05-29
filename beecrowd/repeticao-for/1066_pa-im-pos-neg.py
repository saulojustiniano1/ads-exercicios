pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(1, 6):
  numero = int(input())

  if numero > 0:
    positivos += 1
    if numero % 2 == 0:
      pares += 1
    elif numero % 2 != 0:
      impares += 1
  elif numero < 0:
    negativos += 1
    if numero % 2 == 0:
      pares += 1
    elif numero % 2 != 0:
      impares += 1
  elif numero == 0:
    pares += 1

print(f'{pares} valor(es) par(es)')
print(f'{impares} valor(es) impar(es)')
print(f'{positivos} valor(es) positivo(s)')
print(f'{negativos} valor(es) negativo(s)')
