# Enum
# List
# Tuple
# named tuple (alternative to dict)
# Set
# frozenset
# dict
# OrderedDict
# Object serialization (persistent dicts called shelve)
# obj info

from enum import Enum

# functional syntax
Week_day = Enum('Week_day', ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'])

Month = Enum('Month', ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY',
											 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER'])

# class syntax
class Season(Enum):
	SPRING = 1
	SUMMER = 2
	FALL = 3
	WINTER = 4

print(dir(Enum))

for each_month in Month:
	print(each_month, each_month.name, each_month.value)

# Immutable objects are common in functional programming,
# whereas mutable objects are widely used in object-oriented programming.
# variables and objects are two different animals in Python:
#  - Variables hold references to objects.
#  - Objects live in concrete memory positions. (ids) id(my_object) in CPython
#  - Python objects have three core properties:
#  		> identity: (ids) id(my_object)
#  	 	>	type:
#  	 	> value:

isinstance([1, 2, 3], list)

a = 13
print(type(id(a)))


class Person:
	def __init__(self, name):
		self.name = name


class Student(Person):
	def __init__(self, name, major):
		super().__init__(name)
		self.major = major


john = Student("John", "Computer Science")
type(john) # <class '__main__.Student'>

john.__class__ = Person
type(john) # <class '__main__.Person'>


# Single-item data types, such as integers, floats, complex numbers, and Booleans, are always immutable
# Strings bytes and tuples, frozensets are immutable
# lists, dictionaries, and sets are mutable as well as BYTEARRAYS

# If you want to store a binary value over 127 in a bytearray object,
# then you must enter it using the appropriate escape sequence in the literal

print( issubclass(bool, int), isinstance(True, int), isinstance(False, int), int(True), int(False)) # True True True 1 0

# my_string = 'whatever'
# my_string[0] = 'W' #>TypeError: 'str' object does not support item assignment

greeting = "Hello!"

mutable_greeting = bytearray(greeting.encode("utf-8"))
print(id(mutable_greeting)) #140293973558064

mutable_greeting[1] = ord("E")
print(mutable_greeting)
print(bytearray(b'HEllo'))

print(id(mutable_greeting)) #140293973558064

# Good examples of where to use tuples include records from a SQL database and lines from a CSV file
for i in dir(tuple):
	print(i)

# There are seven sequence types: strings, bytes, lists, tuples, bytearrays, buffers, and range objects.

#  immutable types, such as numbers, Booleans, and strings, are hashable. That means you can use them as dictionary keys.
# UNION OPERATOR
# Regular operator
inventory = {"apples": 42} | {"bananas": 24}
print(inventory) # {'apples': 42, 'bananas': 24}

# Augmented operator
inventory = {"apples": 42}
print(id(inventory)) # 4381513984
inventory |= {"bananas": 24}
print(inventory) # {'apples': 42, 'bananas': 24}
print(id(inventory)) # 4381513984

# SETS

#print({'lemon', 'banana', 'grape', 'orange'}.remove("mango")) #!> KeyError: 'mango'
print({'lemon', 'banana', 'grape', 'orange'}.discard("mango"))

# Python’s sets also implement operations from the original mathematical sets,
# including union, intersection, difference, and symmetric difference. All these operations return a new set object
# few methods that mutate the target set in place:
# . a_set.intersection_update(*others)
# . a_set.difference_update(*others)
# . a_set.symmetric_difference_update(other)

# | Union, & intersection, - difference, ^ symmetric difference


# BYTEARRAYS
greeting = bytearray(b"Hello, World!")
greeting[1] = 69 # OK: "L", b"L", bytearray(b"L"), ord("л") -> ERROR
greeting[2] = ord("L")


## Aliasing Variables
## Mutatating Arguments in Functions

print([i for i in enumerate([1, 4, 8, 5])]) #[(0, 1), (1, 4), (2, 8), (3, 5)]

## Using Mutable Default Values !!

def append_to(item, target=[]): # The function becomes stateful. !!!
	target.append(item)
	return target

append_to(1) # [1]
append_to(2) # [1, 2]
append_to(3) # [1, 2, 3]
print(append_to(4))

def append_to(item, target=None): # Solved
	if target is None:
		return [item]
	target.append(item)
	return target

append_to(1) # [1]
append_to(2) # [2]
append_to(3) # [3]
print(append_to(4)) # [4]


def cumulative_mean(value, sample=[]):
	sample.append(value)
	return sum(sample) / len(sample)

cumulative_mean(1)
cumulative_mean(3)
cumulative_mean(6)
print(cumulative_mean(10)) # 5 :-D

## Making Copies of Lists
# A shallow copy, which you create using the slicing operator ([:]), the .copy() method, or the copy.copy() function
# A deep copy, which you can create using the copy.deepcopy() function

## Getting None From Mutator Methods
'<html lang="en">'.removeprefix("<").removesuffix(">").upper().center(20) # '   HTML LANG="EN"   '
[3, 4, 2, 6, 1].sort() # None !!

#("RED", [255, 0, 0])[1] = [0, 0, 0] #!> TypeError: 'tuple' object does not support item assignment
("RED", [255, 0, 0])[1][0] = 0 # ('RED', [0, 0, 0]) !!

## In general, putting mutable objects in tuples is a bad idea.

## Concatenating Many Strings
_ = "Hello" + "," + " " + "World" + "!" # BAD
_ = "".join(["Hello", ",", " ", "World", "!"]) # GOOD

## Mutability of Classes, Instances and Attributes
#...
#_ = john.__dict__ #{'name': 'John Doe', 'job': 'Python Dev'}
#del john.job # {'name': 'John Doe'}

## Techniques to Control Mutability in Custom Classes

# Defining a .__slots__ class attribute
#  the .__slots__ class attribute specifies the allowed attributes for a given object
# Unfortunately, the .__slots__ attribute doesn’t prevent you from adding new class attributes and methods dynamically

class Book:
	__slots__ = ("title",)
	def __init__(self, title):
		self.title = title


harry_potter = Book("Harry Potter") # harry_potter.title #'Harry Potter'

# harry_potter.author = "J. K. Rowling" #!> AttributeError: 'Book' object has no attribute 'author'


# Providing custom .__setattr__() and .__delattr__() methods
class Immutable:
	def __init__(self, value):
		super().__setattr__("value", value)

	def __setattr__(self, name, attr_value):
		raise AttributeError(f"can't set attribute '{name}'")

	def __delattr__(self, name):
		raise AttributeError(f"can't delete attribute '{name}'")


# Using read-only properties


class Point:
	def __init__(self, x, y):
		self._x = x
		self._y = y

	@property
	def x(self):
		return self._x

	@property
	def y(self):
		return self._y

	def __repr__(self):
		return f"{type(self).__name__}(x={self.x}, y={self.y})"



# Relying on descriptors with an appropriate .__set__() method

class Coordinate:
	def __set_name__(self, owner, name):
		self._name = name

	def __get__(self, instance, owner):
		return instance.__dict__[f"_{self._name}"]

	def __set__(self, instance, value):
		raise AttributeError(f"can't set attribute '{self._name}'")

class Point:
	x = Coordinate()
	y = Coordinate()

	def __init__(self, x, y):
		self._x = x
		self._y = y

	def __repr__(self):
		return f"{type(self).__name__}(x={self.x}, y={self.y})"

# Using an immutable class, such as a named tuple or a data class

from collections import namedtuple

Point = namedtuple("Point", "x y")
point = Point(21, 42)
print(point) # Point(x=21, y=42)
print(point.x) # 21
print(point.y) # 42


