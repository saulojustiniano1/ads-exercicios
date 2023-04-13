numero = int(input())

if numero not in [61, 71, 11, 21, 32, 19, 27, 31]:
  messagem = 'DDD nao cadastrado'
else:
  if numero == 61:
    messagem = 'Brasilia'
  elif numero == 71:
    messagem = 'Salvador'
  elif numero == 11:
    print('Sao Paulo')
  elif numero == 21:
    messagem = 'Rio de Janeiro'
  elif numero == 32:
    messagem = 'Juiz de Fora'
  elif numero == 19:
    messagem = 'Campinas'
  elif numero == 27:
    messagem = 'Vitoria'
  elif numero == 31:
    messagem = 'Belo Horizonte'

print(messagem)
