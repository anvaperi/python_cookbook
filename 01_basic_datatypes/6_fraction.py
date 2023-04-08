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

print('int attrs:\n',  '\n'.join(dir(Fraction)))