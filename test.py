check = [True, False, True]
ns = [1, 2, 3]

print([n for n, check in zip(ns, check) if check])

print([i for i in filter(lambda x: check[ns.index(x)] , ns)])