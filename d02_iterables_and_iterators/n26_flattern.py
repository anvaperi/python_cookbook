# def my_func(*args):
#     for arg in args:
#         print(arg, end=' ')
#
# my_func(1, 2, 3, 4, 5, 6) # prints 1 2 3
#
# a, *b, c = "asdfghjkl"
# print(''.join(b))
#

my_list = [1, [2, 3], 4, [5, 6]]
my_sublists = [sublist if type(sublist) == list else [sublist] for sublist in my_list]
flat_list = [item for sublist in my_sublists for item in sublist]
print(flat_list) # prints [1, 2, 3, 4, 5, 6]

my_list = [1, [2, 3], 4, [5, 6]]
flat_list = [item for sublist in my_list for item in (sublist if isinstance(sublist, list) else [sublist])]
print(flat_list)  # prints [1, 2, 3, 4, 5, 6]