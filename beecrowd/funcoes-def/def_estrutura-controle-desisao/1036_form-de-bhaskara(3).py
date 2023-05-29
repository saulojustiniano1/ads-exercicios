a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

def calc_delta(a, b, c):
  delta = (b ** 2) - (4 * a * c)
  return delta

def calc_bhaskara(a, b, delta):
  if delta > 0:
    x1 = (- b + (delta ** 0.5)) / (2 * a)
    x2 = (- b - (delta ** 0.5)) / (2 * a)
    return x1, x2
  else:
    print('Impossivel calcular')

def imprimir(a, b, c):
  x1, x2 = calc_bhaskara(a, b, c)
  if a != 0:
    if x1 == x2:
      print(f'R = {x1}')
    else:
      print(f'R1 = {x1}')
      print(f'R2 = {x2}')
  else:
    print('Impossivel calcular')


def main(a, b, c):
  imprimir(a, b, c)

