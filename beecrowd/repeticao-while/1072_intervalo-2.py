valor = int(input())

contador = 1
dentro = 0
fora = 0

while contador <= valor:
  numero = int(input())

  contador += 1

  if numero >= 10 and numero <= 20:
    dentro += 1
  else:
    fora += 1

print(f'{dentro} in')
print(f'{fora} out')
