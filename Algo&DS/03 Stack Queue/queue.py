import re


class queue:
    def __init__(self):
        self.list = []

    def push(self, data):
        self.list.insert(0, data)

    def pop(self):
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

    qu.push(100)
    qu.push(200)
    qu.push(300)
    qu.push(400)
    qu.push(500)
    qu.push(600)

    print('size', qu.size())
    print('pop', qu.pop())
    print('size', qu.size())
    print('front', qu.front())
    print('back', qu.back())
    print('empty', qu.empty())
    print('pop', qu.pop())
