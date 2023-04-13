notas = input().split()

n1 = float(notas[0])
n2 = float(notas[1])
n3 = float(notas[2])
n4 = float(notas[3])

media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / (2 + 3 + 4 + 1)

if media >= 7:
  print(f'Media: {media:.1f}')
  print('Aluno aprovado.')
elif media >= 5 and media <= 6.9:
  nota_final = float(input())
  media_final = (nota_final + media) / 2
  print(f'Media: {media:.1f}')
  print('Aluno em exame.')
  print(f'Nota do exame: {nota_final:.1f}')
  if media_final >= 5:
    print('Aluno aprovado.')
  else:
    print('Aluno reprovado.')
  print(f'Media final: {media_final:.1f}')
elif media < 5:
  print(f'Media: {media:.1f}')
  print('Aluno reprovado.')
