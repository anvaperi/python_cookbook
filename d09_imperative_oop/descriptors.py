class Celsius:
	def __get__(self, instance, owner):
		return (instance.fahrenheit - 32) * 5 / 9

	def __set__(self, instance, value):
		instance.fahrenheit = value * 9 / 5 + 32


class Temperature:
	celsius = Celsius()

	def __init__(self, fahrenheit):
		self.fahrenheit = fahrenheit


temp = Temperature(100)
print(temp.celsius)  # Output: 37.77777777777778

temp.celsius = 20
print(temp.fahrenheit)  # Output: 68.0