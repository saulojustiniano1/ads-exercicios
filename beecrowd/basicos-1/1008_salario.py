numero_do_funcionario = int(input())
numero_de_horas_trabalhadas = int(input())
valor_por_horas_trabalhadas = float(input())

salario = numero_de_horas_trabalhadas * valor_por_horas_trabalhadas

print(f'NUMBER = {numero_do_funcionario}')
print(f'SALARY = U$ {salario:.2f}')
