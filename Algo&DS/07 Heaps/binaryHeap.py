from select import select


CAPACITY = 10


class MaxHeap:
    def __init__(self) -> None:
        self.heap = [0] * CAPACITY
        self.index = 0

    def fix_up(self, index):
        parent = self.parentIndex(index)

        if parent >= 0 and self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.fix_up(parent)

    def insert(self, data):
        if self.index >= CAPACITY:
            print('heap is full.')
            return

        self.heap[self.index] = data
        self.index += 1

        self.fix_up(self.index - 1)

    def parentIndex(self, index):
        return (index - 1)//2

    def leftChild(self, index):
        return index*2 + 1

    def rightChild(self, index):
        return index*2 + 2

    def printHeap(self):
        print(self.heap)

    def getMax(self):
        return self.heap[0]


if __name__ == '__main__':
    mHeap = MaxHeap()
    mHeap.insert(1)
    mHeap.insert(2)

    mHeap.printHeap()
    mHeap.insert(3)
    mHeap.insert(4)
    mHeap.insert(5)
    mHeap.insert(6)
    mHeap.printHeap()

    print('Max Element', mHeap.getMax())
    mHeap.insert(7)
    mHeap.insert(8)

    mHeap.printHeap()

    print('Max Element', mHeap.getMax())
