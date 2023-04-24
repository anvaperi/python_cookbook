import re

# extract numbers
print(re.findall('\d+', 'hello 12 hi 89. Howdy 34'))
# split
print(re.split('\d+', 'Twelve:12 Eighty nine:89.'))
# split only at first occurrence
print(re.split('\d+', 'Twelve:12 Eighty nine:89 Nine:9.', 1))
# pattern, replace, in_string
print(re.sub('\s+', '', 'acb 12\
de 23 \n f45 6'))
# pattern, replace, in_string -> (out_str, substitutions_count)
print(re.subn('\s+', '', 'acb 12\
de 23 \n f45 6'))
# search
print(bool(re.search('\APython', 'Python is fun')))
for attr in dir(re.search('\APython', 'Python is fun')):
    print(attr)
# three digits + space + two digits
match = re.search('(\d{3}) (\d{2})', '39801 356, 2102 1111')
print(match.group(2), match.groups(), match.start(), match.end(), match.span(), match.re, match.string) 
#  raw strings
print(re.search(r'[\n\r]', '\n and \r are escape sequences.'))
