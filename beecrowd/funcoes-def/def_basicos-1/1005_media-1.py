def calc_media(nota1, nota2):
  peso_1 = 3.5
  peso_2 = 7.5

  media = ((nota1 * peso_1) + (nota2 * peso_2)) / (peso_1 + peso_2)

  return media

nota_1 = float(input())
nota_2 = float(input())

print(f'MEDIA = {calc_media(nota_1, nota_2):.5f}')
