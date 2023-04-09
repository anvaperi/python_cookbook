class SequenceIterator:
	def __init__(self, sequence=None, function=lambda t: t, *, stop=0):
		self.__sequence = sequence
		self.__function = function
		self.__index = stop if sequence is None else 0

	def __iter__(self):
		return self

	@staticmethod
	def __next_decorator__(next_f):
		def __next_generator__(self):
			if self.__sequence is None:
				self.__sequence = range(self.__index)
				self.__index = 0
			next_f(self)
		return __next_generator__

	@__next_decorator__
	def __next__(self):
		if self.__index >= len(self.__sequence):
			raise StopIteration
		item = self.__function(self.__sequence[self.__index])
		self.__index += 1
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