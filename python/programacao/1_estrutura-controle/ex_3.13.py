# Exercício 3.13 - Escreva um programa que converta uma temperatura digitada em
# ºC em ºF. A fórmula para essa conversão é:
#                  9 x C
#              F= ------- + 32
#                    5

celsius = float(input('Digite a temperatura em Celsius(ºC) para converter a fahrenheit(ºF): '))

fahrenheit = ((9 * celsius) / 5) + 32

print(f'A temperatura em celsius é {celsius}C convertido em fahrenheit fica de {fahrenheit:.1f}F')
