linha = int(input())
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

    for k in matriz[linha]:
        soma = soma + k

    print(soma)

if opcao == 'M':
    media = 0
    soma = 0

    for k in matriz[linha]:
        soma = soma + k

    media = soma / 12

    print(media)
