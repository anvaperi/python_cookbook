from n02_sequence import SequenceIterator
numbers_iter = SequenceIterator([7, 8, 9, 10])
for number in numbers_iter:	print(number) # Works fine
for number in numbers_iter: print(number) # Doesn't work because numbers_iter has been exhausted

## Iterators constraints:
# Iterators cannot be iterated more than once.
# Exhausted iterators cannot be reset
# Iterators cannot go backwards as they lack a .__prev__() method
# No. of items cannot be known until it has been exhausted.

numbers_iter = SequenceIterator([1, 2, 3, 4, 5, 6])
for number in numbers_iter:
	if number == 4:
		break
	print(number)
print(next(numbers_iter), next(numbers_iter))