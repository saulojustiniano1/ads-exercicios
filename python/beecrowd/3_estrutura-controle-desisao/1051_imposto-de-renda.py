salario = float(input())

isento =  2000

if salario >= 0 and salario <= isento:
  print('Isento')

elif salario > 2000 and salario <= 3000:
  calc8 = salario - isento
  imposto_de_renda = calc8 * 0.08
  print(f'R$ {imposto_de_renda:.2f}')

elif salario > 3000 and salario <= 4500:
  calc_18 = salario - 3000
  imposto18 = calc_18 * 0.18
  calc_8 = ((salario - calc_18) - isento)
  imposto8 =  calc_8 * 0.08
  imposto_de_renda = imposto8 + imposto18
  print(f'R$ {imposto_de_renda:.2f}')

elif salario > 4500:
  calc28 = salario - 4500
  imposto28 = calc28 * 0.28
  calc18 = ((salario - calc28) - 3000)
  imposto18 = calc18 * 0.18
  calc8 = (((salario - calc28) - calc18) - isento)
  imposto8 = calc8 * 0.08
  imposto_de_renda = imposto28 + imposto18 + imposto8
  print(f'R$ {imposto_de_renda:.2f}')
