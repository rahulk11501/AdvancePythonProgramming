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
    prev = None
    head_val = self.head
    if head_val.data == remove_data:
      self.head = head_val.next
      del head_val
      return
    while head_val and head_val.data:
      print("reached", head_val.data)
      if head_val.data == remove_data:
        break
      prev = head_val
      head_val = head_val.next
      
    if prev:
      prev.next = head_val.next
      del head_val
    
  def list_len(self):
    curr = self.head
    count = 0
    while curr and curr.data:
      count +=1
      curr = curr.next
    print(count)


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

print("*******  List 1  **********")
list1.printlist()
print("*******  List 2  **********")
list2.printlist()
print("**. Del node **************")
list1.del_node("Mon")

print("******** updated ***********")
list1.printlist()
list1.list_len()