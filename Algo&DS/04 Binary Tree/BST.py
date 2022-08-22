from os import remove


class Node:
    def __init__(self, data, parent):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent


class BST:
    def __init__(self):
        self.root = None

    def insert_node(self, data, parent):
        if data < parent.data:
            if parent.left is None:
                parent.left = Node(data, parent)
            else:
                self.insert_node(data, parent.left)
        elif data > parent.data:
            if parent.right is None:
                parent.right = Node(data, parent)
            else:
                self.insert_node(data, parent.right)
        else:
            print('duplicate data', data)

    def insert(self, data):
        if self.root == None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def inorder(self, parent):
        if parent == None:
            return

        self.inorder(parent.left)
        print(parent.data)
        self.inorder(parent.right)

    def traverse(self):
        if self.root:
            self.inorder(self.root)

    def successor(self, node):
        if node.right == None:
            if node.left:
                return node.left
            else:
                return node
        else:
            return self.successor(node.right)

    def remove_node(self, data, node):
        if node is None:
            return
        if data == node.data:
            print('found', data)
            if node.left == None and node.right == None:
                if node.parent.left is node:
                    node.parent.left = None
                else:
                    node.parent.right = None
                del node
            elif node.left and node.right:
                suc = self.successor(node.left)
                node.data, suc.data = suc.data, node.data
                self.remove_node(data, suc)
            else:
                if node.parent.left is node:
                    if node.left:
                        node.parent.left = node.left
                    else:
                        node.parent.left = node.right
                else:
                    if node.left:
                        node.parent.right = node.left
                    else:
                        node.parent.right = node.right

                del node
        elif data < node.data:
            self.remove_node(data, node.left)
        else:
            self.remove_node(data, node.right)

    def remove(self, data):
        self.remove_node(data, self.root)


if __name__ == '__main__':
    bst = BST()
    bst.insert(500)
    bst.insert(250)
    bst.insert(750)
    bst.insert(125)
    bst.insert(375)
    bst.insert(600)
    bst.insert(800)
    bst.insert(900)

    bst.traverse()
    bst.remove(750)
    bst.traverse()
