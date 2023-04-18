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
		r       =          self.r
		rvi	    = r     or self.i
		rvivj   = rvi   or self.j
		rvivjvk = rvivj or self.k
		out = ''
		if not rvivjvk:
			return '0'
		if self.k:
			out = str(self.k) + 'k' + out
			if rvivj and self.k > 0:
				out = ' +' + out
		if self.j:
			out = str(self.j) + 'j' + out
			if rvi and self.j > 0:
				out = ' +' + out
		if self.i:
			out = str(self.i) + 'i' + out
			if r and self.i > 0:
				out = ' +' + out
		if self.r:
			out = str(self.r) + out
		return out


if __name__ == '__main__':
	q1 = Quaternion(1, 2, 3, 4)
	q2 = Quaternion(0, 0, 0, -1)
	q3 = Quaternion(0, 0, 0, -1)
	s = q1 * q2
	print(f'{s=} ', s)
	print(q1, q2, sep='\n')
	print(f'{q2==q3=}')

