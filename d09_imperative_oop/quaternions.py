from dataclasses import dataclass
from functools import reduce
from numpy import matrix, matmul

@dataclass
class Quaternion:
	r: float
	i: float
	j: float
	k: float

	def as_array(self):
		return [self.r, self.i, self.j, self.k]

	def as_matrix(self):
		return matrix([
			[+self.r, -self.i, -self.j, -self.k],
			[+self.i, +self.r, -self.k, +self.j],
			[+self.j, +self.k, +self.r, -self.i],
			[+self.k, -self.j, +self.i, +self.r]
		])

	def __mul__(self, other):
		m = matmul(self.as_matrix(), other.as_matrix())
		return Quaternion(m.item((0,0)), m.item((1,0)), m.item((2,0)), m.item(3,0))

	def __str__(self):
		if self.r == self.i == self.j == self.k:
			return '0'
		out = ''
		if self.r: out += str(self.r) + ' '
		if self.i: out += str(self.i) + 'i '
		if self.j: out += str(self.j) + 'j '
		if self.k: out += str(self.k) + 'k '
		return out

if __name__ == '__main__':
	q1 = Quaternion(0, 0, 1, 0)
	q2 = Quaternion(0, 1, 0, 0)
	s = q1 * q2
	print(f'{s=}')
