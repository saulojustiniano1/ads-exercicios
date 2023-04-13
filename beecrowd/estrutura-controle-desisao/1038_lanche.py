valores = input().split()

cod_item = int(valores[0])
quant_item = int(valores[1])

if cod_item == 1:
  pagar = quant_item * 4.00
elif cod_item == 2:
  pagar = quant_item * 4.50
elif cod_item == 3:
  pagar = quant_item * 5.00
elif cod_item == 4:
  pagar = quant_item * 2.00
elif cod_item == 5:
  pagar = quant_item * 1.50

print(f'Total: R$ {pagar:.2f}')
