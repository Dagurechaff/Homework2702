def game(n, h):
	if n >= 333 and h == 4:
		return True
	if n >= 333:
		return False
	if h > 3:
		return False
	if h % 2 == 1:
		return game(n + 3, h + 1) or game(n + 8, h + 1) or game(n * 2, h + 1)
	return game(n + 3, h + 1) and game(n + 8, h + 1) and game(n * 2, h + 1)
test = True
mn = 0
mx = 0
for S in range(1, 333):
	if game(S, 1):
		if test:
			mn = S
			test = False
		mx = S 
print(mn, mx)
