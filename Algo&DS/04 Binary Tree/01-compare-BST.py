from operator import truediv
from BST import BST


def BST_compare(tree1, tree2):
    if not tree1 or not tree2:
        return tree1 == tree2

    if tree1.data != tree2.data:
        return False

    return BST_compare(tree1.left, tree2.left) and BST_compare(tree1.right, tree2.right)


if __name__ == '__main__':
    bst1 = BST()
    bst1.insert(500)
    bst1.insert(250)
    bst1.insert(750)
    bst1.insert(125)
    bst1.insert(375)
    bst1.insert(600)
    bst1.insert(800)
    bst1.insert(900)

    bst2 = BST()
    bst2.insert(500)
    bst2.insert(250)
    bst2.insert(750)
    bst2.insert(125)
    bst2.insert(375)
    bst2.insert(600)
    bst2.insert(800)
    bst2.insert(900)

    print('bst1 == bst2 ==>', BST_compare(bst1.root, bst2.root))
