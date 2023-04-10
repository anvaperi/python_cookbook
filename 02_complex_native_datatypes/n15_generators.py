from fractions import Fraction


def evens():
	"""Generate even integers, starting with 0."""
	n = 0
	while True:
		yield n
		n += 2

evens = evens()
print(list(next(evens) for _ in range(5)))

import itertools as it

odds = it.count(start=1, step=2)
print(list(next(odds) for _ in range(5)))

negatives = it.count(start=1.3, step=-2.1)
print(list(next(negatives) for _ in range(5)))

print(list(zip(it.count(), ['a', 'b', 'c'])))

def fibs():
	a, b = 0, 1
	while True:
		yield a
		a, b = b, a + b

fibs = fibs()
print(list(next(fibs) for _ in range(15)))

def harmonics():
	i = 0
	acc = 0
	while True:
		i += 1
		fraction = Fraction(1,i)
		acc += fraction
		yield acc

def simplify_fraction(fraction):
	"""Extracts the integer quotient of a fraction leaving another one whose numerator equals the remainder.
	The format is a three length tuple as follows: (quotient, remainder, divisor)"""
	return tuple([
		fraction.numerator // fraction.denominator,
		fraction.numerator %  fraction.denominator,
													fraction.denominator
	])

format_fraction = lambda fraction: \
	str(fraction[0]) + '+' + \
	str(fraction[1]) + '/' + \
	str(fraction[2]) + '; '

harmonics = harmonics()
fractions = list(format_fraction(simplify_fraction(next(harmonics))) for _ in range(15))
print(''.join(fractions))

def factorial():
	i = 0
	n = 1
	while True:
		yield n
		i += 1
		n *= i

factorial = factorial()
print(list(next(factorial) for _ in range(15)))

all_ones = it.repeat(1)
print(list(next(all_ones) for _ in range(15)))

five_qs = it.repeat('q', 5)

while True:
	try:
		nextq = next(five_qs)
		print(nextq, end=' ')
	except StopIteration:
		print()
		break

alternating_nums = it.cycle([1, 0, -1, 0])
print(list(next(alternating_nums) for _ in range(15)))

def accumulate(inputs, func):
	itr = iter(inputs)
	prev = next(itr)
	for cur in itr:
		yield prev
		prev = func(prev, cur)

import operator as op
print(list(it.accumulate([1, 2, 3, 4, 5], op.add)))
print(list(it.accumulate([1, 2, 3, 4, 5])))
print(list(it.accumulate([9, 21, 17, 5, 11, 12, 2, 6], min)))
print(list(it.accumulate([1, 2, 3, 4, 5], lambda x, y: (x + y)/2)))
print(list(it.accumulate([1, 2, 3, 4, 5], lambda x, y: x - y)))
print(list(it.accumulate([1, 2, 3, 4, 5], lambda x, y: y - x)))

def first_order(p, q, initial_val):
    """Return sequence defined by s(n) = p * s(n-1) + q."""
    return it.accumulate(it.repeat(initial_val), lambda s, _: p*s + q)