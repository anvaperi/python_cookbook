class BinaryTree():
	"""Implementation of a Binary Tree inorder ordered. """
	def __init__(self, value, side=None, parent=None, left=None, right=None):
		self.value = value
		self.children = {'left': left, 'right': right}
		self.parent = parent # is necessary to have the parent to track back during inorder_traversal
		self.side = side # is necessary to know side of current node to skip the value of father
										# when tracking back during inorder_traversal from right child.
		self.depth = 0
		self.height = 0

	def root(self):
		parent = self
		while parent.parent is not None:
			parent = parent.parent
		return parent

	def inorder_traversal(self, skip=False):
		if skip: # When reached by right child, traversal goes upwards.
			yield self.parent.inorder_traversal(self.side=='right')
		elif self.children['left'] is not None:
			yield self.children['left'].inorder_traversal()
		else:
			yield self.value
			if self.children['right'] is not None:
				yield self.children['right'].inorder_traversal()
			else:
				if self.parent is not None:
					yield self.parent.inorder_traversal(self.side=='right')
		return self

	def add_node(self, value):
		if value < self.value:
			if self.children['left'] is None:
				node = BinaryTree(value, side='left',parent=self)
				self.children['left'] = node
			else:
				self.children['left'].add_node(value)
		else: # value > self.value
			if self.children['right'] is None:
				node = BinaryTree(value, side='right', parent=self)
				self.children['right'] = node
			else:
				self.children['right'].add_node(value)
		return self

	#def __str__(self):


bt = BinaryTree(3)
bt.add_node(1)
print(bt.value)



'│─└'