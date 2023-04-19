from collections import namedtuple

# COLORS
background_color_code = 10
brighter_color_code = 60
color_code_offset = 30
reset_color_code = 39
colors = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'grey']
code_str = lambda code: '\033[' + str(code) + 'm'

encode_color = lambda color_name, brighter_check, bckgrnd_check: \
	color_code_offset + colors.index(color_name) +\
	brighter_color_code * brighter_check + \
	background_color_code * bckgrnd_check

colorise_text = lambda color_name, brighter_check=False, bckgrnd_check=False, input_str='': \
	code_str(encode_color(color_name, brighter_check, bckgrnd_check)) + \
	input_str + code_str(reset_color_code)

text_color 			= namedtuple('text_color', 'background foreground')

Cmyk_color 			= namedtuple('Cmyk_color', 'c m y k')
bright_grey 		= Cmyk_color(False,  False,  False,  False)
dark_grey 			= Cmyk_color(False,  False,  False,  True)
bright_yellow 	= Cmyk_color(False,  False,  True,  False)
dark_yellow 		= Cmyk_color(False,  False,  True,  True)
bright_magenta 	= Cmyk_color(False,  True,  False,  False)
dark_magenta   	= Cmyk_color(False,  True,  False,  True)
bright_red 			= Cmyk_color(False,  True,  True,  False)
dark_red 				= Cmyk_color(False,  True,  True,  True)
bright_cyan 		= Cmyk_color(True,  False,  False,  False)
dark_cyan 			= Cmyk_color(True,  False,  False,  True)
bright_green 		= Cmyk_color(True,  False,  True,  False)
dark_green 			= Cmyk_color(True,  False,  True,  True)
bright_blue 		= Cmyk_color(True,  True,  False,  False)
dark_blue 			= Cmyk_color(True,  True,  False,  True)
bright_black 		= Cmyk_color(True,  True,  True,  False)
dark_black 			= Cmyk_color(True,  True,  True,  True)


# EMPHASIS
strikethrough_code = 9
underscore_code = 4
italics_code = 3
bold_code = 1
reset_all = 0

in_bold 				= lambda input_str: code_str(bold_code) 					+ input_str + code_str(reset_all)
in_italics 			= lambda input_str: code_str(italics_code) 				+ input_str + code_str(reset_all)
underscored			= lambda input_str: code_str(underscore_code) 		+ input_str + code_str(reset_all)
strikethrought 	= lambda input_str: code_str(strikethrough_code) 	+ input_str + code_str(reset_all)


if __name__ == '__main__':
	pass