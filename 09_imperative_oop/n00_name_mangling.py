class MyClass:
	def __init__(self):
		self.__private = 42

obj = MyClass()
#print(obj.__private)  # this will raise an AttributeError
print(obj._MyClass__private)  # this works