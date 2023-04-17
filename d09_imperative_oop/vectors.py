from dataclasses import dataclass
from math import sqrt, atan

@dataclass
class Vector:
	x: float
	y: float
	z: float

	@property
	def latitude(self):
		return atan(self.z/self.rcoslat)

	@property
	def longitude(self):
		return atan(self.y/self.x)

	@property
	def rcoslat(self):
		return sqrt(self.x * self.x + self.y * self.y)

	@property
	def r(self):
		return sqrt(self.scalar_mul(self))

	def __add__(self, other):
		return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

	def __mul__(self, other):
		return Vector(
			self.y * other.z -  self.z * other.y,
			self.z * other.x - self.x * other.z,
			self.x * other.y - self.y * other.x
		)

	def scalar_mul(self, other):
		return Vector(self.x * other.x, self.y * other.y, self.z * other.z)