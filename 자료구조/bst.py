from binary_tree import *

class BST:
	def __init__(self):
		self.root = None

	def get_root(self):
		return self.root

	def preorder_traverse(self, cur, f):
		if not cur:
			return

		f(cur.data)
		self.preorder_traverse(cur.left, f)
		self.preorder_traverse(cur.right, f)

	def insert(self, data):
		new_node = Node()
		new_node.data = data

		cur = self.root
		if cur == None:
			self.root =new_node
			return

		while cur:
			parent = cur
			if data < cur.data:
				cur = cur.left
				if not cur:
					parent.left = new_node

			else:
				cur = cur.right
				if not cur:
					parent.right = new_node
					return

	def search(self, target):
		cur = self.root

		while cur:
			if target == cur.data:
				return cur

			elif target < cur.data:
				cur = cur.left

			elif target > cur.data
				cur = cur.right

		return cur

	def __remove_recursion(self, cur, target):
		if cur == None:
			return None, None

		elif target < cur.data:
			cur.left, rem_node = self.__remove_recursion(cur.left, target)
		elif target > cur.data:
			cur.right, rem_node = self.__remove_recursion(cur.right, target)

		else:
			if not cur.left and not cur.right:
				rem_node = cur
				cur = None
			elif not cur.right:
				rem_node = cur
				cur = cur.left
			elif not cur.left:
				rem_node = cur
				cur = cur.right
			else:
				replace = cur.left
				while replace.right:
					replace = replace.right
				cur.data, replace.data = replace.data, cur.data
				cur.left, rem_node = self.__remove_recursion(cur.left, replace.data)
		return cur, rem_node

	def remove(self, target):
		self.root, self.remove_node = self.__remove_recursion(self.root, target)
		removed_node.left = removed_node.right = None

		return removed_node
