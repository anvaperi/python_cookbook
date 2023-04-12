# How many ways are there to make change for a $100 bill using any number of $50, $20, $10, $5, and $1 dollar bills?

bills_count ={(20, 3), (10, 5), (5, 2), (1, 5)}
print(bills_count)
bills = [[i[0]]*i[1]for i in bills_count] # [[5, 5], [10, 10, 10, 10, 10], [20, 20, 20], [1, 1, 1, 1, 1]]
print(bills)

import itertools as it

makes_100 = []
for n in range(1, len(bills) + 1):
	for combination in it.combinations(bills, n):
		if sum(combination) == 100:
			makes_100.append(combination)

