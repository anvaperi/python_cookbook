class SequenceIterator:
	def __init__(self, sequence=None, function=lambda t: t, *, stop=0):
		self._sequence = sequence
		self._function = function
		self._index = stop if sequence is None else 0

	def __iter__(self):
		return self

	@staticmethod
	def __next_decorator__(next_f):
		def __next_generator__(self):
			if self._sequence is None:
				self._sequence = range(self._index)
				self._index = 0
			next_f(self)
		return __next_generator__

	@__next_decorator__
	def __next__(self):
		if self._index >= len(self._sequence):
			raise StopIteration
		item = self._function(self._sequence[self._index])
		self._index += 1
		return item

if __name__ == '__main__':
	for item in SequenceIterator([1, 2, 3, 4], lambda x: x * x):
		print(item)

# sequence = SequenceIterator([1, 2, 3, 4])
#
# # Get an iterator over the data
# iterator = sequence.__iter__()
# while True:
# 	try:
# 		# Retrieve the next item
# 		item = iterator.__next__()
# 	except StopIteration:
# 		break
# 	else:
# 		# The loop's code block goes here...
# 		print(item)