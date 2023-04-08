# integer values under or over zero. Use for discrete mathematical operations or counters
import math
PI = math.pi

x = 3
negated   = -x;     print('Negated: ', negated)
unchanged = +x;     print('unchanged: ', unchanged)
vect_mod  = abs(x); print('vect_mod: ', vect_mod)
sum       = 3 + 4;  print('sum: ', sum)
diff      = 7 - 19; print('diff: ', diff)
product   = 5 * 2;  print('product: ', product)
divission = 4 / 3;  print('divission: ', divission)
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


