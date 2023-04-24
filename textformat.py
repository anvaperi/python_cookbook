


#______________________________________________________________________

def style(any_str, *, bold=False, italics=False, underline=False, strikethrough=False, hex_=15, hex_on_=0):
	"""This function adds ANSI codes to the input string to get the desired text style on the console.
	text emphasis parameters are booleans, e.g. bold=True. Color parameters are numbers from 0 to 15 to represent
	the hexadecimal values of all the CMYK substractive color system, where 'K' stands for darker.
	The equivalences between ANSI colours and CMYK ones are as follows:

		color: 			white | white | yellow | yellow | magenta	|	magenta	|	red 	|	red		| ...
		brightness:	light | dark  | light  | dark   | light		|	dark		|	light	|	dark	| ...
		cmyk_bin:		0000  | 0001  | 0010   | 0011   | 0100		|	0101		|	0110	|	0111	| ...
		cmyk_dec:		0			| 1			|	2			 | 3			|	4				|	5				|	6			|	7			| ...
		ansi:  			97    | 37	  | 93     | 33     | 95			|	35			| 91		|	31		| ...

		color:			... |	cyan	| cyan	|	green	|	green	|	blue	|	blue	|	black	|	black
		brightness: ... |	light	|	dark	| light	|	dark	|	light	|	dark	|	light	|	dark
		cmyk_bin:		... |	1000	|	1001	|	1010	|	1011	|	1100	|	1101	|	1110	|	1111
		cmyk_dec: 	... |	8			|	9			|	10		|	11		|	12		|	13		|	14		|	15
		ansi:				... |	96		|	36		|	92		|	32		|	94		|	34		|	90		|	30
	"""
	def ansi_str(ansi):
		"""Format input ansi code so the output makes the string to be printed look as desired."""
		return '\033[' + ansi + 'm'
	reset_all = '\033[0m'

	# COLORS
	def get_color_ansi(hex_):
		"""Takes an input number ranging from 0 to 15 that represents a cmyk color and returns
		its corresponding ansi code."""
		lighter_color_ansi_offset = 90
		darker_color_ansi_offset = 30
		cmy_to_ansi_colors = (7, 3, 5, 1, 6, 2, 4, 0) # = black, red, green, yellow, blue, magenta, cyan, white
		if not 0 <= hex_ <= 15 or type(hex_) != int:
			raise ValueError('color argument must be an integer between 0 and 15!')
		cmy, k = divmod(hex_, 2)
		offset = darker_color_ansi_offset if k else lighter_color_ansi_offset
		return offset + cmy_to_ansi_colors.index(cmy)

	def get_on_color_ansi(hex_on_):
		"""Takes an input number ranging from 0 to 15 that represents a cmyk color and returns
		its corresponding ansi code for a background color. 
		As the ANSI color for white produces a shade of grey, the reset ANSI value is returned instead in that case."""
		reset_on_color_ansi = 49
		on_color_ansi_offset = 10
		if not hex_on_:
			return reset_on_color_ansi
		return on_color_ansi_offset + get_color_ansi(hex_on_)

	# EMPHASIS
	emphasis_ansi = (1, 3, 4, 9) # = bold_ansi, italics_ansi, underline_ansi, strikethrough_ansi
	emphasis_check = bold, italics, underline, strikethrough
	selected_emphasis = [each_emphasis for each_emphasis, check in zip(emphasis_ansi, emphasis_check) if check]

	formats = selected_emphasis + [get_color_ansi(hex_), get_on_color_ansi(hex_on_)]
	return ansi_str(';'.join([str(each_format) for each_format in formats])) + any_str + reset_all

def color(input_str):
	hue = ('white', 'yellow', 'magenta', 'red', 'cyan', 'green', 'blue', 'black')
	brightness = ('light', 'dark')
	given_brightness, given_hue = input_str.split()
	hue_index, brightness_index = hue.index(given_hue), brightness.index(given_brightness)
	if hue_index == -1 or brightness_index == -1:
		raise ValueError('hex_ and hex_on_ color values must be in the format: "light/dark + space + white/yellow/magenta/red/cyan/green/blue/black"')
	return hue_index * 2 + brightness_index

if __name__ == '__main__':
	print(style("--It's me! --Hi.", bold=True, hex_=color('light red')))
	print(style("--I'm the problem it's me", bold=True, hex_=color('dark red')))
	print('--At tee time everybody agrees')
	print(style('Gutten Morgen, wie geht es dir? Die ', hex_=color('dark blue')), end='')
	print(style('Praline ', hex_=color('dark yellow')), end='')
	print(style('wahren sehr, sehr lecker', hex_=color('dark blue')))
	#print("hello, my name is Peter, I am 26 years old".split(','))



