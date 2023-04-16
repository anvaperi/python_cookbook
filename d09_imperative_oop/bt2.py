def xor(a, b):
	return ( (a or b) and not (a and b) )

class TreeNode:
	"""Node of Binary Search Tree. """
	def __init__(self, value, lr_index = []):
		self.data = value
		self.left_right = [None, None] # left, right
		self.breadcrumb = lr_index

	#@property
	#def breadcrumb(self):

	def search(self, value):


	def insert(self, value):
		lr_index = int(value > self.data)
		if self.left_right[lr_index] is None:
			self.left_right[lr_index] = TreeNode(value, self.breadcrumb + [bool(lr_index)])
			return self.left_right[lr_index]
		self.left_right[lr_index].insert(value)


	def inorder_traverse(self):
		if self.left_right[0] is not None:
			yield from self.left_right[0].inorder_traverse()
		yield self
		if self.left_right[1] is not None:
			yield from self.left_right[1].inorder_traverse()


	def as_array(self):
		node = self
		while node is not None:
			yield node.data
			node = next(node.inorder_traverse(), None)


	# def get_node(self, given_breadcrumb, position = None): # MOVE TO TREE CLASS
	# 	if position is None:
	# 		self_breadcrumb_len = len(self.breadcrumb)
	# 		for position in range(self_breadcrumb_len):
	# 			if self.breadcrumb[position] != given_breadcrumb[position]:
	# 				raise AttributeError('Given Breadcrumb is incompatible with current Tree')
	# 	if len(given_breadcrumb) - 1 - position:
	# 		lr_index = given_breadcrumb[position]
	# 		return self.left_right[int(lr_index)].get_node(given_breadcrumb, position + 1)
	# 	return self

	def prefix(self):
		breadcrumb = self.breadcrumb
		breadcrumb_len = len(breadcrumb)
		if not breadcrumb_len:
			return ':'
		prefix = ''
		if breadcrumb_len > 1:
			for lr in range(breadcrumb_len - 1):
				prefix += '  │  ' if xor(breadcrumb[lr], breadcrumb[lr + 1]) else '     '
		prefix += '  └' if breadcrumb[-1] else '  ┌'
		return prefix + '─: '

	def __str__(self):
		out = ''
		for node in self.inorder_traverse():
			out += node.prefix() + str(node.data) + '\n'
		return out

my_tree = TreeNode(5)

for n in [2, 10, 7, 15, 12, 20, 30, 6, 8]:
	my_tree.insert(n)

print(my_tree)


# Your updated code looks good! Here are a few suggestions to consider:
#
# Commenting your code can help improve its readability and maintainability.
# You may want to consider adding comments to explain what each function does,
# its inputs and outputs, and any other important details.
#
# You can consider using a property decorator to compute the breadcrumb attribute on-the-fly
# instead of storing it as an instance variable. This can help simplify the TreeNode constructor and
# also ensure that the breadcrumb attribute is always up-to-date with the node's position in the tree.
#
# Instead of defining a separate get_node function, you can add a __getitem__ method to the TreeNode class
# to allow indexing into the tree using the breadcrumb list.
#
# You may want to consider adding a __repr__ method to the TreeNode class to provide a more detailed
# representation of the node when printed in the console.