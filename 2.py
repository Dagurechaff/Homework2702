def F(w, x, y, z):
	return not(not(x) or y) or (y == z) or not(w)
print('w', 'x', 'y', 'z')
for w in True, False:
	for x in True, False:
		for y in True, False:
			for z in True, False:
				if not(F(w, x, y, z)):
					print(int(w), int(x), int(y), int(z), 0)