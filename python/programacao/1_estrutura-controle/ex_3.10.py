# Exercício 3.10 - Faça um programa que calcule o aumento de um salário. Ele deve
# solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento
# e do novo salário.

salario_atual = float(input('Informe seu salário atual: R$'))
valor_do_aumento_em_porcentagem = int(input('Informe a porcentagem que você quer ganhar de aumento(em %): '))

salario_com_aumento = salario_atual + (salario_atual * valor_do_aumento_em_porcentagem / 100)

print(f'Seu salário atual era de R${salario_atual:.2f} com o aumento de {valor_do_aumento_em_porcentagem}% vai passar a ser R${salario_com_aumento:.2f}')
