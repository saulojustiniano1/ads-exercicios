def calc_area(raio):
  pi = 3.14159
  area =  pi * (raio ** 2)

  return area

raio = float(input())

print(f'A={calc_area(raio):.4f}')
