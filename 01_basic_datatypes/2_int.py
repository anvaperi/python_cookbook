# integer values under or over zero. Use for discrete mathematical operations or counters
import math, datetime

PI = math.pi

x = 3
negated   = -x;     print('Negated: ', negated)
unchanged = +x;     print('unchanged: ', unchanged)
vect_mod  = abs(x); print('vect_mod: ', vect_mod)
sum       = 3 + 4;  print('sum: ', sum)
diff      = 7 - 19; print('diff: ', diff)
product   = 5 * 2;  print('product: ', product)
quotient  = 4 // 3; print('quotient: ', quotient)
remainder = 4 % 3;  print('remainder: ', remainder)
quorem    = divmod(4,3); print('quorem: ', quorem) # quotient and remainder
power     = 3 ** 2; print('power: ', power)
power2    = pow(3,2); print('power2: ', power2)
increment = 1
increment += 2;     print('increment: ', increment)
decrement = 1
decrement -= 3;     print('decrement: ', decrement)

math.trunc(PI);     print('trunc: ', math.trunc(PI))
round(PI, 1);       print('round: ', round(PI, 1))
math.floor(PI);     print('floor: ', math.floor(PI))
math.ceil(PI);      print('ceil: ', math.ceil(PI))
int(PI);            print('int: ', int(PI))

print('0⁰ is ␀ but in Python: 0⁰ = ', 0 ** 0, "!!")



i = 33; decimal = i;                 print('dec: ', i, end=' ');          print(int('33'));
print(int('100001', 2), end=' ');    print(int('41', 8), end=' ');        print(int('21', 16));
print(int('0B100001', 0), end=' ');  print(int('0O41', 0), end=' ');      print(int('0X21', 0));
binary  = 0B100001;                  octal   = 0O41;                      hexadecimal = 0X21;
print('bin: ', bin(i), end=' ');     print('oct: ', oct(i), end=' ');     print('hex: ', hex(i))
print(format(i, 'b'), end=' ');      print(format(i, 'o'), end=' ');      print(format(i, 'x'))
print(format(i, '#b'), end=' ');     print(format(i, '#o'), end=' ');     print(format(i, '#x'))
print(format(i, '#010b'), end=' ');  print(format(i, '#010o'), end=' ');  print(format(i, '#010x'))
print(format(i, '08b'), end=' ');    print(format(i, '08o'), end=' ');    print(format(i, '08x'))
print('{:08b}'.format(i), end=' ');  print('{:08o}'.format(i), end=' ');  print('{:08x}'.format(i))
print(f'{i:08b}', end=' ');          print(f'{i:08o}', end=' ');          print(f'{i:08x}')
print('\n two complement', end=' ')

negative = -9
print(bin(negative)) ## -0b1001
_4bit2complement  = negative & 0xF;     print(bin(_4bit2complement))
_8bit2complement  = negative & 0xFF;    print(bin(_8bit2complement))
_16bit2complement = negative & 0xFFFF;  print(bin(_16bit2complement))
print()
year = 2022
month = 1
day = 5
print(f'{year}{month:0>2}{day:0>2}')
print(f'{year}{month:02d}{day:02d}')

now = datetime.datetime.now()
print(f'Today is {now:%d} of {now:%B} {now:%Y}')
print(f'{now=:%Y-%m-%d}')
print()
print('int attrs:\n',  '\n'.join(dir(int)))
i = 13
# representing decimal 13 in binary, octal, and hexadecimal
print(f"binary: {i:b}; octal: {i:o}; hex: {i:x} or {i:X}") # 'binary: 1101; octal: 15; hex: d or D'
# the #-option adds prefixes
print(f"binary: {i:#b}; octal: {i:#o}; hex: {i:#x} or {i:#X}") # 'binary: 0b1101; octal: 0o15; hex: 0xd or 0XD'
# binary with zero padding
print(f"{i:08b}") # '00001101'
# binary with prefix and zero padding
print(f"{i:#08b}") # '0b001101'
# fill (0), align (=), #-option, width (8), type (b)
print(f"{i:0=#8b}") # '0b001101'
# returns the unicode character with decimal representation 36
print(f"{36:c}") # '$'
# printing symbols with unicode decimal representations 33-41
print(''.join([f"{x:c}" for x in range(33, 42)])) # !"#$%&'()
# separator (,) and type (d)
print(f"{10000:,d}") # '10,000'
# type d is the default for integers, so unnecessary
print(f"{10000:,}") # '10,000'
# separator (_), type (b)
print(f"{1200:_b}") # '100_1011_0000'
# to use locale specific number formatting, set the locale
import locale
locale.setlocale(locale.LC_ALL, '')
# then use format type 'n'
print(f"{10 ** 6:n}") # '1,000,000'