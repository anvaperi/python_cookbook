def style(any_str, *, bold=False, italics=False, underline=False, strikethrough=False, hex_color=15, hex_on_color=0):
	"""This function adds ansi codes to the input string to get the desired text style on the console.
	text emphasis parameters are booleans, e.g. bold=True. Color parameters are numbers from 0 to 15 to represent
	the hexadecimal values of all the cmyk substractive color system, where k stands for darker.
	The equivalences between ansi colours and cmyk are as follows:

		color: 			white - white - yellow - yellow - magenta	-	magenta	-	red 	-	red		-
		brightness:	light - dark  - light  - dark   - light		-	dark		-	light	-	dark	-
		cmyk_bin:		0000  - 0001  - 0010   - 0011   - 0100		-	0101		-	0110	-	0111	-
		cmyk_dec:		0			- 1			-	2			 - 3			-	4				-	5				-	6			-	7			-
		ansi:  			97    - 37	  - 93     - 33     - 95			-	35			- 91		-	31		-

		color:			-	cyan	- cyan	-	green	-	green	-	blue	-	blue	-	black	-	black
		brightness: -	light	-	dark	- light	-	dark	-	light	-	dark	-	light	-	dark
		cmyk_bin:		-	1000	-	1001	-	1010	-	1011	-	1100	-	1101	-	1110	-	1111
		cmyk_dec: 	-	8			-	9			-	10		-	11		-	12		-	13		-	14		-	15
		ansi:				-	96		-	36		-	92		-	32		-	94		-	34		-	90		-	30
	"""
	def ansi_str(ansi):
		"""Format input ansi code so the output makes the string to be printed look as desired."""
		return '\033[' + str(ansi) + 'm'
	reset_all = 0

	# COLORS
	def get_color_ansi(hex_color):
		"""Takes an input number ranging from 0 to 15 that represents a cmyk color and returns
		its corresponding ansi code."""
		lighter_color_ansi_offset = 90
		darker_color_ansi_offset = 30
		# reset_color_ansi = 39
		cmy_to_ansi_colors = black, red, green, yellow, blue, magenta, cyan, white = (7, 3, 5, 1, 6, 2, 4, 0)
		if not 0 <= hex_color <= 15 or type(hex_color) != int:
			raise ValueError('color argument must be an integer between 0 and 15!')
		cmy, k = divmod(hex_color, 2)
		offset = darker_color_ansi_offset if k else lighter_color_ansi_offset
		return offset + cmy_to_ansi_colors.index(cmy)

	def get_on_color_ansi(hex_on_color):
		"""Takes an input number ranging from 0 to 15 that represents a cmyk color and returns
		its corresponding ansi code for a background color."""
		on_color_ansi_offset = 10
		return on_color_ansi_offset + get_color_ansi(hex_on_color)

	# EMPHASIS
	strikethrough_ansi = 9
	underline_ansi = 4
	italics_ansi = 3
	bold_ansi = 1

	end = ansi_str(reset_all)
	start = []
	if bold:					start += [bold_ansi]
	if italics: 			start += [italics_ansi]
	if underline: 		start += [underline_ansi]
	if strikethrough: start += [strikethrough_ansi]
	start += [get_color_ansi(hex_color), get_on_color_ansi(hex_on_color)]
	start = ansi_str(';'.join([str(c) for c in start]))
	return start + any_str + end


if __name__ == '__main__':
	print(style("--It's me! --Hi.", bold=True, hex_color=6))
	print(style("--I'm the problem it's me", bold=True, hex_color=7))
	print('--At tee time everybody agrees')




