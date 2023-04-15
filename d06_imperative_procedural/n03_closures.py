power_factory = lambda exp: lambda base: base ** exp

print(power_factory(2)(10), power_factory(3)(10), power_factory(2)(15))

# Variables like exp are called free variables.
# They are variables that are used in a code block but not defined there.
# Free variables are the mechanism that closures use to retain state information between calls.

def mean():
	iterable_sum = 0
	counter = 0
	def inner_mean(number):
		nonlocal iterable_sum
		nonlocal counter
		iterable_sum += number
		counter += 1
		return iterable_sum/counter
	return inner_mean

current_mean = mean()
another_mean = mean()
print( current_mean(10), current_mean(15), 'a', another_mean(1),  another_mean(7), 'a', current_mean(12),
			'a', another_mean(4), current_mean(11), current_mean(13) )
#> 10.0 12.5 a 1.0 4.0 a 12.333333333333334 a 4.0 12.0 12.2

# def dowhile():
# 	"""Returns a function with a bool parameter returning True the first time and the parameter value after that."""
# 	check_first_time = True
# 	def inner_dowhile(condition):
# 		nonlocal check_first_time
# 		if check_first_time:
# 			check_first_time = False
# 			return True
# 		return condition
# 	return inner_dowhile
#
#
# secret_word = "python"
# counter = 0
# word = secret_word
# dowhile_here = dowhile()
# while dowhile_here(word != secret_word):
# 	word = input("Enter the secret word: ").lower()
# 	counter = counter + 1
# 	if word == secret_word:
# 		print('succeed!')
# 		break
# 	if counter > 7:
# 		print('too many tries!')
# 		break
#
# print('hola')
#
# secret_word = "hola"
# counter = 0
# word = secret_word
# dowhile_here = dowhile()
# while dowhile_here(word != secret_word):
# 	word = input("Enter the secret word: ").lower()
# 	counter = counter + 1
# 	if word == secret_word:
# 		print('succeed!')
# 		break
# 	if counter > 7:
# 		print('too many tries!')
# 		break

def generator():
	count = 0
	def inner_generator():
		nonlocal count
		count +=1
		return count
	return inner_generator

generator1 = generator()
generator1()
generator1()
generator1()
generator1()
generator1()
print(generator1())

print((generator1() for _ in range(5)))

from functools import partial
square = partial(lambda exp, base: base ** exp, 2)
print(square(10))