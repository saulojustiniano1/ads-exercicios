c = 1
t = 1
aux = c

print('-=' * 15)
while True:
	if c <= 10:
		print(f'{t} x {c} = {t * c}')
		c += 1
    
	if c == 11:
		c = aux
		t += 1
	
	if t == 11:
		break