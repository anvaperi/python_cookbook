from dataclasses import dataclass


@dataclass
class Dual:
	r: float
	epsilon: float

	def __add__(self, other):
		return Dual(self.r + other.r,	self.epsilon + other.epsilon)

	def __mul__(self, other):
		return Dual(self.r * other, self.r * other.epsilon + self.epsilon * other.r)