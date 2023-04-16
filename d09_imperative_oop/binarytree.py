def xor(a, b):
	return ( (a or b) and not (a and b) )


class TreeNode:
	"""Node of Binary Search Tree. It takes a value to store as data and creates two children whithin a list,
	each of them initialised to None. """
	def __init__(self, value):  #, lr_index = []):
		self.data = value
		self.left_right = [None, None] # left, right


	def search(self, value):
		"""Returns the descendant node whose data match the given value or 'None' if not found."""
		if value == self.data:
			return self
		lr_index = int(value > self.data)
		if self.left_right[lr_index] is None:
			return None
		return self.left_right[lr_index].search(value)


	def insert(self, value):
		"""Inserts a new node with the given data in an inorder way and returns the inserted new node."""
		lr_index = int(value > self.data)
		if self.left_right[lr_index] is None:
			self.left_right[lr_index] = TreeNode(value) #, self.breadcrumb + [bool(lr_index)])
			return self.left_right[lr_index]
		self.left_right[lr_index].insert(value)


	def inorder_traverse(self):
		"""This function is a generator recursively yielding all descendant nodes in inorder way."""
		if self.left_right[0] is not None:
			yield from self.left_right[0].inorder_traverse()
		yield self
		if self.left_right[1] is not None:
			yield from self.left_right[1].inorder_traverse()


	def ordered_array(self):
		"""Iterates all the node data yielding them in inorder way."""
		return (node.data	for node in self.inorder_traverse())



class BSTree:
	"""Composite class of TreeNode with a unique attribute, 'root' as the TreeNode object."""
	def __init__(self, values):
		"""Initialises the tree from a list of values by creating a root node and inserting the rest of the values to it."""
		self.root = TreeNode(values[0])
		for n in values[1:]:
			self.root.insert(n)

	#XXX Pending to be tested. TO DO: return 'None' when the value does not belong to any descendant.
	def subtree(self, value):
		"""Returns a whole new subtree from a given value of a descendant of root."""
		return BSTree( [node.data for node in self.root.search(value).inorder_traverse()])


	def breadcrumb(self, value):
		"""Generates for the descendant node with a matching value a 'breadcrumb' list path
		of booleans corresponding to left(0) and right(1) values. This information is required for other methods.
		The meaning of the path represents the way to get from the root node to the desired one."""
		path = []
		def build_path(node, value):
			nonlocal path
			if node.data == value:
				return path
			lr_index = int(value > node.data)
			if node.left_right[lr_index] is None:
				return None #[]
			path += [lr_index]
			return build_path(node.left_right[lr_index], value)
		return build_path(self.root, value)


	def prefix(self, value):
		"""This function returns a single line of a drawing of the tree structure as a string.
		It requires the value of the node to be printed out as well as the 'breadcrumb'
		method to perform intermediate calculations. Also, a xor function is required.
		It generates the drawing with some Unicode symbols of the drawing-box type."""
		breadcrumb = self.breadcrumb(value)
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
		"""This method returns the whole sketch of the tree as a multiline string by calling the 'prefix' method."""
		out = ''
		for node in self.root.inorder_traverse():
			out += self.prefix(node.data) + str(node.data) + '\n'
		return out


	# def get_node(self, given_breadcrumb, position = None):
	# 	if position is None:
	# 		self_breadcrumb_len = len(self.breadcrumb)
	# 		for position in range(self_breadcrumb_len):
	# 			if self.breadcrumb[position] != given_breadcrumb[position]:
	# 				raise AttributeError('Given Breadcrumb is incompatible with current Tree')
	# 	if len(given_breadcrumb) - 1 - position:
	# 		lr_index = given_breadcrumb[position]
	# 		return self.left_right[int(lr_index)].get_node(given_breadcrumb, position + 1)
	# 	return self


if __name__ == '__main__':
	my_tree = BSTree([5, 2, 10, 7, 15, 12, 20, 30, 6, 8])
	print(my_tree)
	print([n for n in my_tree.root.ordered_array()])


#   ┌─: 2
# :5
#   │         ┌─: 6
#   │    ┌─: 7
#   │    │    └─: 8
#   └─: 10
#        │    ┌─: 12
#        └─: 15
#             └─: 20
#                  └─: 30


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