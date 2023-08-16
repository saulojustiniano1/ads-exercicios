i = 0
j = 1
c = 0
aux_i = i
aux_j = j

while i <= 2 and j <= 5:
  while c < 3:
    if i in [0, 1] or i > 1.8:
      print(f'I={i:.0f} J={j:.0f}')
    else:
      print(f'I={i:.1f} J={j:.1f}')
    c += 1
    j += 1

  if j >= 4:
    c = 0
    i = aux_i
    j = aux_j
    i += 0.2
    j += 0.2
    aux_i = i
    aux_j = j
  