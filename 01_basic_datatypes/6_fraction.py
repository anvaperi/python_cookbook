from fractions import *
from decimal import Decimal

print(Fraction(16,-10))
print(Fraction(123))
print(Fraction())
print(Fraction('-3/7'))
print(Fraction('-.125'))
print(Fraction('7e-6'))
print(Fraction(1.1))
print(Fraction(Decimal('1.1')))
print(Decimal('3.14').as_integer_ratio())
#print(Fraction(1, 0)) # ERROR!!
f = Fraction(9,5)
print(f.numerator, f.denominator)
print(Fraction('3.1415926535897932').limit_denominator(1000))

def reduced_fraction(fraction):
	return (fraction.numerator // fraction.denominator) + \
		(Fraction(fraction.numerator % fraction.denominator, fraction.denominator))*1J

def print_reduced_fraction(fraction):
	print(' + '.join([str(i) for i in (reduced_fraction(fraction))]))

print(reduced_fraction(f))
print(reduced_fraction(Fraction(2,3)))
print(reduced_fraction(Fraction(20,3)))

def combine_fraction(in_tuple):
  return Fraction(in_tuple[0] * in_tuple[1].denominator + in_tuple[1].numerator, in_tuple[1].denominator)

my_tuple = (6, Fraction(2,3))
print(combine_fraction(my_tuple))

print('int attrs:\n',  '\n'.join(dir(Fraction)))