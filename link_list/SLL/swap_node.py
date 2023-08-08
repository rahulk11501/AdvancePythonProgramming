"""Swap Node Implementation"""
from typing import Any

class Node:
    """ Create Node """

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        pass

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass



class SLL():
    """ SLL creation """

    def __init__(self):
        self.head = None

    def at_end(self, new_node):
        """ Insert at end of list """
        if not self.head:
            self.head = new_node
        else:
            tail = self.head
            while tail.next:
                tail = tail.next
            tail.next = new_node

    def printlist(self):
        """ Print all nodes of list """
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next
    
    def swap_node(self, x, y):
        """" x and y are same """
        if x == y:
            pass
        """"""
        else

def exec_ops():
    """Testing"""
    list1 = SLL()

    list1.at_end(Node("Sun"))
    list1.at_end(Node("Mon"))
    list1.at_end(Node("Tue"))
    list1.at_end(Node("Wed"))
    list1.at_end(Node("Thu"))
    list1.at_end(Node("Fri"))
    list1.at_end(Node("Sat"))
    list1.printlist()

exec_ops()
