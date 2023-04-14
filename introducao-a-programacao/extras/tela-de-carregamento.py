# Programa da barra de carregemento simples

from os import system
from time import sleep

caracter = '#'
contador = 1

while contador <= 100:
  system('clear')
  print(f'{caracter} {contador}%', end='', flush=True)
  sleep(0.1)

  caracter += '#'
  contador += 1

print('\nDownload Carregado!')
