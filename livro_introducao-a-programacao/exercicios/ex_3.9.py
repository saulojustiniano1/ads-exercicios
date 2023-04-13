# Exercício 3.9 - Escreva um programa que leia a quantidade de dias, horas, minutos e
# segundos do usuário. Calcule o total em segundos.

quantidade_de_dias = int(input('Informe a quantidade de dias: '))
quantidade_de_horas = int(input('Informe a quantidade de horas (entre 0 e 23): '))
quantidade_de_minutos = int(input('Informe a quantidade de minutos (entre 0 e 59): '))
quantidade_de_segundos = int(input('Informe a quantidade de segundos (entre 0 e 59): '))

total_de_segundos = (quantidade_de_dias * 24 * 60 * 60) + (quantidade_de_horas * 60 * 60) + (quantidade_de_minutos * 60) + quantidade_de_segundos

print(f'A quantidade de total de segundos de {quantidade_de_dias} dias, {quantidade_de_horas} horas, {quantidade_de_minutos} minutos e {quantidade_de_segundos} segundos foi de {total_de_segundos} segundos')
