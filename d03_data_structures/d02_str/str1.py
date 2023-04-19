my_string = 'hiten mitsurugi ryu amakakeru ryou no hirameki'
my_ba = bytearray(my_string, 'utf-8') # b'bla bla bla'
hi = b'hellO worlD'

print(1, my_string, my_ba)
print(2, my_string.find('ry'), my_ba.find(b'ry')) # -1 if missing
print(3, my_string.count('ry'), my_ba.count(b'ry'))
print(4, my_string.index('ry'), my_ba.index(b'ry'))
print(5, my_string[-5:7:-2], '\n', my_ba[-5:7:-2])
print(6, my_string.split('u'), '\n', my_ba.split(b'u'))
print(7, my_string.startswith('h'), my_ba.endswith(b'i'))
print(8, '.' * 3, b',' * 2)
print(9, my_string.replace('ryu', 'dragon'), '\n', my_ba.replace(b'mitsurugi',b'gyou'))
print(10, my_string.upper(), b'HFk'.lower(), hi.title(), hi.capitalize(), hi.swapcase())
print(11, '_'.join(['ab', 'bc', 'cd']), reversed([1, 2, 3]), reversed(b'12345')) # review reversed
print(12, 'oooooups!, Hmmmm'.lstrip('o'), '______eee_____'.rstrip('_'), b'mmemm'.lstrip(b'm'))
print(13, 'Lorem' + ' Ipsum', b'toki ' + b'doki')

# word.isalnum() #check if all char are alphanumeric 
# word.isalpha() #check if all char in the string are alphabetic
# word.isdigit() #test if string contains digits
# word.istitle() #test if string contains title words
# word.isupper() #test if string contains upper case
# word.islower() #test if string contains lower case
# word.isspace() #test if string contains spaces
# word.endswith('d') #test if string endswith a d
# word.startswith('H') #test if string startswith H
