# Boolean literals are 'False' and 'True'

empty_list = []
empty_tuple = ()
empty_dictionary = {}
empty_set = set()
empty_string = ""
empty_range = range(0)
zero_integer = 0
zero_float = 0.0
zero_complex = 0j
const_none = None
const_flase = False
falsies = (empty_list, empty_tuple, empty_dictionary, empty_set, empty_string, empty_range, zero_integer,
           zero_float, zero_complex, const_none, const_flase)

non_empty_seq_or_collection = [[1, 2]]
non_zero_nums = 8
const_true = True
truthies = [non_empty_seq_or_collection, non_zero_nums, const_true]

eq = 5 == 6
ne = 4 != 9
gt = 4 > 2
ge = 3 >= 1
lt = 1 < 9
le = 0 <= 2
match = 'a' in 'abc'
not_match = 'w' not in 'abc'
any_op = any([False, False, True])
all_op = all([True, True, True])
conditions = [eq, ne, gt, ge, lt, le, match, not_match, any_op, all_op]

print('falsies: ',    [bool(to_check) for to_check in falsies])
print('truthies: ',   [bool(to_check) for to_check in truthies])
print('conditions: ', [bool(to_check) for to_check in conditions])
print('bool attrs:\n',  '\n'.join(dir(bool)))
