# Exercício 3.12 - Escreva um programa que calcule o tempo de uma viagem de carro.
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia_a_percorrer = float(input('Qual a distância da viagem (em KM): '))
velocidade_media = int(input('Qual foi a velocidade média da viagem (em KM): '))

tempo_da_viagem_horas = distancia_a_percorrer / velocidade_media

print(f'A viagem de carro vai durar aproximadamente {tempo_da_viagem_horas:.1f} horas')
