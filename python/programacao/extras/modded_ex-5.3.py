from time import sleep

contador = 10

while contador >= 0:
    print(f'{contador}', end=' ', flush=True)
    sleep(1)

    contador -= 1

print('\nFogo!')
