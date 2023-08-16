# Exercício 3.15 - Escreva um programa para calcular a redução do tempo de vida de um fumante. 
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
# Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de 
# vida um fumante perderá. Exiba o total em dias.

quantidade_de_cigarro_por_dia = int(input('Quantos cigarros você fuma por dia? '))
quantos_anos_fumou = int(input('Há quantos anos você fuma? '))

total_de_cigarros = quantidade_de_cigarro_por_dia * quantos_anos_fumou * 365
total_minutos_fumando = total_de_cigarros * 10
total_dias_perdidos = total_minutos_fumando / 24 / 60

print(f'Você perdeu aproximadamente {total_dias_perdidos:.2f} dias de vida fumando, PARE DE FUMAR!!!')
