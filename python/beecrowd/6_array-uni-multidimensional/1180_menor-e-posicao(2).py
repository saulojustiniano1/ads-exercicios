valor = int(input())

lista = input()

lista = lista.split()

for i in range(len(lista)):
    lista[i] = int(lista[i])

menor = lista[0]
posicao = 0

for j in range(1, len(lista)):
    if lista[j] < menor:
        menor = lista[j]
        posicao = j

print(f'Menor valor: {menor}')
print(f'Posicao: {posicao}')
