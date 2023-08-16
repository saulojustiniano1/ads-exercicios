i = 1
j = 7

while j >= 5 and i < 10:
  print(f'I={i} J={j}')
  j -= 1
  if j <= 4:
    j = 7
    i += 2
