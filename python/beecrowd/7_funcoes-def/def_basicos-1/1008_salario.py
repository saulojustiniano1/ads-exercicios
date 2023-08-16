def calc_salario(horas_trabalhadas, valor_das_horas):
  salario = horas_trabalhadas * valor_das_horas

  return salario

numero_funcionario = int(input())
horas_trabalhadas = int(input())
valor_das_horas = float(input())

print(
  f'NUMBER = {numero_funcionario}\n'
  f'SALARY = U$ {calc_salario(horas_trabalhadas, valor_das_horas):.2f}'
)
