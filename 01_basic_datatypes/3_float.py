## Indeterminate (nan) forms: 0/0, ∞/∞, 0*∞, ∞ - ∞, 0^0, 1^∞, ∞^0
import math

inf = float('inf')
_inf = float('-inf')
nan = float('nan')
print(inf, _inf, nan)
nan = math.nan
print(math.isnan(nan))
divission = 4 / 3;  print('divission: ', divission)

print(inf + _inf) # nan

x = -0.00345E-12
print(x)

x = 20
print(f'value: {x}')
print(f'value: {x=}')

normal_num = 7.5
print(f'{normal_num}')
padded_num = 9.5
print(f'{padded_num:8}')
print(f'{normal_num}')
right_num = 12.5
print(f'{right_num:>8}')
print(f'{normal_num}')
left_num = 5.4
print(f'{left_num=:_<7}')
x = 20.123
print(f'{x:0<8}')
print(f'{x:.5f}')
print(f'{x:.1f}')
x = 1000000
print(f'{x:,}')


# sign (+): a sign is attached to both positive and negative numbers
print(f"{3:+} or {-3:+}") # '+3 or -3'
# sign (-): a sign is only used for negative numbers
print(f"{3:-} or {-3:-}") # '3 or -3'
# no sign is the same as sign (-)
print(f"{3} or {-3}") # '3 or -3'
# sign (space): a leading space for positive numbers and a minus sign for negative
print(f"{3: } or {-3: }") # ' 3 or -3'
# sign (+), separator (,)
print(f"{10000:+,}") # '+10,000'
# fill (?), align (<), sign (+), width (11), sep (,)
print(f"{10000:?<+11,}") # '+10,000????'
# fill (?), align (=), sign (+), width (5)
print(f"{3:?=+5}") # '+???3'
# fill (0), align (=), sign (+), width (5)
print(f"{3:0=+5}") # '+0003'
# sign (+), 0-option, width (5)
print(f"{3:+05}") # '+0003'
# 0-option, width (5)
print(f"{3:05}") # '00003'

# %-style with precision=1
print(f"{1/2:.1%}") # '50.0%'
# Lower case e versus upper case E
print(f"{1000:.1e} vs {1000:.1E}") # '1.0e+03 vs 1.0E+03'
# Lower case f versus upper case F
print(f"{1000:.1f} vs {1000:.1F}") # '1000.0 vs 1000.0'
# Lower case g versus upper case G
print(f"{1000:.1g} vs {1000:.1G}") # '1e+03 vs 1E+03'
# Lower versus upper case NaN representation
nan = float('nan')
print(f"{nan:f} vs {nan:F}") # 'nan vs NAN'

si = 55   # small integer
li = 666666   # large integer
sf = 7.77777   # small float
lf = 8888.88   # large float
sc = 9e6   # scientific notation
# none -- no type specified
print(f"{si}  {li}  {sf}  {lf}  {sc}") # '55   666666   7.77777   8888.88   9000000.0'
# n -- number type
print(f"{si:n}  {li:n}  {sf:n}  {lf:n}  {sc:n}") # '55   666666   7.77777   8888.88   9e+06'
# n with #-option
print(f"{si:#n}  {li:#n}  {sf:#n}  {lf:#n}  {sc:#n}") # '55   666666   7.77777   8888.88   9.00000e+06'
# n with precision = 3 (precision not allowed for integers)
#XXX print(f"{si:.3n}  {li:.3n}  {sf:.3n}  {lf:.3n}  {sc:.3n}") # 
# e with precision = 3 (forces 3 digits after decimal point)
print(f"{si:.3e}  {li:.3e}  {sf:.3e}  {lf:.3e}  {sc:.3e}")
# including the #-option gives the same result here
print(f"{si:#.3e}  {li:#.3e}  {sf:#.3e}  {lf:#.3e} {sc:#.3e}") # '5.500e+01   6.667e+05   7.778e+00   8.889e+03   9.000e+06'
# f with precision = 3 (forces 3 digits after decimal point)
print(f"{si:.3f}  {li:.3f}  {sf:.3f}  {lf:.3f}  {sc:.3f}" )
# including the #-option gives the same result here
print("{si:#.3f}  {li:#.3f}  {sf:#.3f}  {lf:#.3f}  {sc:#.3f}") # '55.000   666666.000   7.778   8888.880   9000000.000'
# g with precision = 3 (shows no unnecesary zeros or decimal points)
print(f"{si:.3g}  {li:.3g}  {sf:.3g}  {lf:.3g}  {sc:.3g}") # '55   6.67e+05   7.78   8.89e+03   9e+06'
# g with #-option (forces showing 3 significant digits)
print(f"{si:#.3g}  {li:#.3g}  {sf:#.3g}  {lf:#.3g}  {sc:#.3g}") #'55.0   6.67e+05   7.78   8.89e+03   9.00e+06'
# In float types generally, the #-option forces a decimal point occurrence even when no digits follow it
print(f"{10:#.0e}  {10:#.0f}  {10:#.0g}") # '1.e+01   10.   1.e+01'

print('int attrs:\n',  '\n'.join(dir(float)))