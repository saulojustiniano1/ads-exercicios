opcao = str(input()).upper()
matriz = []

for i in range(12):
    matriz.append([])

    for j in range(12):
        valor = float(input())
        matriz[i].append(valor)

if opcao == 'S':
    soma = 0
    contador = 1
    for i in range(0, 11):
        for j in range(contador, 12):
            # print('m[{}][{}]'.format(i,j))
            soma = soma + matriz[i][j]
        contador += 1
    print('{:.1f}'.format(soma))

if opcao == 'M':
    soma = 0
    contador = 1
    contador_2 = 0
    for i in range(0, 11):
        for j in range(contador, 12):
            # print('m[{}][{}]'.format(i,j))
            soma = soma + matriz[i][j]
            contador_2 += 1
        contador += 1

    media = soma / (contador_2)
    print('{:.1f}'.format(media))
