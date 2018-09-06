class Node:
  def __init__(self, data=None):
    self.data = data
    self.nxt = None

class SinglyLinkedList:

  def __init__(self):
    self.tail = None

  def append(self, data):
    # Encapsulate the data in a Node
    node = Node(data)

    if self.tail == None:
      