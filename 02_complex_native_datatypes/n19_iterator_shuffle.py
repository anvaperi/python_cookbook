import itertools as it
import random
import math

def iterator_shuffle(iterator, pause=3, to_add_element=None):
	element = 0
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
		if to_add_element is not None:
			yield to_add_element
		#XXX print('\npaused')
	#XXX print('END')

#XXX iterable =[1, 2, 3, 4, 5]
#XXX iterator = iter(iterable)
if __name__ == '__main__':
	print(list(iterator_shuffle(iter([1, 2, 3, 4, 5]))))