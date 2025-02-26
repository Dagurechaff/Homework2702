def F(n):
	if n > 2000:
		return 16
	return 2 * F(n + 3)

s = [int(i) for i in str(int(F(50) / F(110))).replace('0', '')]
t = 1
for i in s:
	t *= i
print(t)