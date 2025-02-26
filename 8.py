from itertools import product
k = 0
for i in product(sorted('СИНЕРГЯ'), repeat = 6):
	f=''.join(i)

	k+=1
	if 'ГИРЯ' in f:
		print(k,f)