lista_par = []
lista_impar = []
aux_par = 0
aux_impar = 0

for valor in range(15):
    numero = int(input())

    if numero % 2 == 0:
        lista_par.append(numero)
    if numero % 2 != 0:
        lista_impar.append(numero)

for p in lista_par:
    print(f'par[{aux_par}] = {p}')
    aux_par += 1
    if aux_par > 4:
        aux_par = 0

for i in lista_impar:
    print(f'impar[{aux_impar}] = {i}')
    aux_impar += 1
    if aux_impar > 4:
        aux_impar = 0
