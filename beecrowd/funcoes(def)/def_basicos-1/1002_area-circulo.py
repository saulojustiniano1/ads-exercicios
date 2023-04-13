raio = float(input())

def calc_area(raio):
  pi = 3.14159
  return pi * (raio ** 2)

area = calc_area(raio)

print(f'A={area:.4f}')
