matriz = []
letra = input().upper()

for i in range(12):
    matriz.append([])

    for j in range(12):
        valor = float(input())
        matriz[i].append(valor)

contador = 0
contador_2 = 0
soma = 0

for i in range(11, 0, -1):
    contador_2 += 1
    for j in range(contador_2, 12):
        soma += matriz[i][j]
        contador += 1

if letra == 'S':
    print('{}'.format(soma))

if letra == 'M':
    media = soma / contador
    print('{:.1f}'.format(media))
