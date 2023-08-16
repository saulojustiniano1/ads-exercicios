valor = int(input())

total_cobaias = 0
total_coelhos = 0
total_ratos = 0
total_sapos = 0

for i in range(1, valor+1):
  numero_cobaias, tipo_cobaias = input().split()

  numero_cobaias = int(numero_cobaias)
  tipo_cobaias = str(tipo_cobaias)

  total_cobaias += numero_cobaias

  if tipo_cobaias in ['c', 'C']:
    total_coelhos += numero_cobaias
  elif tipo_cobaias in ['r', 'R']:
    total_ratos += numero_cobaias
  elif tipo_cobaias in ['s', 'S']:
    total_sapos += numero_cobaias
  
percentual_coelhos = (total_coelhos * 100) / total_cobaias
percentual_ratos = (total_ratos * 100) / total_cobaias
percentual_sapos = (total_sapos * 100) / total_cobaias

print(f'Total: {total_cobaias} cobaias')
print(f'Total de coelhos: {total_coelhos}')
print(f'Total de ratos: {total_ratos}')
print(f'Total de sapos: {total_sapos}')
print(f'Percentual de coelhos: {percentual_coelhos:.2f} %')
print(f'Percentual de ratos: {percentual_ratos:.2f} %')
print(f'Percentual de sapos: {percentual_sapos:.2f} %')
