

def toogle(state=[True]):
	state[0] = not state[0]
	return state[0]

def reset_do_while():
	toogle(True)

print(toogle(), toogle(), toogle(), toogle([True]), toogle([True]), toogle([True]))

def do_while(condition, check_first_called=[True]):
	if check_first_called[0]:
		check_first_called[0] = False
		return True
	return condition


secret_word = "python"
counter = 0
word = secret_word
while do_while(word != secret_word):
	word = input("Enter the secret word: ").lower()
	counter = counter + 1
	if word == secret_word:
		print('succeed!')
		break
	if counter > 7:
		print('too many tries!')
		break

print('hola')

secret_word = "hola"
counter = 0
word = secret_word
while do_while(word != secret_word):
	word = input("Enter the secret word: ").lower()
	counter = counter + 1
	if word == secret_word:
		print('succeed!')
		break
	if counter > 7:
		print('too many tries!')
		break