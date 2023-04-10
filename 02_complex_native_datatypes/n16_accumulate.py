import itertools as it
import operator as op

def accumulate(input_iterable, binari_funtion):
	iterator = iter(input_iterable)
	previous_element = next(iterator)
	for current_element in iterator:
		yield previous_element
		previous_element = binari_funtion(previous_element, current_element)

print(list(it.accumulate([1, 2, 3, 4, 5], op.add)))
print(list(it.accumulate([1, 2, 3, 4, 5])))
print(list(it.accumulate([9, 21, 17, 5, 11, 12, 2, 6], min)))
print(list(it.accumulate([1, 2, 3, 4, 5], lambda x, y: (x + y)/2)))
print(list(it.accumulate([1, 2, 3, 4, 5], lambda x, y: x - y)))
print(list(it.accumulate([1, 2, 3, 4, 5], lambda x, y: y - x)))