from decimal import *
import math

nan = Decimal("Nan")

getcontext()
# Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999,
#         capitals=1, clamp=0, flags=[], traps=[Overflow, DivisionByZero,
#         InvalidOperation])


getcontext().prec = 28    # Set a new precision
print(Decimal(10)) #'10'
print(Decimal('3.14')) # '3.14'
print(Decimal(3.14)) # 3.140000000000000124344978758017532527446746826171875
print(Decimal(math.pi)) # 3.141592653589793115997963468544185161590576171875
print(Decimal((0, (3, 1, 4), -2))) # '3.14'
print(Decimal(str(2.0 ** 0.5))) # '1.4142135623730951'
print(Decimal(2) ** Decimal('0.5')) # '1.414213562373095048801688724'
print(Decimal('NaN')) # 'NaN'
print(Decimal('-Infinity')) # '-Infinity'
print(Decimal(math.pi).as_integer_ratio()) # 355/113
print(Decimal(-355).copy_abs())
my_dec = Decimal('-234.87')
print(my_dec)
print(my_dec.is_finite())
print(my_dec.is_infinite())
print(my_dec.is_nan())
print(my_dec.is_signed())
print(my_dec.is_zero())
print(Decimal('-0.0023487000').normalize(context=None))
print((-my_dec).sqrt(context=None))


print('bool attrs:\n',  '\n'.join(dir(Decimal)))