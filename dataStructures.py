class Stack(object):
	self.items = []

	def push(self, elem):
		self.items.append(elem)

	def size(self):
		return len(self.items)