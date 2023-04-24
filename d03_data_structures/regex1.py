import re

pattern = '^a...s$'
print([re.match(pattern, each_string) for each_string in ['abs', 'alias', 'abyss', 'Alias', 'An Abacus'] ])
charsetptt = '[a-c]' # [0-39] is the same as [01239]
print([re.match(charsetptt, each_string) for each_string in ['a', 'ac', 'Hey Jude', 'abc de ca']])
notinset = '[^h-z]'
print([re.match(notinset, each_str) for each_str in ['aeg', '34b', 'ewx', 'x4']])
anychar = '.'
print([re.match(anychar, each_str) for each_str in ['c', '\n']])
startswithab = '^ab'
print([re.match(startswithab, word) for word in ['abc', 'acb']])
endswith13 = '13$'
print([re.match(endswith13, word) for word in ['er1413', '13\n']]) # !! review
noneormany01s = '..(01)*..' # X* <> X{0,many}
print([re.match(noneormany01s, word) for word in ['a0101010101bc', 'acb']])
oneormanylove = '.(love)+' # X+ <> X{1,many}
print([re.match(oneormanylove, word) for word in ['alovelove or love me right now!!bc', 'alive cb']])
zerooronething = '.*(thing)?' # X? <> X{0,1}
print([re.match(zerooronething, word) for word in [' slkjfdskfljf lkjsdf lkjds lfjk bc', 'alithingve cb']])
twotofourdigits = '.*[0-9]{2,4}'
print([re.match(twotofourdigits, word) for word in ['ab123csde', '12 and 345673', '1 ans 2']])
avb = '.*a|b'
print([re.match(avb, word) for word in ['cde', 'ade', 'acdbea']])
avbvcandxz = '(a|b|c)xz'
print([re.match(avbvcandxz, word) for word in ['ab xz', 'abxz', 'axz cabxz']])
dollarsandas = '\$a' # '\' escapes especial chars
print([re.match(dollarsandas, word) for word in ['$ab xz', 'abxz', 'axz cabxz']])
stringbeginning = '\Athe'
print(re.match(stringbeginning, 'the space'))
stringend = 'bla\Z'
wordbeginning = '\bwo'
print(re.match(wordbeginning, 'woman'))
wordend = 'ew\b'
print(re.match(wordend, 'brew'))
notatbeginningnorendofword = '\Bcas\B'
print(re.match(notatbeginningnorendofword, 'Cassandra'))
digit = '\d' # also [0-9]
print(re.match(digit, 'r2d2'))
nondigit = '\D' # also [^0-9]
print(re.match(nondigit, 'yin'))
anywhitespacechar = '\s' # also [ \t\n\r\f\v]
print(re.match(anywhitespacechar, 'Python RegEx'))
anynonwhitespacechar = '\S' # also [^ \t\n\r\f\v]
print(re.match(anynonwhitespacechar, '   '))
alphanum = '\w' # also [a-zA-Z0-9_]
anynonalphanum = '\W' # also [^a-zA-Z0-9_]
# https://regex101.com/
