# Boolean literals are 'False' and 'True'

from fractions import Fraction
from decimal import Decimal

bool_mark = lambda x: '✓' if x else '✗'

logic_id = lambda x: x
logic_not = lambda x: not x
logic_and = lambda x, y: x and y
nand = lambda x, y: not logic_and(x, y)
logic_or = lambda x, y: x or y
nor = lambda x, y: not logic_or(x, y)
xor = lambda x, y: nand(x,y) and logic_or(x, y)
xnor = lambda x, y: not xor(x, y)
logics = [logic_id, logic_not, logic_and, nand, logic_or, nor, xor, xnor]
print(logics)
print([ ''.join([bool_mark(x), bool_mark(f(x))]) for x in [False, True] for f in logics[:2]])
print([''.join([bool_mark(x), bool_mark(y), bool_mark(f(x,y))]) for x in [False, True] for y in [False, True] for f in logics[2:]])

empty_list = []
empty_tuple = ()
empty_dictionary = {}
empty_set = set()
empty_string = ""
empty_range = range(0)
zero_integer = 0
zero_float = 0.0
zero_decimal = Decimal(0)
zero_fraction = Fraction(0, 1)
zero_complex = 0j
const_none = None
const_flase = False
falsies = (empty_list, empty_tuple, empty_dictionary, empty_set, empty_string, empty_range, zero_integer,
           zero_float, zero_decimal, zero_fraction, zero_complex, const_none, const_flase)
print('falsies: ',    ''.join([bool_mark(bool(to_check)) for to_check in falsies]))

non_empty_seq_or_collection = [[1, 2]]
non_zero_nums = 8
const_true = True
truthies = [non_empty_seq_or_collection, non_zero_nums, const_true]
print('truthies: ',   ''.join([bool_mark(bool(to_check)) for to_check in truthies]))

eq = 5 == 6
ne = 4 != 9
gt = 4 > 2
ge = 3 >= 1
lt = 1 < 9
le = 0 <= 2
match = 'a' in 'abc'
not_match = 'w' not in 'abc'
op_is = eq is ne
op_isnot = eq is not ne
op_any = any([False, False, True])
op_all = all([True, True, True])
conditions = [eq, ne, gt, ge, lt, le, match, not_match, op_is, op_isnot, op_any, op_all]
print('conditions: ', ''.join([bool_mark(bool(to_check)) for to_check in conditions]))

## Some classes have the methods:  __eq__(), __lt__(), __le__(), __gt__(), __ge__()

print('bool attrs:\n',  '\n'.join(dir(bool)))
