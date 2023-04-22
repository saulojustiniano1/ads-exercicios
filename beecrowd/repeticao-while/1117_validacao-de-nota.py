contador = 0
soma_nota = 0

while contador < 2:
  nota = float(input())

  if nota >= 0 and nota <= 10:
    soma_nota += nota
    contador += 1

  else:
    print('nota invalida')
  
media = soma_nota / contador

print(f'media = {media:.2f}')
