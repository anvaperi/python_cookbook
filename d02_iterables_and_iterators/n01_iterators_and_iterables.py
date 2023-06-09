# Python’s while loop supports indefinite iteration, whereas for loop supports definite iteration
# Iterators take responsibility for:
#   - Returning the data from a stream or container one item at a time
#   - Keeping track of the current and visited items
# Iterator Protocol implements two methods:
#   - .__iter__()	Initializes the iterator and by returning an iterator object. def __iter__(self): return self
#   - .__next__()	Iterates over the iterator by returning the next value in the data stream or
#   raises Exception(StopIteration) at the end.
#
# for loops, comprehensions, iterable unpacking ...
# Iterators may be generated by processed or raw input or from no input at all

counter = 0
while counter < 3:
	print("Hello!")
	counter += 1

iterable_list = [1, 2, 3, 4, 5]
for element in iterable_list:
	print(element)

for element in set('abcde'):
	print(element)