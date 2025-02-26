
print('w', 'x', 'y', 'z')
for w in True, False:
	for x in True, False:
		for y in True, False:
			for z in True, False:
				if not(not(not(x) or y) or (y == z) or not(w)):
					print(int(w), int(x), int(y), int(z), 0)