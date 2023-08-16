valor = int(input())

impares = 1

while impares <=6:
  if valor % 2 != 0:
    print(valor)
    impares += 1
    valor += 1
  else:
    valor += 1
      