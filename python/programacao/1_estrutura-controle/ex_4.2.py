# Exercício 4.2 - Escreva um programa que pergunte a velocidade do carro de um usuário. 
# Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. 
# Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.

velocidade_do_carro = float(input('Informe a velocidade do veiculo (em Km): '))

if velocidade_do_carro > 80:
  multa = (velocidade_do_carro - 80) * 5
  print(f'A velocidade foi {velocidade_do_carro:.2f}KM, seu carro foi MULTADO!!!')
  print(f'A valor da multa é de R${multa:.2f}')

if velocidade_do_carro <= 80:
  print(f'A velocidade é {velocidade_do_carro:.2f}KM, seu carro NÃO foi MULTADO!!!')
