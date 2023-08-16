opcao = str(input()).upper()
matriz = []

for i in range(12):
    matriz.append([])
    for j in range(12):
        valor = float(input())
        matriz[i].append(valor)

contador = 12
soma = 0
contador_2 = 0
for i in range(11):
    contador -= 1
    for j in range(contador):
        soma += matriz[i][j]
        contador_2 += 1

if opcao == 'S':
    print('{}'.format(soma))

if opcao == 'M':
    media = soma / contador_2
    print('{:.1f}'.format(media))
