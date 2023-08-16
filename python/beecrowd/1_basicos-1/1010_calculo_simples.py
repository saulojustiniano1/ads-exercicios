peca_1 = input().split()
peca_2 = input().split()

codigo_da_peca_1 = int(peca_1[0])
numero_da_peca_1 = int(peca_1[1])
valor_unitario_1 = float(peca_1[2])

codigo_da_peca_2 = int(peca_2[0])
numero_da_peca_2 = int(peca_2[1])
valor_unitario_2 = float(peca_2[2])

valor_total = (numero_da_peca_1 * valor_unitario_1) + (numero_da_peca_2 * valor_unitario_2)

print(f'VALOR A PAGAR: R$ {valor_total:.2f}')
