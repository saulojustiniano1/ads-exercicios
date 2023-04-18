while True: 
  x, y = map(int, input().split())

  if x == 0:
    break
  elif y == 0:
    break

  if x > 0 and y > 0:
    print('primeiro')
    continue
  elif x < 0 and y > 0:
    print('segundo')
    continue
  elif x < 0 and y < 0:
    print('terceiro')
    continue
  elif x > 0 and y < 0:
    print('quarto')
    continue
