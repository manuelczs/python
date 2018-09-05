class Stack(object):
	self.items = []

	def push(self, elem):
		self.items.append(elem)

	def size(self):
		return len(self.items)

	def pop(self):
		return self.items.pop()

	def peak(self):
		return self.items[len(self.items) - 1]

	def isEmpty(self):
		return self.items == []