"""Insertion operations for double link list"""
from typing import Any

class Node:
    """Class representing a Node"""
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None

    def __repr__(self) -> str:
        pass

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass


class DLL():
    """ Class representing a Double link list and related operations """
    def __init__(self) -> None:
        self.head = None

    def append_at_end(self, data):
        """Function adding node at end"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
    
    def append_at_start(self, data):
        """ Function adding node at start """
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def append_in_between(self, data, after):
        """ Function appends node after given node """
        new_node = Node(data)
        ptr1 = self.head
        ptr2 = None
        while ptr1.next:
            if ptr1.data == after:
                ptr2 = ptr1.next
                ptr1.next = new_node
                new_node.next = ptr2
                new_node.prev = ptr1
                ptr2.prev = new_node
            else:
                ptr1 = ptr1.next


    def print_list(self):
        """Function print the double list"""
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next


def main():
    """Function to perform different DLL methods"""
    d_list = DLL()
    d_list.append_at_start("Mon")
    d_list.append_at_start("Sun")
    d_list.append_at_end("Tue")
    d_list.append_at_end("Wed")
    d_list.append_at_end("Fri")
    d_list.append_in_between("Thu", "Fri")
    d_list.print_list()


main()
