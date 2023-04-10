import itertools as it

print('\n--First Order Recurrence Relations--\n')
def first_order(p, q, initial_val):
	"""Return sequence defined by s(n) = p * s(n-1) + q."""
	return it.accumulate(it.repeat(initial_val), lambda s, _: p*s + q)

evens = first_order(p=1, q=2, initial_val=0)
print(list(next(evens) for _ in range(5)))
odds = first_order(p=1, q=2, initial_val=1)
print(list(next(odds) for _ in range(5)))
count_by_threes = first_order(p=1, q=3, initial_val=0)
print(list(next(count_by_threes) for _ in range(5)))
count_by_fours = first_order(p=1, q=4, initial_val=0)
print(list(next(count_by_fours) for _ in range(5)))
all_ones = first_order(p=1, q=0, initial_val=1)
print(list(next(all_ones) for _ in range(5)))
all_twos = first_order(p=1, q=0, initial_val=2)
print(list(next(all_twos) for _ in range(5)))
alternating_ones = first_order(p=-1, q=0, initial_val=1)
print(list(next(alternating_ones) for _ in range(5)))


print('\n--Second Order Recurrence Relations--\n')

def second_order(p, q, r, initial_values):
	"""Return sequence defined by s(n) = p * s(n-1) + q * s(n-2) + r."""
	intermediate = it.accumulate(
		it.repeat(initial_values),
		lambda s, _: (s[1], p*s[1] + q*s[0] + r)
	)
	return map(lambda x: x[0], intermediate)

fibs = second_order(p=1, q=1, r=0, initial_values=(0, 1))
print(list(next(fibs) for _ in range(8)))
alt_fibs = second_order(p=-1, q=1, r=0, initial_values=(-1, 1))
print(list(next(alt_fibs) for _ in range(6)))
pell = second_order(p=2, q=1, r=0, initial_values=(0, 1))
print(list(next(pell) for _ in range(6)))
lucas = second_order(p=1, q=1, r=0, initial_values=(2, 1))
print(list(next(lucas) for _ in range(6)))