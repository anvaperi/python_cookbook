import itertools as it

for combination in it.combinations("rgb", 2):	print(combination, end=' ')
print('-----')
for combination in it.combinations_with_replacement("xyz", 2):	print(combination, end=' ')
print('-----')
for permutation in it.permutations("abc", 2):	print(permutation, end=' ')
print('-----')