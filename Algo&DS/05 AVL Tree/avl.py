class Node:
    def __init__(self, data, parent) -> None:
        self.data = data
        self.parent = parent
        self.height = 0
        self.left = None
        self.right = None

    def print(self):
        print('data', self.data, ' height', self.height)


class AVLTree:
    def __init__(self) -> None:
        self.root = None

    def getBalanceFactor(self, node):
        if node is None:
            return 0
        else:
            factor = self.getHeight(node.left)-self.getHeight(node.right)

        return factor

    def rightRotate(self, node):
        print('right rotate')
        P = node.parent
        if P:
            if P.left is node:
                A = node
                B = node.left

                P.left = B
                B.parent = P

                temp = B.right
                B.right = A
                A.left = temp

                A.parent = B
            else:
                A = node
                B = node.left

                P.right = B
                temp = B.right
                B.right = A
                A.left = temp

                A.parent = B
        else:
            A = node
            B = node.left

            self.root = B
            B.parent = None
            temp = B.right
            B.right = A
            A.left = temp

            A.parent = B

        A.height = max(self.getHeight(A.left), self.getHeight(A.right)) + 1
        B.height = max(self.getHeight(B.left), self.getHeight(B.right)) + 1

    def leftRotate(self, node):
        print('left rotate')
        P = node.parent
        if P:
            if P.left is node:
                B = node
                A = node.right

                P.left = A
                A.parent = P

                temp = A.left
                A.left = B
                B.right = temp

                B.parent = A
            else:
                B = node
                A = node.right

                P.right = A
                A.parent = P

                temp = A.left
                A.left = B
                B.right = temp

                B.parent = A
        else:
            B = node
            A = node.right

            self.root = A
            A.parent = None

            temp = A.left
            A.left = B
            B.right = temp

            B.parent = A

        A.height = max(self.getHeight(A.left), self.getHeight(A.right)) + 1
        B.height = max(self.getHeight(B.left), self.getHeight(B.right)) + 1

    def validateAVL(self, node):
        while node:
            node.print()
            node.height = max(self.getHeight(node.left),
                              self.getHeight(node.right))+1

            balanceFactor = self.getBalanceFactor(node)

            if balanceFactor > 1:
                if self.getBalanceFactor(node.left) < 0:
                    self.leftRotate(node.left)
                self.rightRotate(node)
            elif balanceFactor < -1:
                if self.getBalanceFactor(node.right) > 0:
                    self.rightRotate(node.right)
                self.leftRotate(node)

            node = node.parent

    def getHeight(self, node):
        if node is None:
            return -1

        return node.height

    def insert_node(self, data, parent):
        if data < parent.data:
            if parent.left is None:
                parent.left = Node(data, parent)
                parent.height = max(self.getHeight(
                    parent.left), self.getHeight(parent.rigt))+1
            else:
                return self.insert_node(data, parent.left)
        elif data > parent.data:
            if parent.right is None:
                parent.right = Node(data, parent)
            else:
                return self.insert_node(data, parent.right)

        self.validateAVL(parent)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def traverse(self):

        print('inorder')
        self.inorder(self.root)

    def inorder(self, node):
        if node is None:
            return

        self.inorder(node.left)
        node.print()
        self.inorder(node.right)


if __name__ == '__main__':
    avl = AVLTree()

    avl.insert(10)
    avl.insert(20)
    avl.insert(30)
    avl.insert(40)
    avl.insert(50)
    avl.insert(60)
    avl.insert(70)
    avl.insert(80)

    avl.traverse()
