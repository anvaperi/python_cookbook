import itertools as it

print('\n\n\n-------------------\nRepeated elements')
cycle = it.chain.from_iterable(it.repeat('abc', 5))
print(list(it.repeat('abc', 5)))
print(list(it.chain.from_iterable(it.repeat('abc', 5))))
print(''.join(list(it.islice(cycle, 50))))