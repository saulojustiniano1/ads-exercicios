valores_1 = input().split()
valores_2 = input().split()

x1 = float(valores_1[0])
y1 = float(valores_1[1])

x2 = float(valores_2[0])
y2 = float(valores_2[1])

distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(f'{distancia:.4f}')
