def calc_media(nota1, nota2, nota3):
  peso1 = 2
  peso2 = 3
  peso3 = 5

  media = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)

  return media

nota_1 = float(input())
nota_2 = float(input())
nota_3 = float(input())

print(f'MEDIA = {calc_media(nota_1, nota_2, nota_3):.1f}')
