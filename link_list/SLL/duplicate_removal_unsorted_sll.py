"""Remove duplicates nodes from list"""

class SLL:
    """Class Single Link List"""
    def __init__(self):
        self.head = None

    def at_end(self, new_data):
        """Insert at end"""
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            tail = self.head
            while tail.next:
                tail = tail.next
            tail.next = new_node

    def printlist(self):
        """Print Link List"""
        output = self.head
        while output is not None:
            print(output.data)
            output = output.next

    def remove_dup(self):
        """Remove Duplicates"""
        ptr1, ptr2, dup = None, None, None
        ptr1 = self.head
        while ptr1:
            ptr2 = ptr1
            while ptr2 and ptr2.next:
                if ptr1.data == ptr2.next.data:
                    dup = ptr2.next
                    ptr2.next = ptr2.next.next
                    dup = None
                else:
                    ptr2 = ptr2.next
            ptr1 = ptr1.next
        print("dup", dup)

def exec_ops():
    """"Testing"""
    list1 = SLL()
    # print(Node("Mon").next)
    node1 = Node("Mon")
    node2 = Node("Tues")
    node3 = Node("Wed")
    list1.head = node1

    node1.next = node2
    node2.next = node3

    list1.at_end("Thurs")
    list1.at_end("Fri")
    list1.at_end("Thurs")
    list1.at_end("Fri")
    list1.at_end("Sat")
    list1.at_end("Sun")

    list1.remove_dup()

    list1.printlist()

exec_ops()
