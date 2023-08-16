i = 1
j = 7
c = 0

while True:
  if c < 3:
    print(f'I={i} J={j}')
    j -= 1
    c += 1
  if c == 3:
    c1 = 0
    continue
  if c1 < 3:
    j = 7
    i = 3
    print(f'I={i} J={j}')
    c1 -= 1


    