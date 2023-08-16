valor = int(input())

for numero in range(1, valor+1):
  if numero % 2 == 0:
    print(f'{numero}^2 = {numero**2}')
