i = 1
j = 7
aux = j

while j >= 5 and i < 10:
  print(f'I={i} J={j}')
  j -= 1

  if j <= 4 or i >= 3 and j <= 6 or i >= 5 and j <= 8 or i >= 7 and j <= 10 or i >= 9 and j <= 12:
    j = aux
    j += 2
    i += 2
    aux = j
