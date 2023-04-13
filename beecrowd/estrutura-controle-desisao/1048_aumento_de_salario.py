salario = float(input())

if salario >= 0 and salario <= 400:
  reajuste = salario * 0.15
  novo_salario = salario + reajuste
  percentual = 15
elif salario > 400 and salario <= 800:
  reajuste = salario * 0.12
  novo_salario = salario + reajuste
  percentual = 12
elif salario > 800 and salario <= 1200:
  reajuste = salario * 0.10
  novo_salario = salario + reajuste
  percentual = 10
elif salario > 1200 and salario <= 2000:
  reajuste = salario * 0.07
  novo_salario = salario + reajuste
  percentual = 7
elif salario > 2000:
  reajuste = salario * 0.04
  novo_salario = salario + reajuste
  percentual = 4

print(f'Novo salario: {novo_salario:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {percentual} %')
