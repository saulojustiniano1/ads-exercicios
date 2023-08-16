opcao = str(input()).upper()
matriz = []

for i in range(12):
    matriz.append([])

    for j in range(12):
        valor = float(input())
        matriz[i].append(valor)

if opcao == 'S':
    soma = 0
    contador = 11
    for i in range(11, 0, -1):
        for j in range(0, contador):
            # print('m[{}][{}]'.format(i,j))
            s = s + matriz[i][j]
        contador -= 1
    print('{:.1f}'.format(soma))

if opcao == 'M':
    soma = 0
    contador = 11
    contador_2 = 0
    for i in range(11, 0, -1):
        for j in range(0, contador):
            # print('m[{}][{}]'.format(i,j))
            soma = soma + matriz[i][j]
            contador_2 += 1
        contador -= 1

    media = soma / (contador_2)
    print('{:.1f}'.format(media))
