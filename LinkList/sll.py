# Single Link List Implementation
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class SLL:
  def __init__(self):
    self.head = None

  def printlist(self):
    output = self.head
    while output is not None:
      print(output.data)
      output = output.next

  def at_end(self, new_data):
    new_node = Node(new_data)
    if self.head is None:
      self.head = new_node
    else:
      tail = self.head
      while tail.next:
        tail = tail.next
      tail.next = new_node

  def at_start(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node

  def at_middle(self, middle_node, new_data):
    new_data = Node(new_data)
    new_data.next = middle_node.next
    middle_node.next = new_data.next
  
  def del_node(self, remove_data):
    curr = self.head
    while curr and curr.data:
      print(curr.data)
      if curr.data == remove_data:
        curr.data = None
      curr = curr.next




list1 = SLL()
# print(Node("Mon").next)
node1 = Node("Mon")
node2 = Node("Tues")
node3 = Node("Wed")
list1.head = node1

node1.next = node2

# Following all print same value
print(node2)
print(list1.head.next)
print(node1.next)

node2.next = node3

list1.at_end("Thurs")
list1.at_end("Fri")

list2 = SLL()

list2.at_end("Sat")
list1.at_start("Sun")
list1.del_node("Mon")
print("*******  List 1  **********")
list1.printlist()
print("*******  List 2  **********")
list2.printlist()