
def to_izey(number):
	"""Returns any positive or negative integer into a coded number,
	whose cyphers 0 to 5 are equivalent to normal cyphers,
	 that is, they add to the total number the amount +c*10^i,
	 where c is the normal cypher and i their order of magnitude.
	 The remaining cyphers behave similarly,
	 but they extract the amount: c*10^i, from the number; where I, Z, E, Y
	 take the values -1, -2, -3 and -4 respectively.
	 E.g. 1Y2 is equivalent to 100 - 40 + 2 = 62;
	 			E54 is equivalent to -300 + 50 + 4 = -246."""
	number_copy = abs(number)
	conversion_digit = 4 + (number < 0)
	carry_over_num = conversion_digit
	# loops until number_copy becomes 0
	while number_copy:
		number_copy = number_copy // 10
		carry_over_num = carry_over_num*10 + conversion_digit
	number += carry_over_num *pow(-1,number < 0)
	syezi_digits = '543210IZEY' if number < 0 else 'YEZI012345'
	return ''.join([ syezi_digits[int(digit)] for digit in str(abs(number))])

print([to_izey(num) for num in [900, 911, 1378, 5456, -5456, 912312]])
['01I00', '01I11', '0014ZZ', '0055YY', '0I4544', '01I12312']


def seg_to_units_min_seg(segs):
	mins, segs = divmod(segs, 60)
	hrs, min = divmod(mins, 60)
	days, hrs = divmod(hrs, 24)
	return (days, hrs, min, segs)

def inches_to_miydftin(inches):
	feets, inches = divmod(inches, 12)
	yards, feets = divmod(feets, 3)
	miles, yards = divmod(yards, 1760)
	return (miles, yards, feets, inches)

for i in range(0, 3660, 666):
	print(seg_to_units_min_seg(i))
