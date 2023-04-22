i = 0
j = 1
aux_i = i
aux_j = j

while i <= 2 and j <= 5:
  print(f'I={round(i, 1)} J={round(j, 1)}')
  j += 1

  if j >= 4:
    i = aux_i
    j = aux_j
    i += 0.2
    j += 0.2
    aux_i = i
    aux_j = j

