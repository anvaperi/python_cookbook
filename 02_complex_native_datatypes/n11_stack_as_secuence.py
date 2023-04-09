class Stack:
	def __init__(self):
		self._items = []

	def push(self, item):
		self._items.append(item)

	def pop(self):
		if not self.__len__():
			raise IndexError("pop from an empty stack") from None
		return self._items.pop()

	def __getitem__(self, index):
		return self._items[index]

	def __len__(self):
		return len(self._items)

	def __iter__(self):
		return iter(self._items)

	def __iter_gen__(self):
		for item in self._items:
			yield item

	def __iter_gen2__(self):
		yield from self._items

if __name__ == '__main__':
	from random import random, seed

	seed(10)
	my_stack = Stack()
	element  = int(5*random())

	while element:
		my_stack.push(element)
		element = int(5*random())

	#XXX iter(my_stack)
	for value in my_stack:
		print(value, end=' ')
