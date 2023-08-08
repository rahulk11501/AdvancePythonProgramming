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

    def swap_node(self, x_data: Any, y_data: Any):
        """" swap node """
        if x_data == y_data:
            return
        prev_x = None
        curr_x = self.head
        while curr_x is not None and curr_x.data is not x_data:
            prev_x = curr_x
            curr_x = curr_x.next
        prev_y = None
        curr_y = self.head
        while curr_y is not None and curr_y.data is not y_data:
            prev_y = curr_y
            curr_y = curr_y.next
        if curr_x is None or curr_y is None:
            return

        if prev_x is not None:
            prev_x.next = curr_y
        else:
            self.head = curr_y

        if prev_y is not None:
            prev_y.next = curr_x
        else:
            self.head = curr_y
        temp = curr_x.next
        curr_x.next = curr_y.next
        curr_y.next = temp


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
    print("SWAP NODE")
    list1.swap_node("Sun", "Mon")
    list1.printlist()


exec_ops()
