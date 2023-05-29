def calc_diferenca(valor1, valor2, valor3, valor4):
  prod_ab = valor1 * valor2
  prod_cd = valor3 * valor4

  diferenca = prod_ab - prod_cd

  return diferenca

numero_1 = int(input())
numero_2 = int(input())
numero_3 = int(input())
numero_4 = int(input())

print(f'DIFERENCA = {calc_diferenca(numero_1, numero_2, numero_3, numero_4)}')
