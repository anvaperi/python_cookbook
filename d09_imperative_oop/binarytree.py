from enum import Enum

#__________________________________________________________________

def xor(a, b):
	return ( (a or b) and not (a and b) )
#__________________________________________________________________

class Data:
	__name__ = 'Data'
	def __init__(self, value, leader=None):
		if leader is not None:
			self.leader = leader
			self.value  = value
		else:
			self.leader = value

	def __str__(self):
		if hasattr(self, 'value'):
			return str(self.leader) + ': ' + str(self.value)
		return str(self.leader)
#_________________________________________________________________

class Side(Enum):
	L = False
	R = True

get_side = lambda condition: Side.L if not condition else Side.R
oposite_side = lambda side: Side.R if side == Side.L else Side.L
side_as_bool = lambda side: False if side == Side.L else True

#_________________________________________________________________

class TreeNode:
	"""Node of Binary Search Tree. It takes a value to store as data and creates two children within a list,
	each of them initialised to None. """
	__name__ = 'Binary search tree node'
	__slots__ = 'data', 'child_left', 'child_right'

	def __init__(self, data):
		"""Initialises TreeNode assigning the value of parameter 'data' to its corresponding property,
		leaving both children as 'None'.
		It is important to notice that parameter data is an object of the previously defined class 'Data'."""
		self.data = data
		self.child_left = None
		self.child_right = None

	def get_child(self, side):
		"""Returns the corresponding child node according to the value of parameter 'side',
		which is an object of enumeration Side accepting as values 'L' for 'left' and 'R' for 'right'. """
		if side == Side.L:
			return self.child_left
		return self.child_right

	def add_child(self, side, data):
		"""Creates a new TreeNode and inserts it to the current one on the side specified by the parameter 'side'.
		After that the inserted node is returned."""
		return self.append_child(side, TreeNode(data))

	def append_child(self, side, other):
		if side == Side.L:
			self.child_left = other
		else:
			self.child_right = other
		return self

	def insert(self, data):
		"""Inserts a new node with the given data in an inorder way and returns the inserted new node."""
		side = get_side(data.leader >= self.data.leader)
		if self.get_child(side) is None:
			return self.add_child(side, data).get_child(side)
		self.get_child(side).insert(data)

	def search(self, lead_value):
		"""Returns the descendant node whose data match the given value or 'None' if not found."""
		if lead_value == self.data.leader:
			return self
		side = get_side(lead_value > self.data.leader)
		if self.get_child(side) is None:
			return None
		return self.get_child(side).search(lead_value)


	def inorder_traverse(self, path=[]):
		"""This function is a generator recurively yielding all descendant nodes in inorder way
		as well as the path to reach each descendant of the current node as a list of values 'Side.L' and 'Side.R'.
		Although a mutable argument '[]' is given as default value for parameter 'path' it is necessary to get this
		method 'inorder_traverse' behaving as an state function during recursion in order to get the appropriate paths
		to each descendant."""
		if self.child_left is not None:
			yield from self.child_left.inorder_traverse(path + [Side.L])
		yield (self, path)
		if self.child_right is not None:
			yield from self.child_right.inorder_traverse(path + [Side.R])

	def ordered_array(self):
		"""Iterates all the node data yielding them in inorder way."""
		if hasattr(self.data, 'value'):
			return (node.data.value for node, _ in self.inorder_traverse())
		return (node.data.leader	for node, _ in self.inorder_traverse())

	@staticmethod
	def prefix(breadcrumb):
		"""This function returns a single line of a drawing of the tree structure as a string.
		It requires the value of the node to be printed out as well as the 'breadcrumb'
		method to perform intermediate calculations. Also, a xor function is required.
		It generates the drawing with some Unicode symbols of the drawing-box type."""
		# breadcrumb = self.breadcrumb(lead_value, skip)
		breadcrumb_len = len(breadcrumb)
		if not breadcrumb_len:
			return '◆'
		prefix = ''
		if breadcrumb_len > 1:
			for edge_index in range(breadcrumb_len - 1):
				prefix += '  │  ' if xor(
					side_as_bool(breadcrumb[edge_index]),
					side_as_bool(breadcrumb[edge_index + 1])
				) else '     '
		prefix += '  └' if side_as_bool(breadcrumb[-1]) else '  ┌'
		return prefix + '─> '

	def __str__(self):
		"""This method returns the whole sketch of the tree as a multiline string by calling the 'prefix' method.
		The method plots left and right children above and below their parent respectively."""
		out = ''
		for node, node_breadcrumb in self.inorder_traverse(path=[]):
			out += TreeNode.prefix(node_breadcrumb) + str(node.data) + '\n'
		return out

	def rotate(self, child_side, rotation_side=None):
		if rotation_side is None:
			parent_node 	= None
			rotating_node = self
			rotation_side = child_side
		else:
			parent_node 	= self
			rotating_node = self.get_child(child_side)




		# print('================')
		# print(parent_node, rotating_node.data, rotation_side)
		# print('================')
		ascending_child = rotating_node.get_child(oposite_side(rotation_side))
		#print(parent_node, '\n', rotating_node, '\n', ascending_child)

		rotating_node.append_child(oposite_side(rotation_side), ascending_child.get_child(rotation_side))
		ascending_child.append_child(rotation_side, rotating_node)
		if parent_node is not None:
			parent_node.append_child(rotation_side, ascending_child)
		return self


class BSTree:
	"""Composite class of TreeNode with a unique attribute, 'root' as the TreeNode object."""
	def __init__(self, data):
		"""Initialises the tree from a list of values by creating a root node and inserting the rest of the values to it."""
		self.root = TreeNode(data[0])
		for n in data[1:]:
			self.root.insert(n)

	def __str__(self):
		return str(self.root)




if __name__ == '__main__':
	#my_data = [Data(x//2 if not x%2 else x, x) for x in [5, 2, 10, 7, 15, 12, 20, 30, 6, 8]]
	my_data = [Data(x) for x in [5, 2, 10, 7, 15, 12, 20, 30, 6, 8]]
	my_tree = BSTree(my_data)
	#print(my_tree.root.child_left)
	print(my_tree)
	#print([n for n in my_tree.root.ordered_array()])
	#print(TreeNode.__doc__)
	print('L rotation over 10')
	print(my_tree.root.rotate(Side.R, Side.L))


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



	# order = lambda any_list: BSTree(any_list).root.ordered_array()
	# my_list = [4, 1, 6, 2]
	# print()
	# print(f'{my_list=} -> {[n for n in order(my_list)]=}')

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

	# SUITS = '♣♦♥♠'
	# RANKS = 'A23456789XJQK'
	#
	# my_suit = '♠'
	# my_rank =  '5'
	#
	# i = RANKS.index(my_rank) * len(SUITS) + SUITS.index(my_suit)
	# print(f'{i=}')