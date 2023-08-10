"""Deletion operation for double link list"""
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
   
    def __repr__(self) -> str:
        pass

    def delete_at_end(self):
        """ Funtion deletes a node at end of DLL"""
        ptr = self.head
        while ptr is not None:
            if ptr.next is None and ptr.prev:
                ptr = ptr.prev
                ptr.next = None
            else:
                # print("ptr.data", ptr.data)
                ptr = ptr.next
    
    def delete_at_start(self):
        """ Function deletes node at start of DLL """
        ptr = self.head.next
        ptr.prev = None
        self.head = ptr
    
    def delete_at_middle(self, data):
        """ Function deletes any node of DLL """
        ptr = self.head
        while ptr.next is not None:
            if ptr.data == data:
                temp = ptr
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                ptr = ptr.next
                del(temp)
            else:
                ptr = ptr.next

    def append_at_end(self, data):
        """ Function appends a node at end """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = new_node
            new_node.prev = ptr

    def print_list(self):
        """ Funtion prints the nodes of the list """
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next

def main():
    """ evals to test functionality """
    d_list = DLL()
    d_list.append_at_end("Sun")
    d_list.append_at_end("Mon")
    d_list.append_at_end("Tue")
    d_list.append_at_end("Wed")
    d_list.append_at_end("Thu")
    d_list.append_at_end("Fri")
    d_list.append_at_end("Sat")
    d_list.print_list()
    print("***** Delete at end ********")
    d_list.delete_at_start()
    d_list.delete_at_middle("Wed")
    d_list.print_list()
main()
    