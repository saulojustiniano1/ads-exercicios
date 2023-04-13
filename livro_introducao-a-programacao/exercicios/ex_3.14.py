# Exercício 3.14 - Escreva um programa que pergunte a quantidade de km percorridos
# por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais
# o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por
# dia e R$ 0,15 por km rodado.

quantidade_de_km_percorrido_do_carro = float(input('Informe a quantidade percorrida do carro alugado (em km): '))
quantidade_dias_que_o_carro_foi_alugado = int(input('Informe quantos dias o carro foi alugado: '))

preco_a_pagar = (quantidade_de_km_percorrido_do_carro * 0.15) + (quantidade_de_km_percorrido_do_carro * 60)

print(f'O carro alugado percorreu {quantidade_de_km_percorrido_do_carro}km e foi alugado por {quantidade_dias_que_o_carro_foi_alugado} dias, valor total a se pagar pelo serviço é de R${preco_a_pagar}')
