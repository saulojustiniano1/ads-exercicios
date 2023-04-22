numero_1 = int(input('Número 1: '))
numero_2 = int(input('Número 2: '))

mult = 0
contador = 1

while contador <= numero_2:
  mult += numero_1

  contador += 1
  
print(f'{numero_1} x {numero_2} = {mult}')
