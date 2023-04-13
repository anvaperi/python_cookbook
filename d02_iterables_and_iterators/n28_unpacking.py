#Unpacking
x, y = 10, 20;		print(x, y)
(x, y) = (10, 20);		print(x, y)
x, y = [10, 20];		print(x, y)
x, y = 'hi';		print(x, y)
x, y, z = point = 10, 20, 30;		print(point, x, y, z)
x, y, z = y, z, x;		print(x, y, z)
my_dict = {'k1': 'va', 'k2': 'vb', 'k3': 'vc'}
for item in my_dict.items():
	print(f'{item[0]=}: {item[1]=}')
for k, v in my_dict.items():
	print(f'{k=}: {v=}')
for i, v in enumerate([5, 3, 1]):
	print(f'{i=}: {v=}')
for name, age in zip(['Jean', 'Joseph', 'Julius'], [34, 12, 82]):
	print(f'{name=}: {age=}')
mmddyyy_date = '04/13/2023'
month, day, year = mmddyyy_date.split('/')
print(f'{year}-{month}-{day}')

x, *y = 10, 20, 30
print(x, y)

_, *z, _ = [1, 2, 3, 4, 5]
print(z)

import sys
def f(a, b): pass
f(sys.argv[0], sys.argv[1:]) # :(

program_name, *args = sys.argv
f(program_name, args) # :D

color, (x, y, z) = color, point = ('red', (255, 0, 0))
print(color, point)

ais = a0, a1, a2 = (1, 2), (3, 4), (5, 6)
bis = b0, b1, b2 = (-1, -5), (-3, -2), (-9, 0)

for (ax, ay), (bx, by) in zip(ais, bis):
	if ax == -bx and ay == -by:
		print(f' a {ax}:{ay} was negated')
	else:
		print(f' a {ax}:{ay} was not negated')

print()
for i , (first, last) in (lambda items:
	enumerate(zip((items), reversed(items))))([1, 2, 3, 4, 6, 3, 2, 1]):
	if first != last: print('Error')
	print(f'{i=}: {first=}: {last=}')

from collections import Counter

def most_common(items):
	(value, times_seen), = Counter(items).most_common(1) # BEWARE OF THE TRAILING COMMA!!
	return value

def most_common2(items):
	[(value, times_seen)] = Counter(items).most_common(1) # Better, more clear
	return value
numbers = [1,2,3,3,4,5,6,6,7,9]
[first, *rest] = numbers

