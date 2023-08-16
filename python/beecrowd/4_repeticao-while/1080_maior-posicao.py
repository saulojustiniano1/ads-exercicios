contador = 0
maior = 0
posicao_maior = 0

while contador < 100:
  valor = int(input())

  contador += 1
  
  if valor > maior:
    maior = valor
    posicao_maior = contador

print(maior)
print(posicao_maior)
