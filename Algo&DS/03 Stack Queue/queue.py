import re


class queue:
    def __init__(self):
        self.list = []

    def enqueue(self, data):
        self.list.insert(0, data)

    def dequeue(self):
        if len(self.list):
            return self.list.pop()

    def front(self):
        if len(self.list):
            return self.list[-1]

    def back(self):
        if len(self.list):
            return self.list[0]

    def size(self):
        return len(self.list)

    def empty(self):
        return len(self.list) == 0


if __name__ == '__main__':
    qu = queue()

    qu.enqueue(100)
    qu.enqueue(200)
    qu.enqueue(300)
    qu.enqueue(400)
    qu.enqueue(500)
    qu.enqueue(600)

    print('size', qu.size())
    print('dequeue', qu.dequeue())
    print('size', qu.size())
    print('front', qu.front())
    print('back', qu.back())
    print('empty', qu.empty())
    print('dequeue', qu.dequeue())
