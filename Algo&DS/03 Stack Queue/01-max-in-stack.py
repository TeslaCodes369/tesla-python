from stack import stack


class stackMax:
    def __init__(self) -> None:
        self.norm_stack = stack()
        self.max_stack = stack()

    def push(self, data):
        if self.norm_stack.size() == 0:
            self.norm_stack.push(data)
            self.max_stack.push(data)
        else:
            self.norm_stack.push(data)

            maxElem = self.max_stack.top()
            if data < maxElem:
                self.max_stack.push(maxElem)
            else:
                self.max_stack.push(data)

    def pop(self):
        if self.norm_stack.size() > 0:
            self.max_stack.pop()
            return self.norm_stack.pop()

    def top(self):
        if self.norm_stack.size() > 0:
            return self.norm_stack.top()

    def empty(self):
        return self.norm_stack.empty()

    def size(self):
        return self.norm_stack.size()

    def max(self):
        return self.max_stack.top()


if __name__ == '__main__':
    mlist = stackMax()

    mlist.push(10)
    mlist.push(101)
    mlist.push(20)
    mlist.push(13)
    mlist.push(1055)
    mlist.push(103)
    mlist.push(1110)
    mlist.push(120)
    mlist.push(102)

    print('size', mlist.size())
    print('max', mlist.max())
    print('pop', mlist.pop())
    print('pop', mlist.pop())
    print('pop', mlist.pop())
    print('pop', mlist.pop())
    print('pop', mlist.pop())
    print('pop', mlist.pop())
    print('size', mlist.size())
    print('max', mlist.max())
