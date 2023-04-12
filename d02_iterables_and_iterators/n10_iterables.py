# An iterable is an object that you can iterate over, typically, by means of a for loop,
# unpacking operations and in built-in functions, such as
# all(), any(), enumerate(), max(), min(), len(), zip(), sum(), map(), and filter().
# Pure iterable objects typically hold the data themselves. For example, Python built-in container types
# —such as lists, tuples, dictionaries, and sets—are iterable objects. However,
# iterators are also iterable objects even if they don’t hold the data themselves.
#
# iterables:
#  - Implement the iterable protocol
#  - Make the built-in iter() function return an iterator
#  - Implement the sequence protocol
#

from n02_sequence import SequenceIterator

class Iterable:
	def __init__(self, sequence):
		self.sequence = sequence

	def __iter__(self):
		return SequenceIterator(self.sequence)

if __name__ == '__main__':
	for value in Iterable([1, 2, 3, 4]): print(value, end=' ')
	my_iterable = Iterable(['a', 'b', 'c', 'd'])
	#XXX print(next(my_iterable)) # TypeError: 'Iterable' object is not an iterator
	print(next(iter(my_iterable))) # iter() method returns an iterator
	#print(next(reversed(my_iterable))) # TypeError: 'Iterable' object is not reversible
	print(next(reversed(['a', 'b', 'c', 'd'])))
	# reversed uses Iterable.__reverse__() if exists else .__len__() and .__getitem___(index) if both exist else error
	my_iterable2 = Iterable([43, 32, 21, 10])
	my_list = [item for item in my_iterable2]
	# print(my_iterable2[2]) # TypeError: 'Iterable' object is not subscriptable
	print(my_list[2])

# Sequences are container data types that store items in consecutive order and, thus, accessible through a zero-based index
# the sequence protocol consists of the following methods:
# .__getitem__(index) takes an integer index starting from zero and returns its corresponding item if
# 	index is in range else raises an IndexError exception
# .__len__() returns the length of the sequence.

# uses of iterables: for loops, comprehensions, unpacking

one, two, tree, four = [1, 2, 3, 4] # unpacking
