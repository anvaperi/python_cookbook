
num_alpha 	= list(zip([1, 2, 3], ['a', 'b', 'c']))
num_sum 		= list(map(sum, zip([1, 2, 3], [4, 5, 6])))
scalar_prod = list(map(lambda t: t[0] * t[1], zip([1, 2, 3], [4, 5, 6])))

print(f'{num_alpha=}\n{num_sum=}\n{scalar_prod=}')

# Given a list of values inputs and a positive integer n, write a function that splits inputs into groups of length n.
# For simplicity, assume that the length of the input list is divisible by n.
# For example, if inputs = [1, 2, 3, 4, 5, 6] and n = 2, your function should return [(1, 2), (3, 4), (5, 6)].

shortest_grouper = lambda inputs, n:	zip(*([iter(inputs)] * n))

n1 = 5
inputs1 = [1, 4, 3, 5, 3, 2, 7, 5, 86, 98, 0, 7, 3]
for element in shortest_grouper(inputs1, n1): print(element, end=' ')
print()

import itertools as it
x = [1, 2, 3, 4, 5]
y = ['a', 'b', 'c']
print(list(zip(x, y)))
print(list(it.zip_longest(x, y)))

longest_grouper = lambda inputs, n, fillvalue=None:	it.zip_longest(*([iter(inputs)] * n), fillvalue=fillvalue)
for element in longest_grouper(inputs1, n1): print(element, end=' ')
print()