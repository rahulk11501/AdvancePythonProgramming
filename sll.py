class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class SLL:
  def __init__(self):
    self.head = None


list1 = SLL()
# print(Node("Mon").next)
node1 = Node("Mon")
node2 = Node("Tues")
node3 = Node("Wed")
list1.head = node1

node1.next = node2
print(node2)
print(list1.head.next)
print(node1.next)
node2.next = node3
