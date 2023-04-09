def inlessfibogen(stop):
	lower, higher = 0, 1
	index = 1
	yield lower
	while index < stop:
		lower, higher = (higher, lower + higher)
		index += 1
		yield lower
	else:
		return

for i in inlessfibogen(10):
	print(i)