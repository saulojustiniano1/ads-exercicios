# Exercício 4.9 - Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. 
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. 
# O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação 
# como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

valor_da_casa = float(input('Informe o valor da casa que você deseja fazer o empréstimo: R$'))
salario_da_pessoa = float(input('Informe quanto você ganhar: R$'))
quantidade_de_anos_a_pagar = int(input('Em quantos anos você deseja pagar: '))

prestacao_mensal_da_casa = valor_da_casa / (quantidade_de_anos_a_pagar * 12)

salario_30 = salario_da_pessoa * 0.3

if salario_30 > prestacao_mensal_da_casa:
  print(f"""
Seu salário é de R${salario_da_pessoa:.2f} com {quantidade_de_anos_a_pagar} anos de prestação da casa você vai pagar R${prestacao_mensal_da_casa:.2f} por mês\n
O valor da prestação mensal não pode ser superior a 30% do salário, VALOR DE 30% DO SALÁRIO R${salario_30:.2f}\n
VOCÊ FOI APROVADO PARA FAZER O EMPRÉSTIMO!
""")
else:
  print(f"""
Seu salário é de R${salario_da_pessoa:.2f} com {quantidade_de_anos_a_pagar} anos de prestação da casa você vai pagar R${prestacao_mensal_da_casa:.2f} por mês\n
O valor da prestação mensal não pode ser superior a 30% do salário, VALOR DE 30% DO SALÁRIO R${salario_30:.2f}\n
VOCÊ FOI NEGADO PARA FAZER O EMPRÉSTIMO!
""")
