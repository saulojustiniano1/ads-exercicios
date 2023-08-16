valor = int(input())
contador = 0

for i in range(1000):
    print(f'N[{i}] = {contador}')
    contador += 1
    if valor <= contador:
        contador = 0
