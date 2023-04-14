
def to_syezi(number):
	number_copy = abs(number)
	conversion_digit = 4 + (number < 0)
	carry_over_num = conversion_digit
	while number_copy % 10:
		number_copy = number_copy // 10
		carry_over_num = carry_over_num*10 + conversion_digit
	number += carry_over_num *pow(-1,number < 0)
	syezi_digits = '543210IZEY' if number < 0 else 'YEZI012345'
	return ''.join([ syezi_digits[int(digit)] for digit in str(abs(number))])


print([to_syezi(num) for num in [1378, 5456, -5456, 912312]])
