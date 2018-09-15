class Stack(object):
	
	def __init__(self):
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


class Queue(object):

	def __init__(self):
		self.items = []

	def enqueue(self, elem):
		self.items.index(0, elem)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

	def isEmpty(self):
		return self.items == []

	def peak(self):
		return self.items[self.items[0]]


class Dequeue(object):

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []