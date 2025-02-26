def game(n, h):
	if n >= 333 and (h == 5 or h == 3):
		return True
	if n >= 333:
		return False
	if h > 5:
		return False
	if h % 2 == 0:
		return game(n + 3, h + 1) or game(n + 8, h + 1) or game(n * 2, h + 1)
	return game(n + 3, h + 1) and game(n + 8, h + 1) and game(n * 2, h + 1)

for S in range(1, 333):
	if game(S, 1):
		print(S)

#160