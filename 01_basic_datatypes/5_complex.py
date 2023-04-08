import math

def real_dom_root(sqrt_f):
  return lambda radicand: sqrt_f(radicand) if radicand >= 0 else 1J*sqrt_f(-radicand)

def real_dom_log(log_f):
  return lambda argument: log_f(argument) if argument > 0 else (math.pi*1J + log_f(-argument)) if argument < 0 else float('-Inf')

@real_dom_root
def sqrt(radicand):
  return math.sqrt(radicand)

@real_dom_log
def log10(argument):
  return math.log(argument, 10)

print('root(-9): ', sqrt(-9))
print('log10(-100): ', log10(-100))

c1 = complex(1, 2)
c2 = 4 + 5j
print(c1, ' = ', c1.real, ' + ', c1.imag, ' i', ' = ', abs(c1), ' ∠ ',math.atan(c1.imag/c1.real), ' rad', sep='')
print(c2, '; ',c2.conjugate())
print('int attrs:\n',  '\n'.join(dir(complex)))
