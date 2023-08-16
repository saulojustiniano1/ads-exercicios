valor = int(input())

cedula100 = valor // 100
valor_restante = valor % 100

cedula50 = valor_restante // 50
valor_restante = valor_restante % 50

cedula20 = valor_restante // 20
valor_restante = valor_restante % 20

cedula10 = valor_restante // 10
valor_restante = valor_restante % 10

cedula5 = valor_restante // 5
valor_restante = valor_restante % 5

cedula2 = valor_restante // 2
valor_restante = valor_restante % 2

cedula1 = valor_restante

print(valor)
print(f'{cedula100} nota(s) de R$ 100,00')
print(f'{cedula50} nota(s) de R$ 50,00')
print(f'{cedula20} nota(s) de R$ 20,00')
print(f'{cedula10} nota(s) de R$ 10,00')
print(f'{cedula5} nota(s) de R$ 5,00')
print(f'{cedula2} nota(s) de R$ 2,00')
print(f'{cedula1} nota(s) de R$ 1,00')
