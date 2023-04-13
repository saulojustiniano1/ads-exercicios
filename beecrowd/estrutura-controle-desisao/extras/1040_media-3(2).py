n1, n2, n3, n4 = map(float, input().split())

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / (2 + 3 + 4 + 1)

if media >= 7:
  mensagem = ('Aluno aprovado.')
elif media >= 5 and media <= 6.9:
  nota_exame = float(input())
  media_final = (media + nota_exame) / 2
  mensagem = ('Aluno em exame.')
  if media_final >= 5.0:
    mensagem_exame = ('Aluno aprovado.')
  else:
    mensagem_exame = ('Aluno reprovado.')
elif media < 5:
  mensagem = ('Aluno reprovado.')

print(f'Media: {media:.1f}')
print(mensagem)
if mensagem == 'Aluno em exame.': 
  print(f'Nota do Exame: {nota_exame:.1f}')
  print(mensagem_exame)
  print(f'Media final: {media_final:.1f}')
