salario = float(input())

if salario >= 0 and salario <= 2000:
  print('Isento')

elif salario > 2000 and salario <= 3000:
  imposto_de_renda = (salario - 2000) * 0.08
  print(f'R$ {imposto_de_renda:.2f}')

elif salario > 3000 and salario <= 4500:
  imposto18 = (salario - 3000) * 0.18
  imposto8 =  (((salario - (salario - 3000)) - 2000)) * 0.08
  imposto_de_renda = imposto8 + imposto18
  print(f'R$ {imposto_de_renda:.2f}')

elif salario > 4500:
  imposto28 = (salario - 4500) * 0.28
  imposto18 = (((salario - ((salario - 4500))) - 3000)) * 0.18
  imposto8 = ((((salario - ((salario - 4500))) - (((salario - ((salario - 4500))) - 3000))) - 2000)) * 0.08
  imposto_de_renda = imposto28 + imposto18 + imposto8
  print(f'R$ {imposto_de_renda:.2f}')
