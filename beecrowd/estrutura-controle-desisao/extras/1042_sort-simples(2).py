a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if a > b and a > c:
  if b > c:
    menor = c
    meio = b
    maior = a
  else:
    menor = b
    meio = c
    maior = a
elif b > a and b > c:
  if a > c:
    menor = c
    meio = a
    maior = b
  else:
    menor = a
    meio = c
    maior = b
elif c > a and c > b:
  if a > b:
    menor = b
    meio = a
    maior = c
  else:
    menor = a
    meio = b
    maior = c

print(menor)
print(meio)
print(maior)
print()
print(a)
print(b)
print(c)
