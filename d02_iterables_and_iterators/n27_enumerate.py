import random

for count, value in enumerate(['a', 'b', 'c']):
	print(count, value, end=' ')
print()

for count, value in enumerate(['a', 'b', 'c'], start=1):
	print(count, value, end=' ')
print()

# Different action for the first loop element
users = ["Test User", "Real User 1", "Real User 2"]
for index, user in enumerate(users):
	if not index:
		print("Extra verbose output for:", end=' ')
	print(user)


def filter_evens(iterable):
	"""Return items from ``iterable`` when their index is even."""
	return (value	for index, value in enumerate(iterable, start=1) if not index % 2)

print(list(filter_evens(chr(n) for n in range(ord('A'), ord('Z')+1))))

# Your version of enumerate() has two requirements. It should:
#
# Accept an iterable and a starting count value as arguments
# Send back a tuple with the current count value and the associated item from the iterable

def my_aggr_enumerate(sequence, start=0):
	count = start + 1
	iterator = iter(sequence)
	first_element = next(iterator)
	yield start, first_element
	is_num = isinstance(first_element, int) or isinstance(first_element, float)
	if is_num:
		acc = current_min = current_max = first_element
	for item in iterator:
		disorder = int(count * random.random())
		yield count, item, disorder
		count += 1
		if is_num:
			acc += item
			current_min = min(current_min, item)
			current_max = max(current_max, item)
	else:
		if is_num:
			yield (-1, count)
			yield (-2, acc)
			yield (-3, acc/count)
			yield (-4, current_min)
			yield (-5, current_max)

aggregations = my_aggr_enumerate([30, 1, 2 ,3, 4, 5, 6, 7, 8, 9])
print(list(aggregations))


aggregations = my_aggr_enumerate(["Spring", "Summer", "Fall", "Winter"])
print(list(aggregations))


enum_instance = enumerate(["a", "b"])
print(next(enum_instance, None), next(enum_instance, None), next(enum_instance, None))

print()
names = ["Fluffy", "Bello", "Lady Kitty"]
species = ["dog", "dog", "cat"]
gender = ["female", "male", "female"]
age_years = ["4", "1", "8"]
for i_count, (i_name, i_species, i_gender, i_age_years) in enumerate(zip(names, species, gender, age_years), start=1):
  print(i_count, i_name, i_species, i_gender, i_age_years)

print()
import itertools
for i_count, i_name, i_species, i_gender, i_age_years in zip(itertools.count(1), names, species, gender, age_years):
	print(i_count, i_name, i_species, i_gender, i_age_years)


#print(4* random.random())