def a(N):
	R = oct(N)[2:]
	if N % 2 == 1:
		R = '3' + R[1:-1] + '3'
	else:
		for i in range(1, 8, 2):
			R = R.replace(str(i), '2')
	return int(R, 8)
s = []
for i in range(1000000):
	k = a(i)
	if k < 300:
		s.append(k)
print(max(s))