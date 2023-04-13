nome_do_vendedor = str(input())
salario_fixo = float(input())
total_de_vendas_efetuadas_por_mes = float(input())

salario_total = salario_fixo + (total_de_vendas_efetuadas_por_mes * 15 / 100)

print(f'TOTAL = R$ {salario_total:.2f}')
