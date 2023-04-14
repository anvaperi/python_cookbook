
def to_romans(num):
	magnitud_order = 0
	output_substr = ''
	output = ''
	chars = ('IV', 'XL', 'CD', 'M-')
	while num:
		five_multiple, one_multiple = divmod(num, 5)
		num, five_multiple = divmod(five_multiple, 2)
		if one_multiple == 4:
			output_substr += chars[magnitud_order][0] # added substractor
			if five_multiple:
				output_substr += chars[magnitud_order + 1][0] # ends in 9
			else:
				output_substr += chars[magnitud_order][1] # ends in 4
		else:
			if five_multiple:
				output_substr += chars[magnitud_order][1]
			output_substr += chars[magnitud_order][0] * one_multiple
		magnitud_order += 1
		output = output_substr + output
		output_substr = ''
	return output
#	return ''.join(output.reverse())

for i in range(500, 4001, 250):
	print(to_romans(i), end=' ')