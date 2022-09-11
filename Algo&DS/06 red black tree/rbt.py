class COLOR:
    RED = 'red'
    BLACK = 'black'


class Node:
    def __init__(self, data, parent=None) -> None:
        self.left = None
        self.right = None
        self.parent = parent
        self.color = COLOR.RED
        self.data = data


class RBT:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            self.root.color = COLOR.BLACK
        else:
            self.insert_node(self.root, data)

    def IsRed(self, node):
        if node:
            return node.color == COLOR.RED
        else:
            return False

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

    def fix_RedBlack_Tree(self, node):
        parent = node.parent
        grandParent = parent.parent
        uncle = None

        while node != self.root and self.IsRed(node) and self.IsRed(node.parent):
            parent_node = node.parent
            grand_parent_node = parent_node.parent

            if parent_node == grand_parent_node.left:
                uncle = grand_parent_node.right

                if uncle and self.IsRed(uncle):
                    print('recoloring node %s to RED' % parent_node.data)
                    grand_parent_node.color = COLOR.RED
                    print('re-coloring node %s to BLACK' % parent_node.data)
                    parent_node.color = COLOR.BLACK
                    uncle.color = COLOR.BLACK
                    node = grand_parent_node
                else:
                    if node == parent_node.right:
                        self.rightRotate(parent_node)
                        node = parent_node
                        parent_node = node.parent

                    parent_node.color = COLOR.BLACK
                    grand_parent_node.color = COLOR.RED
                    print('recoloring %s to BLACK' % parent_node.data)
                    print('recolor %s to READ' % grand_parent_node.data)
                    self.rightRotate(grand_parent_node)

            else:
                uncle = grand_parent_node.left

                if uncle and self.IsRed(uncle):
                    print('recoloring node %s to RED' % parent_node.data)
                    grand_parent_node.color = COLOR.RED
                    print('re-coloring node %s to BLACK' % parent_node.data)
                    parent_node.color = COLOR.BLACK
                    uncle.color = COLOR.BLACK
                    node = grand_parent_node
                else:
                    if node == parent_node.left:
                        self.rightRotate(parent_node)
                        node = parent_node
                        parent_node = node.parent

                    parent_node.color = COLOR.BLACK
                    grand_parent_node.color = COLOR.RED
                    print('recoloring %s to BLACK' % parent_node.data)
                    print('recolor %s to READ' % grand_parent_node.data)
                    self.leftRotate(grand_parent_node)

        if self.IsRed(self.root):
            print('recoloring the root to black..')
            self.root.color = COLOR.BLACK

    def insert_node(self, node, data):
        if data < node.data:
            if node.left:
                return self.insert_node(node.left, data)
            else:
                node.left = Node(data, node)
                self.Is_RedBlack_Tree(node.left)
        elif data > node.data:
            if node.right:
                return self.insert_node(node.right, data)
            else:
                node.right = Node(data, node)
                self.fix_RedBlack_Tree(node.right)


if __name__ == '__main__':
    rbt = RBT()
    rbt.insert(1)
    rbt.insert(2)
    rbt.insert(3)
    rbt.insert(4)
    rbt.insert(5)
    rbt.insert(6)
    rbt.insert(7)
    rbt.insert(8)
