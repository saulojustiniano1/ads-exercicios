coluna = int(input())
opcao = input().upper()

matriz = []

for i in range(12):
    matriz.append([])

for i in range(12):
    for j in range(12):
        valor = float(input())
        matriz[i].append(valor)


if opcao == 'S':
    soma = 0

    for k in range(12):
        soma = soma + matriz[k][coluna]

    print(soma)

if opcao == 'M':
    media = 0
    soma = 0

    for k in range(12):
        soma = soma + matriz[k][coluna]

    media = soma / 12

    print(f'{media:.1f}')
