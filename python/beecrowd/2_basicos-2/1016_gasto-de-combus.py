tempo_gasto_na_viagem = int(input())
velocidade_media = int(input())

distancia_percorrida = tempo_gasto_na_viagem * velocidade_media

quantidade_de_litros_necessario = distancia_percorrida / 12

print(f'{quantidade_de_litros_necessario:.3f}')
