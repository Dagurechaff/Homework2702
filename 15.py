def t(A):
	for x in range(1, 10000):
		if not((A + 2 * x > 400 - A) and (A % 100 + 120 % A > 140)):
			return False
	return True

for A in range(1, 100000000):
	if t(A):
		print(A)
		break