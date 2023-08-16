valor = int(input())
lista = input().split()
nova_lista = []
menor = 1
contador = 0

for i in range(len(lista)):
    nova_lista.append(int(lista[i]))

for i in nova_lista:
    if i < menor:
        menor = i
        posicao = contador
    contador += 1

print(f'Menor valor: {menor}')
print(f'Posicao: {posicao}')
