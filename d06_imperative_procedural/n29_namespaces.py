import sys
# for i in sys.__dict__.keys():
# 	print(i, sep='\n')

print()
print(sys.__dict__['hash_info'])

print()

print(__name__) # '__main__'
print()

print(dir()) # inspect the names within your main global scope



my_var = 7 # global

def funca():
	my_var = 3 # local scope

def func():
	global my_var # Global scope DON'T DO THIS
	my_var +=5

func()
print(my_var) # 12



def func2():
	var2 = 2
	def func3():
		nonlocal var2
		var2 += 1
	func3()
	func3()
	func3()
	print(f'{var2=}')
func2()

# print('\n\nBUILTINS')
# print(len(dir(__builtins__)))
# for i in dir(__builtins__):
# 	print(i, sep=' ')


# Ellipsis filter

numbers: tuple[int, ...]
numbers = (2, 4, 'a')
print(numbers)

def do_nothing():
	...

do_nothing()
print(... is Ellipsis)

for i in filter(lambda x: x > 0,  [5, 10, 23, 64, 42, 53, 93, 2, 0, -14, 6, -22, -13]):
	print(i, end=' ')


count = len
numbers = [5, 10, 23, 64, 42, 53, 93, 2, 0, -14, 6, -22, -13]
print(f'{count(numbers)=}')





