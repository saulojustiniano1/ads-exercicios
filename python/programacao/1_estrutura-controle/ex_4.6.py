# Exercício 4.6 - Escreva um programa que pergunte a distância que um passageiro
# deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km
# para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.

distancia_a_pecorrer = float(input('Qual é a distância que o passageiro desejar percorrer: '))

if distancia_a_pecorrer <= 200:
  valor_da_passagem = distancia_a_pecorrer * 0.50
else:
  valor_da_passagem = distancia_a_pecorrer * 0.45

messagem = f'Sua viagem foi de {distancia_a_pecorrer}km e você pagará o valor de R${valor_da_passagem}'

print(messagem)
