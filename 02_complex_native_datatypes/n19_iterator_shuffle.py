import itertools as it
import random
import math

def iterator_shuffle(iterator):
	element = 0
	pause = 3
	memory = float('nan')
	index = 0
	while element is not None:
		while element is not None and index != pause:
			element = next(iterator, None)
			if int(2 * random.random()):
				memory, element = element, memory
				#XXX print(f'{memory=}, {element=}')
			if element is not None and not math.isnan(element):
				#XXX print(element, end=' ')
				yield element
				index += 1
		pause -= 1
		print('\npaused')
	print('END')

# iterable =[1, 2, 3, 4, 5]
# iterator = iter(iterable)

print(list(iterator_shuffle(iter([1, 2, 3, 4, 5]))))