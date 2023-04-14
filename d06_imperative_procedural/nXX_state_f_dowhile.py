# Don't do this but use closures instead for creating state functions

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
