valor = float(input())

nota100 = int(valor // 100)
valor = float(valor % 100)

nota50 = int(valor // 50)
valor = float(valor % 50)

nota20 = int(valor // 20)
valor = float(valor % 20)

nota10 = int(valor) // 10
valor = float(valor % 10)

nota5 = int(valor) // 5
valor = float(valor % 5)

nota2 = int(valor // 2)
valor = float(valor % 2)

moeda1 = int(valor // 1)
valor = float(valor % 1)

moeda050 = int(valor // 0.50)
valor = float(valor % 0.50)

moeda025 = int(valor // 0.25)
valor = float(valor % 0.25)

moeda010 = int(valor // 0.10)
valor = float(valor % 0.10)

moeda005 = int(valor // 0.05)
valor = float(valor % 0.05)

moeda001 = int(round(valor / 0.01))

print('NOTAS:')
print(f'{nota100} nota(s) de R$ 100.00')
print(f'{nota50} nota(s) de R$ 50.00')
print(f'{nota20} nota(s) de R$ 20.00')
print(f'{nota10} nota(s) de R$ 10.00')
print(f'{nota5} nota(s) de R$ 5.00')
print(f'{nota2} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{moeda1} moeda(s) de R$ 1.00')
print(f'{moeda050} moeda(s) de R$ 0.50')
print(f'{moeda025} moeda(s) de R$ 0.25')
print(f'{moeda010} moeda(s) de R$ 0.10')
print(f'{moeda005} moeda(s) de R$ 0.05')
print(f'{moeda001} moeda(s) de R$ 0.01')
