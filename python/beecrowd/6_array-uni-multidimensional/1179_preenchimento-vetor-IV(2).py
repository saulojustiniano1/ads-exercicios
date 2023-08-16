lista_par = []
lista_impar = []
contador = 0
aux_par = 0
aux_impar = 0

while contador < 15:
    valor = int(input())

    if valor % 2 == 0:
        lista_par.append(valor)
        aux_par += 1

    if valor % 2 != 0:
        lista_impar.append(valor)
        aux_impar += 1

    if aux_par > 4:

        for c in range(0, 5):
            print(f'par[{c}] = {lista_par[c]}')
        lista_par = []
        aux_par = 0

    if aux_impar > 4:

        for c in range(0, 5):
            print(f'impar[{c}] = {lista_impar[c]}')
        lista_impar = []
        aux_impar = 0

    contador += 1

if aux_impar > 0:
    for j in range(aux_impar):
        print(f'impar[{j}] = {lista_impar[j]}')

if aux_par > 0:
    for h in range(aux_par):
        print(f'par[{h}] = {lista_par[h]}')
