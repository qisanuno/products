data = [1, 3, 5, 7, 9]
with open('writep.txt', 'w') as f:
	for d in data:
		f.write(str(d + 1) + '\n')