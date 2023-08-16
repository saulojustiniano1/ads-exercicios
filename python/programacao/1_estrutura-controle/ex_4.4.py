# Exercício 4.4 - Escreva um programa que pergunte o salário do funcionário e calcule
# o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de
# 10%. Para os inferiores ou iguais, de 15%.

salario_do_funcionario = float(input('Informe o salário do funcionário: R$'))

if salario_do_funcionario > 1250:
  aumento = salario_do_funcionario * 0.15
  salario_novo = salario_do_funcionario + aumento
if salario_do_funcionario <= 1250:
  aumento = salario_do_funcionario * 0.10
  salario_novo = salario_do_funcionario + aumento

print(f'O funcionário tinha um salário de R${salario_do_funcionario:.2f} com o aumento de R${aumento:.2f} ele vai passar a ganhar R${salario_novo:.2f}')
