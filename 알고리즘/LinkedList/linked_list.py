from typing import Any, Type


class Node:
	def __init__(self, data, next):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.count = 0
		self.head = None
		self.current = None

	def __len__(self):
		return self.count

	def search(self, data: Any) -> int:
		cnt = 0
		ptr = self.head
		while ptr is not None:
			if ptr.data == data:
				self.current = ptr
				return ptr
			cnt += 1
			ptr = ptr.next
		return -1

	def __contains__(self, data: Any) -> bool:
		return self.search(data) >= 0

	def add_first(self, data: Any) -> None:
		ptr = self.head
		self.head = self.current = Node(data, ptr)
		self.count += 1

	def add_last(self, data: Any):
		if self.head is None:
			self.add_first(data)
		else:
			ptr = self.head
			while ptr.next is not None:
				ptr = ptr.next
			ptr.next = self.current = Node(data, None)
			self.count += 1

	def remove_first(self) -> None:
		if self.head is not None:
			self.head = self.current = self.head.next
		self.count -= 1

	def remove_tail(self) -> None:
		if self.head.next is None:
			self.remove_first()
		else:
			ptr = self.head
			pre = self.head

			while ptr.next is not None:
				pre = ptr
				ptr = ptr.next

			pre.next = None
			self.current = pre
			self.count -= 1
	
	def remove(self, p: Node) -> None:
		if self.head is not None:
			if p is self.head:
				self.remove_first()
			else:
				ptr = self.head

				while ptr.next is not p:
					ptr = ptr.next
					if ptr is None:
						return
				ptr.next = p.next
				self.current = ptr
				self.count -= 1


	def remove_current_node(self) -> None:
		self.remove(self.current)


	def clear(self) -> None:
		while self.head is not None:
			self.remove_first()
		self.current = None
		self.count = 0


	def next(self) -> None:
		if self.current is None or self.current.next is None:
			return False
		self.current = self.current.next
		return True


	def print_current_node(self) -> None:
		if self.current is None:
			print("노드가 존재하지 않습니다.")
		else:
			print(self.current.data)


	def print(self) -> None:
		ptr = self.head

		while ptr is not None:
			print(ptr.data)
			ptr =  ptr.next