import more_itertools as mit

mylist = [1,2,3,4,5,6,7,8,9,10]
print(list(mit.chunked(mylist, 3))) #[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]

nested_list = [[1,4], [3,8], [1,10]]
nested_tuples_List = [(5,2), (9,2), [1,5]]
print(list(mit.flatten(nested_list))) #[1, 4, 3, 8, 1, 10]
print(list(mit.flatten(nested_tuples_List))) #[5, 2, 9, 2, 1, 5]

mylist = [3, 1, 4, 21, 13, 5]
print(mit.minmax(mylist)) #(1, 21)
mylist = ["A", "C", "Z", "M"]
print(mit.minmax(mylist)) #('A', 'Z')

A = ["John", "Jane"]	# []
B = ["John", "Max"]		# ['Max']
C = ["Jane", "Emily"] # ['Emily']
print(mit.unique_to_each(A, B, C)) # [[], ['Max'], ['Emily']]

print(mit.unique_to_each("John","Jane")) #[['o', 'h'], ['a', 'e']]

