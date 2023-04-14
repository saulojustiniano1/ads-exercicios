contador = 1
soma_valor = 0
numero_positivo = 0

while contador <= 6:
  valor = float(input())

  if valor > 0:
    numero_positivo += 1
    soma_valor += valor

  contador += 1

media = soma_valor / numero_positivo

print(f'{numero_positivo} valores positivos')
print(f'{media:.1f}')
