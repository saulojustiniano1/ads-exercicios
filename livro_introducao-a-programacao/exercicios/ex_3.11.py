# Exercício 3.11 - Faça um programa que solicite o preço de uma mercadoria e o per-
# centual de desconto. Exiba o valor do desconto e o preço a pagar.

preco_da_mercadoria = float(input('Informe o preço da mercadoria: R$'))
percentual_de_desconto = int(input('Qual o percentual de desconto do produto (em %): '))

preco_da_mercadoria_com_desconto = preco_da_mercadoria - (preco_da_mercadoria * percentual_de_desconto / 100)

print(f'A mercadoria era R${preco_da_mercadoria:.2f} com o desconto de {percentual_de_desconto}% o produto vai passar a ser R${preco_da_mercadoria_com_desconto:.2f}')
