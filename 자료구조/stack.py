class Stack:
	def __init__(self):
		self.container = list()

	def push(self, d):
		self.container.append(d)

	def pop(self):
		return self.container.pop()

	def empty(self):
		if self.container:
			return False
		else:
			return True

	def peek(self):
		return self.container[-1]


if __name__ == '__main__':
	s = Stack()
	s.push(1)
	s.push(2)
	s.push(3)
	s.push(4)
	s.push(5)

	while not s.empty():
		data = s.pop()
		print(data)
