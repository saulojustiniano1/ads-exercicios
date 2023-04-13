# Exercício 4.8 Escreva um programa que leia dois números e que pergunte qual
# operação você deseja realizar. Você deve poder calcular soma (+), subtração (-),
# mu ltiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.

numero_1 = int(input('Informe um número: '))
numero_2 = int(input('Informe outro número: '))

opcao = str(input('Qual operação você deseja realizar (+), (-), (*), (/): '))

if opcao == '+':
  soma = numero_1 + numero_2
  messagem = f'{numero_1} + {numero_2} = {soma}'
elif opcao == '-':
  subtracao = numero_1 - numero_2
  messagem = f'{numero_1} - {numero_2} = {subtracao}'
elif opcao == '*':
  multiplicacao = numero_1 * numero_2
  messagem = f'{numero_1} x {numero_2} = {multiplicacao}'
elif opcao == '/':
  divisao = numero_1 / numero_2
  messagem = f'{numero_1} / {numero_2} = {divisao}'

print(messagem)
