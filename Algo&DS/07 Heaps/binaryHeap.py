CAPACITY = 100


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
        print('Heap Data:')
        for i in range(0, self.index):
            print(self.heap[i], end=' ')
        print('')

    def getMax(self):
        return self.heap[0]

    def fixDown(self, index):
        leftIndex = mHeap.leftChild(index)
        rightIndex = mHeap.rightChild(index)

        if leftIndex > CAPACITY - 1:
            return

        largestIndex = index

        if leftIndex < self.index - 1 and self.heap[largestIndex] < self.heap[leftIndex]:
            largestIndex = leftIndex

        if rightIndex < self.index - 1 and self.heap[largestIndex] < self.heap[rightIndex]:
            largestIndex = rightIndex

        if index != largestIndex:
            self.heap[largestIndex], self.heap[index] = self.heap[index], self.heap[largestIndex]
            self.fixDown(largestIndex)

    def remove(self, index):
        if index <= self.index:
            self.heap[index], self.heap[self.index -
                                        1] = self.heap[self.index-1], self.heap[index]
            self.index -= 1
            self.fixDown(index)

    def poll(self):
        data = self.heap[0]

        self.remove(0)

        return data

    def heap_sort(self):
        print('heap sort:')
        for _ in range(0, self.index):
            print(self.poll(), end=' ')


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

    print('Poll heap', mHeap.poll())
    mHeap.printHeap()

    mHeap.remove(2)
    mHeap.printHeap()

    mHeap.heap_sort()
