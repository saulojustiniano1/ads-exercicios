# Exercício 4.3 - Escreva um programa que leia três números e que imprima o maior e o menor.

numero_1 = int(input('Informe um número: '))
numero_2 = int(input('Informe outro número: '))
numero_3 = int(input('Informe mais um número: '))

if numero_1 > numero_2 and numero_1 > numero_3:
  if numero_2 > numero_3:
    maior = numero_1
    menor = numero_3
  if numero_3 > numero_2:
    maior = numero_1
    menor = numero_2
if numero_2 > numero_1 and numero_2 > numero_3:
  if numero_1 > numero_3:
    maior = numero_2
    menor = numero_3
  if numero_3 > numero_1:
    maior = numero_2
    menor = numero_1
if numero_3 > numero_1 and numero_3 > numero_2:
  if numero_1 > numero_2:
    maior = numero_3
    menor = numero_2
  if numero_2 > numero_1:
    maior = numero_3
    menor = numero_1

print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')
