valores = input().split()

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

area_do_triangulo_retangulo = (a * c) / 2
area_do_circulo = 3.14159 * (c ** 2)
area_do_trapezio = ((a + b) * c) / 2
area_do_quadrado = b ** 2
area_do_retangulo = a * b

print(f'TRIANGULO: {area_do_triangulo_retangulo:.3f}')
print(f'CIRCULO: {area_do_circulo:.3f}')
print(f'TRAPEZIO: {area_do_trapezio:.3f}')
print(f'QUADRADO: {area_do_quadrado:.3f}')
print(f'RETANGULO: {area_do_retangulo:.3f}')
