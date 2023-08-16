valor = int(input())

for i in range(1, valor+1):
  nota_1, nota_2, nota_3 = map(float, input().split())

  media_ponderada = ((nota_1 * 2) + (nota_2 * 3) + (nota_3 * 5)) / (2 + 3 + 5)

  print(f'{media_ponderada:.1f}')
