# finding the middle node of list

from mimetypes import init
from tkinter.messagebox import NO


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class List:
    def __init__(self) -> None:
        self.root = None

    def insertNode(self, node) -> None:
        if self.root == None:
            self.root = node
        else:
            iter = self.root
            while iter.next != None:
                iter = iter.next
            iter.next = node

    def print(self) -> None:
        iter = self.root
        while iter != None:
            print(iter.data)
            iter = iter.next

    def length(self):
        iter = self.root
        len = 0
        while iter != None:
            len += 1
            iter = iter.next

        return len

    def midElem(self):
        iter1 = self.root
        len = self.length()
        mid = len//2
        for i in range(mid):
            iter1 = iter1.next

        return iter1.data

    def reverse(self):
        if self.root != None:
            iter = self.root

            prev = None
            while iter != None:
                iter1 = iter.next
                iter.next = prev
                prev = iter
                iter = iter1

            self.root = prev

    def midElemFast(self):
        siter = self.root
        fiter = self.root

        while fiter != None and siter != None:
            fiter = fiter.next
            if fiter != None:
                fiter = fiter.next
                siter = siter.next

        return siter.data


if __name__ == '__main__':
    li = List()

    len = 0

    for i in range(1, 11):
        d = Node(i)
        li.insertNode(d)

    # li.print()

    print('list len: ')
    print(li.length())

    print('Middle element:')
    print(li.midElem())

    print(li.midElemFast())

    li.print()
    li.reverse()
    print('reversed:')
    li.print()
