from stack import stack


class queueSt:
    def __init__(self):
        self.stq = stack()
        self.temp = stack()

    def enqueue(self, data):
        self.stq.push(data)

    def dequeue(self):
        if self.stq.size() < 1:
            return

        while self.stq.size() != 1:
            self.temp.push(self.stq.pop())

        elem = self.stq.pop()

        while self.temp.size() != 0:
            self.stq.push(self.temp.pop())

        return elem

    def size(self):
        return self.stq.size()


if __name__ == '__main__':
    qst = queueSt()

    qst.enqueue(100)
    qst.enqueue(200)
    qst.enqueue(300)
    qst.enqueue(400)
    qst.enqueue(500)
    qst.enqueue(600)
    qst.enqueue(700)

    print('dequeue', qst.dequeue())
    print('dequeue', qst.dequeue())
    print('dequeue', qst.dequeue())
    print('dequeue', qst.dequeue())
    print('dequeue', qst.dequeue())
    print('dequeue', qst.dequeue())
    print('dequeue', qst.dequeue())
    print('dequeue', qst.dequeue())
